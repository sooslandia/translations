from sltt import context

MARKDOWN_INDENT = " " * 4
MessageList = list[str, "MessageList"]


class MessageManager:
    def __init__(self):
        self._messages = {}

    def register(self, message_list: MessageList):
        stage_context = context.current_stage_context.get()
        stage_messages_group_key = (
            stage_context["pipeline_name"],
            stage_context["stage_number"],
        )
        stage_messages_group = self._messages.setdefault(stage_messages_group_key, {})
        if not stage_messages_group:
            stage_messages_group |= {"stage_context": stage_context, "messages": []}
        stage_messages_group["messages"] += message_list

    def clear_messages(self):
        self._messages.clear()

    def get_formatted_messages(self):
        result = []
        for (
            pipeline_name,
            stage_number,
        ), stage_messages_group in self._messages.items():
            context = stage_messages_group["stage_context"]
            stage_info = f"{context['stage_number']}/{context['total_stages']}, {context['stage_name']}"
            result.append(f"Errors in pipeline {pipeline_name}, stage {stage_info}:\n")
            result.extend(
                self._get_formatted_stage_messages(stage_messages_group["messages"])
            )
            result.append("")
        return "\n".join(result)

    def _get_formatted_stage_messages(self, messages, indent_level=0):
        result = []
        for item in messages:
            if isinstance(item, str):
                result.append(f"{MARKDOWN_INDENT * indent_level}- {item}")
            elif isinstance(item, list):
                result.extend(
                    self._get_formatted_stage_messages(item, indent_level + 1)
                )
            else:
                raise ValueError(f"Unknown item type: {type(item)}")
        return result


message_manager = MessageManager()
