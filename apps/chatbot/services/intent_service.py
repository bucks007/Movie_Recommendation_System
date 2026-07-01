from enum import Enum
import re


class Intent(Enum):
    RECOMMEND = "recommend"
    SIMILAR = "similar"
    PERSONALIZED = "personalized"
    GENRE = "genre"
    TRENDING = "trending"
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
        r"\b(recommend|recommendation|suggest|best|top|must watch|good movies)\b",
        message
    ):
        return Intent.RECOMMEND

    # Movie information

    if re.search(
        r"\b(plot|story|director|directed|actor|actors|cast|runtime|release|released|rating|imdb)\b",
        message
    ):
        return Intent.MOVIE_INFO

    # GENRE

    if re.search(
        r"\b(action|comedy|romance|drama|thriller|crime|horror|animation|family|adventure|fantasy|sci-fi|science fiction)\b",
        message
    ):
        return Intent.GENRE
    
    # TRENDING

    if re.search(
        r"\b(trending|popular|top rated|highest rated|latest)\b",
        message
    ):
        return Intent.TRENDING

    # Search

    if re.search(
        r"\b(find|search|show)\b",
        message
    ):
        return Intent.SEARCH

    return Intent.UNKNOWN
