# Graph Model

## Overview

This project uses a Graph Database (CognoDB) to model relationships between users and movies.

---

# Node Types

## Movie

Properties

- id
- title
- year
- rating
- duration

---

## User

Properties

- id
- name
- email
- age

---

## Genre

Properties

- name

---

## Actor

Properties

- name

---

## Director

Properties

- name

---

# Relationships

Movie → Genre

```
(:Movie)-[:BELONGS_TO]->(:Genre)
```

Movie → Actor

```
(:Movie)-[:ACTED_BY]->(:Actor)
```

Movie → Director

```
(:Movie)-[:DIRECTED_BY]->(:Director)
```

User → Movie

```
(:User)-[:LIKES]->(:Movie)
```

---

# Recommendation Flow

```
User
 │
LIKES
 │
Movie
 │
BELONGS_TO
 │
Genre
 │
BELONGS_TO
 │
Recommended Movie
```

The recommendation engine traverses the graph to find movies that belong to the same genres as the user's liked movies.

---

# Sample Cypher Query

```cypher
MATCH (u:User {name:$user})-[:LIKES]->(:Movie)-[:BELONGS_TO]->(g:Genre)

MATCH (m:Movie)-[:BELONGS_TO]->(g)

WHERE NOT (u)-[:LIKES]->(m)

RETURN DISTINCT
m.title,
m.rating
ORDER BY m.rating DESC
```