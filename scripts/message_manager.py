class MessageManager:
    def __init__(self):
        self.messages = []

    def add_message(self, message):
        self.messages.append(message)

    def add_list_message(self, header, messages_list):
        if (total_messages := len(messages_list)) > 50:
            messages_list = messages_list[:50]
            messages_list.append(f"{total_messages-50} more...")
        self.messages.append(header)
        self.messages.extend("- " + i for i in messages_list)
        self.messages.append("\n")

    def get_messages(self):
        return self.messages


message_manager = MessageManager()
