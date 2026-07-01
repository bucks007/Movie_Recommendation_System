import joblib

from apps.movies.models import Movie


cosine_sim = joblib.load(
    "ml_models/cosine_similarity.joblib"
)

indices = joblib.load(
    "ml_models/movie_indices.joblib"
)

movie_ids = joblib.load(
    "ml_models/movie_ids.joblib"
)


def recommend_movies(movie_id, top_n=10):

    if movie_id not in indices:
        return []

    idx = indices[movie_id]

    similarity_scores = list(
        enumerate(cosine_sim[idx])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    similarity_scores = similarity_scores[
        1:top_n + 1
    ]

    recommended_movie_ids = [

        movie_ids[index]

        for index, _ in similarity_scores

    ]

    movies = Movie.objects.filter(
        movie_id__in=recommended_movie_ids
    )

    movie_dict = {

        movie.movie_id: movie

        for movie in movies

    }

    recommended_movies = [

        movie_dict[mid]

        for mid in recommended_movie_ids

        if mid in movie_dict

    ]

    return recommended_movies