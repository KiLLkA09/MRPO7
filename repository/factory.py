from repository.sqlalchemy_repository import SQLAlchemyRepository
from repository.json_repository import JSONRepository
from repository.xml_repository import XMLRepository
from models import Buyer, Car
from database import SessionLocal

class RepositoryFactory:
    @staticmethod
    def create_repository(repository_type: str, entity_type: str):
        if repository_type == "sqlalchemy":
            if entity_type == "buyer":
                return SQLAlchemyRepository(SessionLocal(), Buyer)
            elif entity_type == "car":
                return SQLAlchemyRepository(SessionLocal(), Car)
        elif repository_type == "json":
            if entity_type == "buyer":
                return JSONRepository("buyers.json")
            elif entity_type == "car":
                return JSONRepository("cars.json")
        elif repository_type == "xml":
            if entity_type == "buyer":
                return XMLRepository("buyers.xml")
            elif entity_type == "car":
                return XMLRepository("cars.xml")
        else:
            raise ValueError(f"Unknown repository type: {repository_type}")
