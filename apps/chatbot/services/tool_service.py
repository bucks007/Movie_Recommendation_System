from .intent_service import Intent
from apps.movies.models import Movie
from apps.recommender.services.content_based import recommend_movies

from .movie_parser import MovieParser
from django.db.models import Q
import re

def execute_tool(
    intent,
    user,
    message
):

    if intent == Intent.GREETING:

        return {
            "type": "text",
            "message":
                "Hello! 👋 I'm your Movie AI Assistant. Ask me for recommendations, similar movies, or information about any movie."
        }

    elif intent == Intent.HELP:

        return {
            "type": "text",
            "message":
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
    elif intent == Intent.GENRE:

        return genre_tool(message)

    elif intent == Intent.TRENDING:

        return trending_tool(message)

    return {

        "type": "text",

        "message":
            "Sorry, I couldn't understand your request."

    }

# Place Holder tools

def recommend_movies_tool(message):

    return {
        "type": "text",
        "message":
            "Recommendation tool will run here."
    }

def similar_movies_tool(message):
    movie = MovieParser.find_movie(message)
    if not movie:
        return {
            "type": "text",
            "message": "I couldn't identify the movie."
        }
    recommendations = recommend_movies(
        movie.movie_id,
        top_n=8
    )
    if not recommendations:
        return {
            "type": "text",
            "message": "No similar movies found."
        }
    return {
        "type": "movies",
        "message": f"Movies similar to {movie.title}",
        "movies": [
            {
                "id": m.id,
                "title": m.title,
                "poster": (
                    m.poster_url
                    if m.poster_url and m.poster_url != "N/A"
                    else "https://placehold.co/300x450?text=No+Poster"
                ),
                "rating": m.vote_average,
                "year": (
                    m.release_date.year
                    if m.release_date
                    else ""
                ),
                "genres": m.genres
            }
            for m in recommendations
        ]
    }

def personalized_tool(user):

    return {
        "type": "text",
        "message":
            "Personalized recommendation tool will run here."
    }


def movie_info_tool(message):

    movie = MovieParser.find_movie(message)

    if not movie:

        return {

            "type": "text",

            "message": "Sorry, I couldn't identify the movie."

        }

    msg = message.lower()

    if "director" in msg or "directed" in msg:

        answer = f"{movie.title} was directed by {movie.director}."

    elif "actor" in msg or "cast" in msg:

        answer = f"The main cast includes {movie.actors}."

    elif "plot" in msg or "story" in msg:

        answer = movie.overview

    elif "runtime" in msg:

        answer = f"Runtime: {movie.runtime}"

    elif "rating" in msg or "imdb" in msg:

        answer = f"IMDb Rating: ⭐ {movie.vote_average}"

    elif "release" in msg:

        answer = f"Released on {movie.release_date}"

    else:

        answer = (
            f"🎬 {movie.title}\n\n"
            f"{movie.overview}\n\n"
            f"⭐ {movie.vote_average}"
        )

    return {

        "type": "movie_info",

        "message": answer,

        "movie": {

            "id": movie.id,

            "title": movie.title,

            "poster": movie.poster_url,

            "rating": movie.vote_average,

            "year": (
                movie.release_date.year
                if movie.release_date
                else ""
            )

        }

    }

def genre_tool(message):

    return {
        "type": "text",
        "message":
            "Genre recommendation tool will run here."
    }

def trending_tool(message):

    return {
        "type": "text",
        "message":
            "Trending movies tool will run here."
    }

def search_tool(message):

    # Remove command words from the query
    query = re.sub(
        r"\b(find|search|show)\b",
        "",
        message,
        flags=re.IGNORECASE
    ).strip()

    if not query:

        return {
            "type": "text",
            "message": "Please tell me which movie you want to search."
        }

    movies = Movie.objects.filter(
        title__icontains=query
    ).order_by("-vote_average")[:8]

    if not movies.exists():

        return {
            "type": "text",
            "message": f"No movies found for '{query}'."
        }

    return {
        "type": "movies",
        "message": f"I found {movies.count()} movie(s).",
        "movies": [
            {
                "id": movie.id,
                "title": movie.title,
                "poster": (
                    movie.poster_url
                    if movie.poster_url
                    and movie.poster_url != "N/A"
                    else "https://placehold.co/300x450?text=No+Poster"
                ),
                "rating": movie.vote_average,
                "year": (
                    movie.release_date.year
                    if movie.release_date
                    else ""
                ),
                "genres": movie.genres
            }
            for movie in movies
        ]
    }
