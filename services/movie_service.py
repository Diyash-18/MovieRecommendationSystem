from database import driver

from queries.movie_queries import (
    GET_ALL_MOVIES,
    GET_MOVIE_BY_ID,
    SEARCH_MOVIE,
    GET_COMPLETE_MOVIE_DETAILS,
    ADD_MOVIE,
    UPDATE_MOVIE,
    DELETE_MOVIE,
    CHECK_MOVIE_EXISTS
)


# =====================================
# Get All Movies
# =====================================

def get_all_movies():

    with driver.session() as session:

        result = session.run(GET_ALL_MOVIES)

        movies = []

        for record in result:
            movies.append(dict(record["m"]))

        return movies


# =====================================
# Get Movie By ID
# =====================================

def get_movie_by_id(movie_id):

    with driver.session() as session:

        result = session.run(
            GET_MOVIE_BY_ID,
            id=movie_id
        )

        record = result.single()

        if record:
            return dict(record["m"])

        return None


# =====================================
# Search Movie
# =====================================

def search_movie(title):

    with driver.session() as session:

        result = session.run(
            SEARCH_MOVIE,
            title=title
        )

        movies = []

        for record in result:
            movies.append(dict(record["m"]))

        return movies


# =====================================
# Complete Movie Details
# =====================================

def get_complete_movie_details(movie_id):

    with driver.session() as session:

        result = session.run(
            GET_COMPLETE_MOVIE_DETAILS,
            id=movie_id
        )

        record = result.single()

        if record:

            return {

                "id": record["id"],
                "title": record["title"],
                "year": record["year"],
                "rating": record["rating"],
                "duration": record["duration"],
                "genres": record["genres"],
                "actors": record["actors"],
                "directors": record["directors"]

            }

        return None


# =====================================
# Check Movie Exists
# =====================================

def movie_exists(movie_id):

    with driver.session() as session:

        result = session.run(
            CHECK_MOVIE_EXISTS,
            id=movie_id
        )

        return result.single() is not None


# =====================================
# Add Movie
# =====================================

def add_movie(movie):

    if movie_exists(movie["id"]):
        return False

    with driver.session() as session:

        session.run(
            ADD_MOVIE,
            id=movie["id"],
            title=movie["title"],
            year=movie["year"],
            rating=movie["rating"],
            duration=movie["duration"]
        )

    return True


# =====================================
# Update Movie
# =====================================

def update_movie(movie_id, movie):

    with driver.session() as session:

        session.run(
            UPDATE_MOVIE,
            id=movie_id,
            title=movie["title"],
            year=movie["year"],
            rating=movie["rating"],
            duration=movie["duration"]
        )

    return True


# =====================================
# Delete Movie
# =====================================

def delete_movie(movie_id):

    with driver.session() as session:

        session.run(
            DELETE_MOVIE,
            id=movie_id
        )

    return True