from flask import Blueprint, request, jsonify, redirect

from services.movie_service import (
    get_all_movies,
    get_movie_by_id,
    search_movie,
    get_complete_movie_details,
    add_movie,
    update_movie,
    delete_movie
)

movie_bp = Blueprint("movie_bp", __name__)


# =====================================
# Get All Movies
# =====================================

@movie_bp.route("/movies", methods=["GET"])
def movies():

    movies = get_all_movies()

    return jsonify({
        "status": "success",
        "count": len(movies),
        "movies": movies
    })


# =====================================
# Get Movie By ID
# =====================================

@movie_bp.route("/movies/<int:movie_id>", methods=["GET"])
def movie(movie_id):

    movie = get_movie_by_id(movie_id)

    if movie:

        return jsonify({
            "status": "success",
            "movie": movie
        })

    return jsonify({
        "status": "failed",
        "message": "Movie not found"
    }), 404


# =====================================
# Search Movie
# =====================================

@movie_bp.route("/search", methods=["GET"])
def search():

    title = request.args.get("title")

    movies = search_movie(title)

    return jsonify({
        "status": "success",
        "count": len(movies),
        "movies": movies
    })


# =====================================
# Complete Movie Details
# =====================================

@movie_bp.route("/movie-details/<int:movie_id>", methods=["GET"])
def movie_details(movie_id):

    movie = get_complete_movie_details(movie_id)

    if movie:

        return jsonify({
            "status": "success",
            "movie": movie
        })

    return jsonify({
        "status": "failed",
        "message": "Movie not found"
    }), 404


# =====================================
# Add Movie
# =====================================

@movie_bp.route("/add-movie", methods=["POST"])
def add_new_movie():

    movie = {
        "id": int(request.form["id"]),
        "title": request.form["title"],
        "year": int(request.form["year"]),
        "rating": float(request.form["rating"]),
        "duration": int(request.form["duration"])
    }

    success = add_movie(movie)

    if not success:

        return jsonify({
            "status": "failed",
            "message": "Movie ID already exists"
        }), 400

    return redirect("/movies-page")


# =====================================
# Edit Movie
# =====================================

@movie_bp.route("/edit-movie/<int:movie_id>", methods=["POST"])
def edit_movie(movie_id):

    movie = {
        "title": request.form["title"],
        "year": int(request.form["year"]),
        "rating": float(request.form["rating"]),
        "duration": int(request.form["duration"])
    }

    update_movie(movie_id, movie)

    return redirect("/movies-page")


# =====================================
# Delete Movie
# =====================================

@movie_bp.route("/delete-movie/<int:movie_id>", methods=["GET"])
def remove_movie(movie_id):

    delete_movie(movie_id)

    return redirect("/movies-page")