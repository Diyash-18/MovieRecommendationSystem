import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import driver


def verify_database():

    with driver.session() as session:

        nodes = session.run("""
        MATCH (n)
        RETURN count(n) AS total
        """).single()["total"]

        relationships = session.run("""
        MATCH ()-[r]->()
        RETURN count(r) AS total
        """).single()["total"]

        print("=" * 40)
        print("DATABASE SUMMARY")
        print("=" * 40)

        print(f"Total Nodes         : {nodes}")
        print(f"Total Relationships : {relationships}")

        print("\nMovies")

        movies = session.run("""
        MATCH (m:Movie)
        RETURN m.title AS title
        ORDER BY title
        """)

        for movie in movies:
            print("•", movie["title"])

        print("\nUsers")

        users = session.run("""
        MATCH (u:User)
        RETURN u.name AS name
        ORDER BY name
        """)

        for user in users:
            print("•", user["name"])


if __name__ == "__main__":
    verify_database()