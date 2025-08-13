import contextvars

current_stage_context = contextvars.ContextVar("current_stage_context")
