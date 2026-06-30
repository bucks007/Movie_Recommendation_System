from .intent_service import Intent


def execute_tool(
    intent,
    user,
    message
):

    if intent == Intent.GREETING:

        return {
            "type": "text",
            "response":
                "Hello! 👋 I'm your Movie AI Assistant. Ask me for recommendations, similar movies, or information about any movie."
        }

    elif intent == Intent.HELP:

        return {
            "type": "text",
            "response":
                "I can recommend movies, find similar movies, search movies, explain plots, and provide personalized recommendations."
        }

    elif intent == Intent.RECOMMEND:

        return recommend_movies_tool(
            message
        )

    elif intent == Intent.SIMILAR:

        return similar_movies_tool(
            message
        )

    elif intent == Intent.PERSONALIZED:

        return personalized_tool(
            user
        )

    elif intent == Intent.MOVIE_INFO:

        return movie_info_tool(
            message
        )

    elif intent == Intent.SEARCH:

        return search_tool(
            message
        )

    return {

        "type": "text",

        "response":
            "Sorry, I couldn't understand your request."

    }

# Place Holder tools

def recommend_movies_tool(message):

    return {
        "type": "text",
        "response":
            "Recommendation tool will run here."
    }


def similar_movies_tool(message):

    return {
        "type": "text",
        "response":
            "Similar movie tool will run here."
    }


def personalized_tool(user):

    return {
        "type": "text",
        "response":
            "Personalized recommendation tool will run here."
    }


def movie_info_tool(message):

    return {
        "type": "text",
        "response":
            "Movie information tool will run here."
    }


def search_tool(message):

    return {
        "type": "text",
        "response":
            "Movie search tool will run here."
    }