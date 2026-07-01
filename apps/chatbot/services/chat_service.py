from .intent_service import detect_intent
from .tool_service import execute_tool

def process_message(user,message):
    intent = detect_intent(message)
    result = execute_tool(
        intent,
        user,
        message
    )
    return result