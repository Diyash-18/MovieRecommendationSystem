# ==========================================
# Recommendation Queries
# ==========================================

# ---------------------------------------------------
# Recommend movies based on user's liked movie genres
# ---------------------------------------------------

RECOMMEND_MOVIES = """
MATCH (u:User {name:$user})-[:LIKES]->(liked:Movie)
MATCH (liked)-[:BELONGS_TO]->(g:Genre)
MATCH (recommended:Movie)-[:BELONGS_TO]->(g)

WHERE recommended <> liked

RETURN DISTINCT
recommended.title AS title,
recommended.rating AS rating

ORDER BY recommended.rating DESC
"""


# ---------------------------------------------------
# Movies By Genre
# ---------------------------------------------------

GET_MOVIES_BY_GENRE = """
MATCH (m:Movie)-[:BELONGS_TO]->(g:Genre)

WHERE g.name=$genre

RETURN

m.id AS id,
m.title AS title,
m.year AS year,
m.rating AS rating

ORDER BY m.rating DESC
"""


# ---------------------------------------------------
# Movies By Actor
# ---------------------------------------------------

GET_MOVIES_BY_ACTOR = """
MATCH (m:Movie)-[:ACTED_BY]->(a:Actor)

WHERE a.name=$actor

RETURN

m.id AS id,
m.title AS title,
m.year AS year,
m.rating AS rating

ORDER BY m.rating DESC
"""


# ---------------------------------------------------
# Movies By Director
# ---------------------------------------------------

GET_MOVIES_BY_DIRECTOR = """
MATCH (m:Movie)-[:DIRECTED_BY]->(d:Director)

WHERE d.name=$director

RETURN

m.id AS id,
m.title AS title,
m.year AS year,
m.rating AS rating

ORDER BY m.rating DESC
"""


# ---------------------------------------------------
# Similar Movies
# ---------------------------------------------------

GET_SIMILAR_MOVIES = """
MATCH (m1:Movie {title:$title})-[:BELONGS_TO]->(g:Genre)

MATCH (m2:Movie)-[:BELONGS_TO]->(g)

WHERE m1 <> m2

RETURN DISTINCT

m2.id AS id,
m2.title AS title,
m2.rating AS rating

ORDER BY m2.rating DESC
"""


# ---------------------------------------------------
# Movies Liked By User
# ---------------------------------------------------

GET_USER_LIKED_MOVIES = """
MATCH (u:User {name:$user})-[:LIKES]->(m:Movie)

RETURN

m.title AS title,
m.rating AS rating
"""


# ---------------------------------------------------
# Movies Directed By Same Director
# ---------------------------------------------------

GET_SAME_DIRECTOR_MOVIES = """
MATCH (m1:Movie {title:$title})-[:DIRECTED_BY]->(d:Director)

MATCH (m2:Movie)-[:DIRECTED_BY]->(d)

WHERE m1 <> m2

RETURN

m2.title AS title,
m2.rating AS rating
"""


# ---------------------------------------------------
# Movies With Same Actor
# ---------------------------------------------------

GET_SAME_ACTOR_MOVIES = """
MATCH (m1:Movie {title:$title})-[:ACTED_BY]->(a:Actor)

MATCH (m2:Movie)-[:ACTED_BY]->(a)

WHERE m1 <> m2

RETURN

m2.title AS title,
m2.rating AS rating
"""


# ---------------------------------------------------
# Multi-Hop Recommendation
# User -> Movie -> Genre -> Movie
# ---------------------------------------------------

MULTI_HOP_RECOMMENDATION = """
MATCH (u:User {name:$user})-[:LIKES]->(:Movie)-[:BELONGS_TO]->(g:Genre)

MATCH (recommended:Movie)-[:BELONGS_TO]->(g)

WHERE NOT (u)-[:LIKES]->(recommended)

RETURN DISTINCT

recommended.title AS title,
recommended.rating AS rating

ORDER BY recommended.rating DESC
"""