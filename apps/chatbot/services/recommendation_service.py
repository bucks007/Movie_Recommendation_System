from apps.movies.models import Movie
from django.db.models import Q

GENRES = [
        "Action",
        "Adventure",
        "Animation",
        "Comedy",
        "Crime",
        "Documentary",
        "Drama",
        "Fantasy",
        "Horror",
        "Mystery",
        "Romance",
        "Sci-Fi",
        "Thriller",
        "War",
        "Western",
    ]

def get_movies_by_genre(genre, limit=10):

    movies = (
        Movie.objects.filter(
            genres__icontains=genre
        )
        .exclude(
            poster_url=""
        )
        .order_by(
            "-vote_average"
        )[:limit]
    )

    return list(movies)


def get_top_movies(limit=10):

    movies = (
        Movie.objects.exclude(
            poster_url=""
        )
        .order_by(
            "-vote_average"
        )[:limit]
    )

    return list(movies)


def get_trending_movies(limit=10):

    movies = (
        Movie.objects.exclude(
            poster_url=""
        )
        .order_by(
            "-vote_average",
            "-release_date"
        )[:limit]
    )

    return list(movies)

def get_top_rated_movies(limit=12):

    return Movie.objects.exclude(
        vote_average__isnull=True
    ).order_by(
        "-vote_average"
    )[:limit]

def get_latest_movies(limit=12):

    return Movie.objects.exclude(
        release_date__isnull=True
    ).order_by(
        "-release_date"
    )[:limit]

def get_movies_by_actor(actor):

    return Movie.objects.filter(
        actors__icontains=actor
    ).order_by(
        "-vote_average"
    )[:12]

def get_movies_by_director(director):

    return Movie.objects.filter(
        director__icontains=director
    ).order_by(
        "-vote_average"
    )[:12]

def get_movies_by_year(year):

    return Movie.objects.filter(
        release_date__year=year
    ).order_by(
        "-vote_average"
    )[:12]