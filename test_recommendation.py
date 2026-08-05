from database import driver

with driver.session() as session:

    print("===== LIKES =====")

    result = session.run("""
    MATCH (u:User)-[:LIKES]->(m:Movie)
    RETURN u.name AS user, m.title AS movie
    """)

    for record in result:
        print(record["user"], "->", record["movie"])

    print("\n===== BELONGS_TO =====")

    result = session.run("""
    MATCH (m:Movie)-[:BELONGS_TO]->(g:Genre)
    RETURN m.title AS movie, g.name AS genre
    """)

    for record in result:
        print(record["movie"], "->", record["genre"])