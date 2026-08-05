from database import driver

with driver.session() as session:

    result = session.run("""
    MATCH (n)
    RETURN
        count(n) AS nodes
    """)

    print("Nodes:", result.single()["nodes"])

    result = session.run("""
    MATCH ()-[r]->()
    RETURN
        count(r) AS relationships
    """)

    print("Relationships:", result.single()["relationships"])

    result = session.run("""
    MATCH (m:Movie)
    RETURN m.title AS title
    """)

    print("\nMovies:")

    for record in result:
        print(record["title"])

    result = session.run("""
    MATCH (u:User)
    RETURN u.name AS name
    """)

    print("\nUsers:")

    for record in result:
        print(record["name"])