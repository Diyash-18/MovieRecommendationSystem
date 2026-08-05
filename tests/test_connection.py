import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database import driver


def test_connection():

    with driver.session() as session:

        result = session.run(
            "RETURN 'Connected to CognoDB Successfully!' AS message"
        )

        print(result.single()["message"])


if __name__ == "__main__":
    test_connection()