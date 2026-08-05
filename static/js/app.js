/* ==========================================
   Movie Recommendation System
   app.js
========================================== */

console.log("Movie Recommendation System Loaded");

/* ------------------------------------------
   Delete Confirmation
------------------------------------------ */

function confirmDelete(movieId) {

    let choice = confirm(
        "Are you sure you want to delete this movie?"
    );

    if (choice) {

        window.location.href = "/delete-movie/" + movieId;

    }

}

/* ------------------------------------------
   Search Validation
------------------------------------------ */

function validateSearch() {

    let searchBox = document.querySelector(
        "input[name='title']"
    );

    if (!searchBox) {
        return true;
    }

    if (searchBox.value.trim() === "") {

        alert("Please enter a movie name.");

        searchBox.focus();

        return false;
    }

    return true;
}

/* ------------------------------------------
   Add Movie Validation
------------------------------------------ */

function validateMovieForm() {

    let title = document.querySelector(
        "input[name='title']"
    );

    let rating = document.querySelector(
        "input[name='rating']"
    );

    let duration = document.querySelector(
        "input[name='duration']"
    );

    if (title.value.trim() === "") {

        alert("Movie title is required.");

        return false;

    }

    if (rating.value < 0 || rating.value > 10) {

        alert("Rating must be between 0 and 10.");

        return false;

    }

    if (duration.value <= 0) {

        alert("Duration must be greater than 0.");

        return false;

    }

    return true;
}

/* ------------------------------------------
   Highlight Current Navigation Link
------------------------------------------ */

document.addEventListener("DOMContentLoaded", function () {

    let currentPath = window.location.pathname;

    let navLinks = document.querySelectorAll(".nav-link");

    navLinks.forEach(function(link) {

        if (link.getAttribute("href") === currentPath) {

            link.classList.add("active");

        }

    });

});

/* ------------------------------------------
   Welcome Message
------------------------------------------ */

window.onload = function () {

    console.log("Welcome to Movie Recommendation System");

};