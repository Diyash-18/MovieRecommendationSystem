# 🎬 Movie Recommendation System using CognoDB

## 📌 Project Overview

The Movie Recommendation System is a graph-based web application developed using **Python**, **Flask**, and **CognoDB**. The application stores movies, users, genres, actors, and directors as graph nodes and uses graph traversal to recommend movies based on user interests.

Unlike traditional SQL databases, CognoDB efficiently manages highly connected data using nodes and relationships, making it ideal for recommendation systems.

---

# Features

- View All Movies
- Search Movies
- View Movie Details
- Add New Movie
- Edit Movie
- Delete Movie
- Personalized Movie Recommendations
- Graph Database Traversal
- Responsive Bootstrap User Interface
- REST API Support

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

# Project Structure

```
MovieRecommendationSystem/
│
├── queries/
│   ├── movie_queries.py
│   └── recommendation_queries.py
│
├── routes/
│   ├── movie_routes.py
│   └── recommendation_routes.py
│
├── services/
│   ├── movie_service.py
│   └── recommendation_service.py
│
├── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── tests/
│
├── app.py
├── config.py
├── database.py
├── seed.py
├── requirements.txt
├── README.md
├── GRAPH_MODEL.md
├── PROJECT_REPORT.md
└── .gitignore
```

---

# Why a Graph Database?

Traditional relational databases store data in tables and retrieve related information using JOIN operations.

This project contains highly connected entities such as:

- Users
- Movies
- Genres
- Actors
- Directors

Graph databases like CognoDB store these relationships directly, making recommendation queries much faster and easier than multiple SQL JOIN operations.

Example relationships:

```
User ------LIKES------> Movie

Movie -----BELONGS_TO-----> Genre

Movie -----DIRECTED_BY-----> Director

Movie -----ACTED_BY-----> Actor
```

The recommendation engine traverses these relationships to suggest movies based on the genres of movies liked by a user.

---

# Graph Data Model

```
                +-----------+
                |   User    |
                +-----------+
                     |
                   LIKES
                     |
                     ▼
                +-----------+
                |   Movie   |
                +-----------+
                 /    |    \
                /     |     \
               ▼      ▼      ▼
           Genre   Actor  Director
```

## Nodes

- User
- Movie
- Genre
- Actor
- Director

## Relationships

- LIKES
- BELONGS_TO
- ACTED_BY
- DIRECTED_BY

---

# Main Cypher Queries

## Get All Movies

```cypher
MATCH (m:Movie)
RETURN m;
```

---

## Get Movie By ID

```cypher
MATCH (m:Movie {id:$id})
RETURN m;
```

---

## Search Movie

```cypher
MATCH (m:Movie)
WHERE toLower(m.title) CONTAINS toLower($title)
RETURN m;
```

---

## Recommendation Query

```cypher
MATCH (u:User {name:$user})-[:LIKES]->(:Movie)-[:BELONGS_TO]->(g:Genre)

MATCH (m:Movie)-[:BELONGS_TO]->(g)

WHERE NOT (u)-[:LIKES]->(m)

RETURN DISTINCT
m.title,
m.rating
ORDER BY m.rating DESC;
```

---

## Movies By Director

```cypher
MATCH (m:Movie)-[:DIRECTED_BY]->(d:Director)
RETURN m,d;
```

---

## Movies By Actor

```cypher
MATCH (m:Movie)-[:ACTED_BY]->(a:Actor)
RETURN m,a;
```

---

## Movies By Genre

```cypher
MATCH (m:Movie)-[:BELONGS_TO]->(g:Genre)
RETURN m,g;
```

---

# REST APIs

## Get All Movies

```
GET /movies
```

---

## Get Movie By ID

```
GET /movies/<id>
```

---

## Search Movie

```
GET /search?title=MovieName
```

---

## Add Movie

```
POST /add-movie
```

---

## Update Movie

```
POST /edit-movie/<id>
```

---

## Delete Movie

```
GET /delete-movie/<id>
```

---

## Recommendation

```
GET /recommend/Aravind
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Diyash-18/MovieRecommendationSystem.git
```

Move into the project folder

```bash
cd MovieRecommendationSystem
```

Create a virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Seed the database

```bash
python seed.py
```

Run the application

```bash
python app.py
```

Open in browser

```
http://127.0.0.1:5000
```

---

# Testing

Database Connection

```bash
python tests/test_connection.py
```

Verify Database

```bash
python tests/verify_db.py
```

Recommendation Test

```bash
python tests/test_recommendation.py
```

---

# Project Features

- Graph Database Implementation
- Movie CRUD Operations
- Search Functionality
- Recommendation Engine
- Multi-Hop Graph Traversal
- Parameterized Cypher Queries
- Responsive Bootstrap UI
- REST API Integration
- Modular Flask Architecture

---

# Future Enhancements

- User Authentication
- Login & Registration
- Movie Posters API
- User Ratings
- Watchlist Feature
- AI-Based Recommendations
- Admin Dashboard
- Collaborative Filtering
- Movie Reviews

---

# Developed By

**DIYA**

Movie Recommendation System

Developed using **Python**, **Flask**, and **CognoDB** as part of the CognoDB Assignment.