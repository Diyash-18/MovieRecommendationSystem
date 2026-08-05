# 🎬 Movie Recommendation System using CognoDB

## 📌 Project Overview

The Movie Recommendation System is a graph-based web application developed using Python, Flask, and CognoDB. It stores movies, users, genres, actors, and directors as graph nodes and recommends movies based on user interests using graph traversal.

This project demonstrates how graph databases can efficiently model relationships and generate personalized recommendations.

---

# Features

- View All Movies
- Search Movies
- View Movie Details
- Movie Recommendation
- Add Movie
- Edit Movie
- Delete Movie
- Graph Database Traversal
- Responsive Bootstrap UI

---

# Technologies Used

## Backend

- Python 3
- Flask

## Database

- CognoDB
- Neo4j Python Driver

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

---

# Folder Structure

```
MovieRecommendationSystem
│
├── queries
├── routes
├── services
├── static
│   ├── css
│   ├── images
│   └── js
├── templates
├── tests
├── app.py
├── config.py
├── database.py
├── seed.py
├── requirements.txt
├── README.md
├── GRAPH_MODEL.md
└── .env
```

---

# Database Nodes

- Movie
- User
- Genre
- Actor
- Director

---

# Relationships

- BELONGS_TO
- DIRECTED_BY
- ACTED_BY
- LIKES

---

# APIs

## Movies

GET

```
/movies
```

---

## Movie By ID

GET

```
/movies/<id>
```

---

## Search Movie

GET

```
/search?title=Movie
```

---

## Recommendations

GET

```
/recommend/Aravind
```

---

## Add Movie

POST

```
/add-movie
```

---

## Update Movie

POST

```
/edit-movie/<id>
```

---

## Delete Movie

GET

```
/delete-movie/<id>
```

---

# Installation

Clone the project

```
git clone YOUR_REPOSITORY_URL
```

Create Virtual Environment

```
python -m venv venv
```

Activate

Windows

```
venv\Scripts\activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Run Seeder

```
python seed.py
```

Run Application

```
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

# Testing

Database Connection

```
python tests/test_connection.py
```

Verify Database

```
python tests/verify_db.py
```

Recommendation Test

```
python tests/test_recommendation.py
```

---

# Future Enhancements

- Authentication
- User Login
- Movie Posters API
- Collaborative Filtering
- Machine Learning Recommendations
- Admin Dashboard

---

# Developed by


DIYA

Movie Recommendation System

CognoDB Assignment 2026