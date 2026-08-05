import os
from flask import Flask, render_template, request

from routes.movie_routes import movie_bp
from routes.recommendation_routes import recommendation_bp

from services.movie_service import (
    get_all_movies,
    get_movie_by_id
)

from services.recommendation_service import recommend_movies

app = Flask(__name__)

# ==========================================
# Register Blueprints
# ==========================================

app.register_blueprint(movie_bp)
app.register_blueprint(recommendation_bp)


# ==========================================
# Home Page
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# Movies Page
# ==========================================

@app.route("/movies-page")
def movies_page():

    movies = get_all_movies()

    return render_template(
        "movies.html",
        movies=movies
    )


# ==========================================
# Movie Details Page
# ==========================================

@app.route("/movie-page/<int:movie_id>")
def movie_page(movie_id):

    movie = get_movie_by_id(movie_id)

    if movie is None:
        return "Movie Not Found", 404

    # Calculate progress for the progress bar
    movie["progress"] = int(movie["rating"] * 10)

    return render_template(
        "movie_details.html",
        movie=movie
    )


# ==========================================
# Recommendation Page
# ==========================================

@app.route("/recommend-page", methods=["GET", "POST"])
def recommend_page():

    recommendations = []

    if request.method == "POST":

        user = request.form["user"]

        recommendations = recommend_movies(user)

    return render_template(
        "recommendations.html",
        recommendations=recommendations
    )


# ==========================================
# Add Movie Page
# ==========================================

@app.route("/add-movie-page")
def add_movie_page():

    return render_template(
        "add_movie.html"
    )


# ==========================================
# Edit Movie Page
# ==========================================

@app.route("/edit-movie-page/<int:movie_id>")
def edit_movie_page(movie_id):

    movie = get_movie_by_id(movie_id)

    if movie is None:

        return "Movie Not Found", 404

    movie["genre"] = ""
    movie["director"] = ""
    movie["actor"] = ""

    return render_template(
        "edit_movie.html",
        movie=movie
    )


# ==========================================
# Run Flask
# ==========================================

# ==========================================
# Run Flask
# ==========================================

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )