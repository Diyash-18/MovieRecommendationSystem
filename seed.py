from database import driver


def seed_database():

    with driver.session() as session:

        # ---------------------------------------------------
        # Delete existing database
        # ---------------------------------------------------

        session.run("""
        MATCH (n)
        DETACH DELETE n
        """)

        print("Old data deleted.")

        # ---------------------------------------------------
        # Create Genres
        # ---------------------------------------------------

        genres = [
            "Action",
            "Adventure",
            "Drama",
            "Comedy",
            "Sci-Fi",
            "Thriller"
        ]

        for genre in genres:
            session.run("""
            CREATE (:Genre {name:$name})
            """, name=genre)

        print("Genres Created")

        # ---------------------------------------------------
        # Create Directors
        # ---------------------------------------------------

        directors = [
            "Christopher Nolan",
            "James Cameron",
            "Steven Spielberg",
            "Rajkumar Hirani"
        ]

        for director in directors:
            session.run("""
            CREATE (:Director {name:$name})
            """, name=director)

        print("Directors Created")

        # ---------------------------------------------------
        # Create Actors
        # ---------------------------------------------------

        actors = [
            "Leonardo DiCaprio",
            "Matthew McConaughey",
            "Tom Hanks",
            "Aamir Khan"
        ]

        for actor in actors:
            session.run("""
            CREATE (:Actor {name:$name})
            """, name=actor)

        print("Actors Created")

        # ---------------------------------------------------
        # Create Movies
        # ---------------------------------------------------

        movies = [

            {
                "id": 1,
                "title": "Inception",
                "year": 2010,
                "rating": 8.8,
                "duration": 148
            },

            {
                "id": 2,
                "title": "Interstellar",
                "year": 2014,
                "rating": 8.7,
                "duration": 169
            },

            {
                "id": 3,
                "title": "Titanic",
                "year": 1997,
                "rating": 7.9,
                "duration": 195
            },

            {
                "id": 4,
                "title": "3 Idiots",
                "year": 2009,
                "rating": 8.4,
                "duration": 170
            }

        ]

        for movie in movies:

            session.run("""

            CREATE (:Movie {

                id:$id,

                title:$title,

                year:$year,

                rating:$rating,

                duration:$duration

            })

            """,

            id=movie["id"],
            title=movie["title"],
            year=movie["year"],
            rating=movie["rating"],
            duration=movie["duration"]
            )

        print("Movies Created")

        # ---------------------------------------------------
        # Create Users
        # ---------------------------------------------------

        users = [

            {
                "id": 1,
                "name": "Aravind",
                "email": "aravind@gmail.com",
                "age": 22
            },

            {
                "id": 2,
                "name": "Rahul",
                "email": "rahul@gmail.com",
                "age": 24
            },

            {
                "id": 3,
                "name": "John",
                "email": "john@gmail.com",
                "age": 27
            }

        ]

        for user in users:

            session.run("""

            CREATE (:User {

                id:$id,

                name:$name,

                email:$email,

                age:$age

            })

            """,

            id=user["id"],
            name=user["name"],
            email=user["email"],
            age=user["age"]
            )

        print("Users Created")

        # ---------------------------------------------------
        # Movie -> Genre
        # ---------------------------------------------------

        relationships = [

            ("Inception", "Sci-Fi"),
            ("Interstellar", "Sci-Fi"),
            ("Titanic", "Drama"),
            ("3 Idiots", "Comedy")

        ]

        for movie, genre in relationships:

            session.run("""

            MATCH (m:Movie {title:$movie})

            MATCH (g:Genre {name:$genre})

            CREATE (m)-[:BELONGS_TO]->(g)

            """,

            movie=movie,
            genre=genre
            )

        print("Movie-Genre Relationships Created")

        # ---------------------------------------------------
        # Movie -> Actor
        # ---------------------------------------------------

        actor_relationships = [

            ("Titanic", "Leonardo DiCaprio"),

            ("Interstellar", "Matthew McConaughey"),

            ("3 Idiots", "Aamir Khan")

        ]

        for movie, actor in actor_relationships:

            session.run("""

            MATCH (m:Movie {title:$movie})

            MATCH (a:Actor {name:$actor})

            CREATE (m)-[:ACTED_BY]->(a)

            """,

            movie=movie,
            actor=actor
            )

        print("Movie-Actor Relationships Created")

        # ---------------------------------------------------
        # Movie -> Director
        # ---------------------------------------------------

        director_relationships = [

            ("Inception", "Christopher Nolan"),

            ("Interstellar", "Christopher Nolan"),

            ("Titanic", "James Cameron"),

            ("3 Idiots", "Rajkumar Hirani")

        ]

        for movie, director in director_relationships:

            session.run("""

            MATCH (m:Movie {title:$movie})

            MATCH (d:Director {name:$director})

            CREATE (m)-[:DIRECTED_BY]->(d)

            """,

            movie=movie,
            director=director
            )

        print("Movie-Director Relationships Created")

        # ---------------------------------------------------
        # User -> Movie
        # ---------------------------------------------------

        likes = [

            ("Aravind", "Interstellar"),

            ("Rahul", "Titanic"),

            ("John", "3 Idiots")

        ]

        for user, movie in likes:

            session.run("""

            MATCH (u:User {name:$user})

            MATCH (m:Movie {title:$movie})

            CREATE (u)-[:LIKES]->(m)

            """,

            user=user,
            movie=movie
            )

        print("User Likes Created")

        print("\n===================================")
        print("Database Seeded Successfully")
        print("===================================\n")


if __name__ == "__main__":
    seed_database()