from flask import Blueprint, jsonify

from services.recommendation_service import (
    recommend_movies,
    get_movies_by_genre,
    get_movies_by_actor,
    get_movies_by_director,
    get_similar_movies
)

recommendation_bp = Blueprint(
    "recommendation",
    __name__
)


# ============================================
# Recommend Movies for User
# ============================================

@recommendation_bp.route("/recommend/<string:user_name>", methods=["GET"])
def recommend(user_name):

    movies = recommend_movies(user_name)

    return jsonify({

        "status": "success",

        "user": user_name,

        "recommendations": movies

    })


# ============================================
# Movies by Genre
# ============================================

@recommendation_bp.route("/genre/<string:genre>", methods=["GET"])
def movies_by_genre(genre):

    movies = get_movies_by_genre(genre)

    return jsonify({

        "status": "success",

        "genre": genre,

        "movies": movies

    })


# ============================================
# Movies by Actor
# ============================================

@recommendation_bp.route("/actor/<string:actor>", methods=["GET"])
def movies_by_actor(actor):

    movies = get_movies_by_actor(actor)

    return jsonify({

        "status": "success",

        "actor": actor,

        "movies": movies

    })


# ============================================
# Movies by Director
# ============================================

@recommendation_bp.route("/director/<string:director>", methods=["GET"])
def movies_by_director(director):

    movies = get_movies_by_director(director)

    return jsonify({

        "status": "success",

        "director": director,

        "movies": movies

    })


# ============================================
# Similar Movies
# ============================================

@recommendation_bp.route("/similar/<string:title>", methods=["GET"])
def similar_movies(title):

    movies = get_similar_movies(title)

    return jsonify({

        "status": "success",

        "movie": title,

        "similar_movies": movies

    })