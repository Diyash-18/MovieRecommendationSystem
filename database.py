from neo4j import GraphDatabase
from config import URI, DB_USERNAME, DB_PASSWORD

driver = GraphDatabase.driver(
    URI,
    auth=(DB_USERNAME, DB_PASSWORD)
)