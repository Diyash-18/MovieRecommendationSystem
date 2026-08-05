from database import driver

from queries.recommendation_queries import (
    RECOMMEND_MOVIES,
    GET_MOVIES_BY_GENRE,
    GET_MOVIES_BY_ACTOR,
    GET_MOVIES_BY_DIRECTOR,
    GET_SIMILAR_MOVIES,
    GET_USER_LIKED_MOVIES,
    GET_SAME_DIRECTOR_MOVIES,
    GET_SAME_ACTOR_MOVIES,
    MULTI_HOP_RECOMMENDATION
)


# ==========================================
# Recommend Movies for User
# ==========================================

def recommend_movies(user):

    with driver.session() as session:

        result = session.run(
            RECOMMEND_MOVIES,
            user=user
        )

        recommendations = []

        for record in result:

            recommendations.append({
                "title": record["title"],
                "rating": record["rating"]
            })

        return recommendations


# ==========================================
# Movies By Genre
# ==========================================

def get_movies_by_genre(genre):

    with driver.session() as session:

        result = session.run(
            GET_MOVIES_BY_GENRE,
            genre=genre
        )

        movies = []

        for record in result:

            movies.append({

                "id": record["id"],
                "title": record["title"],
                "year": record["year"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Movies By Actor
# ==========================================

def get_movies_by_actor(actor):

    with driver.session() as session:

        result = session.run(
            GET_MOVIES_BY_ACTOR,
            actor=actor
        )

        movies = []

        for record in result:

            movies.append({

                "id": record["id"],
                "title": record["title"],
                "year": record["year"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Movies By Director
# ==========================================

def get_movies_by_director(director):

    with driver.session() as session:

        result = session.run(
            GET_MOVIES_BY_DIRECTOR,
            director=director
        )

        movies = []

        for record in result:

            movies.append({

                "id": record["id"],
                "title": record["title"],
                "year": record["year"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Similar Movies
# ==========================================

def get_similar_movies(title):

    with driver.session() as session:

        result = session.run(
            GET_SIMILAR_MOVIES,
            title=title
        )

        movies = []

        for record in result:

            movies.append({

                "id": record["id"],
                "title": record["title"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# User Liked Movies
# ==========================================

def get_user_liked_movies(user):

    with driver.session() as session:

        result = session.run(
            GET_USER_LIKED_MOVIES,
            user=user
        )

        movies = []

        for record in result:

            movies.append({

                "title": record["title"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Movies by Same Director
# ==========================================

def get_same_director_movies(title):

    with driver.session() as session:

        result = session.run(
            GET_SAME_DIRECTOR_MOVIES,
            title=title
        )

        movies = []

        for record in result:

            movies.append({

                "title": record["title"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Movies by Same Actor
# ==========================================

def get_same_actor_movies(title):

    with driver.session() as session:

        result = session.run(
            GET_SAME_ACTOR_MOVIES,
            title=title
        )

        movies = []

        for record in result:

            movies.append({

                "title": record["title"],
                "rating": record["rating"]

            })

        return movies


# ==========================================
# Multi-Hop Recommendation
# ==========================================

def multi_hop_recommendation(user):

    with driver.session() as session:

        result = session.run(
            MULTI_HOP_RECOMMENDATION,
            user=user
        )

        recommendations = []

        for record in result:

            recommendations.append({

                "title": record["title"],
                "rating": record["rating"]

            })

        return recommendations