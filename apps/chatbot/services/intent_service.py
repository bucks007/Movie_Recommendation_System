from enum import Enum
import re


class Intent(Enum):
    RECOMMEND = "recommend"
    SIMILAR = "similar"
    PERSONALIZED = "personalized"
    MOVIE_INFO = "movie_info"
    SEARCH = "search"
    GREETING = "greeting"
    HELP = "help"
    UNKNOWN = "unknown"

def detect_intent(message):
    message = message.lower().strip()

    # Greeting

    if re.search(
        r"\b(hi|hello|hey|good morning|good evening)\b",
        message
    ):
        return Intent.GREETING

    # Help

    if re.search(
        r"\b(help|what can you do)\b",
        message
    ):
        return Intent.HELP

    # Personalized

    if re.search(
        r"\b(for me|recommend me|my recommendations|personalized)\b",
        message
    ):
        return Intent.PERSONALIZED

    # Similar movie

    if re.search(
        r"\b(similar|like)\b",
        message
    ):
        return Intent.SIMILAR

    # Recommendation

    if re.search(
        r"\b(recommend|suggest|best|top)\b",
        message
    ):
        return Intent.RECOMMEND

    # Movie information

    if re.search(
        r"\b(plot|director|actor|cast|story|who directed|who is)\b",
        message
    ):
        return Intent.MOVIE_INFO

    # Search

    if re.search(
        r"\b(find|search|show)\b",
        message
    ):
        return Intent.SEARCH

    return Intent.UNKNOWN