import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import driver


def test_recommendation(user):

    with driver.session() as session:

        result = session.run("""

        MATCH (u:User {name:$user})-[:LIKES]->(liked:Movie)

        MATCH (liked)-[:BELONGS_TO]->(g:Genre)

        MATCH (recommended:Movie)-[:BELONGS_TO]->(g)

        WHERE recommended <> liked

        RETURN DISTINCT

        recommended.title AS title,
        recommended.rating AS rating

        ORDER BY recommended.rating DESC

        """, user=user)

        print("=" * 40)
        print("RECOMMENDED MOVIES")
        print("=" * 40)

        movies = list(result)

        if not movies:

            print("No recommendations found.")
            return

        for movie in movies:

            print(f"{movie['title']}  ⭐ {movie['rating']}")


if __name__ == "__main__":

    test_recommendation("Aravind")