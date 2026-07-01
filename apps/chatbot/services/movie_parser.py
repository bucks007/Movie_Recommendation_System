import re
from rapidfuzz import process, fuzz
from apps.movies.models import Movie


class MovieParser:

    @staticmethod
    def clean_query(message):

        query = re.sub(
            r"\b("
            r"who|what|when|where|tell|me|about|"
            r"director|directed|actor|actors|cast|"
            r"plot|story|runtime|release|released|"
            r"rating|imdb|movie|movies|film|"
            r"similar|like|recommend|recommended|"
            r"recommendation|suggest|show|find|search|"
            r"to|for|of|is|the"
            r")\b",
            "",
            message,
            flags=re.IGNORECASE,
        )

        return re.sub(r"\s+", " ", query).strip()


    @staticmethod
    def find_movie(message):

        query = MovieParser.clean_query(message)

        if not query:
            return None

        # -------------------------
        # 1 Exact Match
        # -------------------------

        movie = Movie.objects.filter(
            title__iexact=query
        ).first()

        if movie:
            return movie

        # -------------------------
        # 2 Partial Match
        # -------------------------

        movies = Movie.objects.filter(
            title__icontains=query
        )

        if movies.exists():
            return movies.order_by(
                "-vote_average",
                "-release_date"
            ).first()

        if movie:
            return movie

        # -------------------------
        # 3 RapidFuzz
        # -------------------------

        movies = list(
            Movie.objects.only(
                "id",
                "title"
            )
        )

        titles = [
            m.title
            for m in movies
        ]

        match = process.extractOne(
            query,
            titles,
            scorer=fuzz.WRatio
        )

        if not match:
            return None

        title, score, _ = match

        if score < 80:
            return None

        for movie in movies:

            if movie.title == title:

                return Movie.objects.get(
                    id=movie.id
                )

        return None