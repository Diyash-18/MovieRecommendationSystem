# ==========================================
# Movie Queries
# ==========================================

# ------------------------------------------
# Get All Movies
# ------------------------------------------

GET_ALL_MOVIES = """
MATCH (m:Movie)
RETURN m
ORDER BY m.title
"""


# ------------------------------------------
# Get Movie By ID
# ------------------------------------------

GET_MOVIE_BY_ID = """
MATCH (m:Movie {id:$id})
RETURN m
"""


# ------------------------------------------
# Search Movie
# ------------------------------------------

SEARCH_MOVIE = """
MATCH (m:Movie)
WHERE toLower(m.title) CONTAINS toLower($title)
RETURN m
ORDER BY m.title
"""


# ------------------------------------------
# Get Complete Movie Details
# ------------------------------------------

GET_COMPLETE_MOVIE_DETAILS = """
MATCH (m:Movie {id:$id})

OPTIONAL MATCH (m)-[:BELONGS_TO]->(g:Genre)
OPTIONAL MATCH (m)-[:ACTED_BY]->(a:Actor)
OPTIONAL MATCH (m)-[:DIRECTED_BY]->(d:Director)

RETURN

m.id AS id,
m.title AS title,
m.year AS year,
m.rating AS rating,
m.duration AS duration,

collect(DISTINCT g.name) AS genres,
collect(DISTINCT a.name) AS actors,
collect(DISTINCT d.name) AS directors
"""


# ==========================================
# CRUD Queries
# ==========================================

# ------------------------------------------
# Check Movie Exists
# ------------------------------------------

CHECK_MOVIE_EXISTS = """
MATCH (m:Movie {id:$id})
RETURN m
"""


# ------------------------------------------
# Add Movie
# ------------------------------------------

ADD_MOVIE = """
CREATE (m:Movie {

    id:$id,

    title:$title,

    year:$year,

    rating:$rating,

    duration:$duration

})

RETURN m
"""


# ------------------------------------------
# Update Movie
# ------------------------------------------

UPDATE_MOVIE = """
MATCH (m:Movie {id:$id})

SET

m.title = $title,
m.year = $year,
m.rating = $rating,
m.duration = $duration

RETURN m
"""


# ------------------------------------------
# Delete Movie
# ------------------------------------------

DELETE_MOVIE = """
MATCH (m:Movie {id:$id})

DETACH DELETE m
"""