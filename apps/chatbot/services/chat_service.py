from .intent_service import detect_intent

def process_message(user, message):

    intent = detect_intent(message)

    return f"Intent detected: {intent.value}"