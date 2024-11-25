import xml.etree.ElementTree as ET
from repository.abstract_repository import AbstractRepository

class XMLRepository(AbstractRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            tree = ET.parse(self.file_path)
            root = tree.getroot()
            return self._parse_elements(root)
        except FileNotFoundError:
            return []

    def _parse_elements(self, root):
        entities = []
        for elem in root:
            entity = {}
            for child in elem:
                entity[child.tag] = child.text
            entities.append(entity)
        return entities

    def _save_data(self):
        root = ET.Element("entities")
        for entity in self.data:
            entity_elem = ET.SubElement(root, "entity")
            for key, value in entity.items():
                child_elem = ET.SubElement(entity_elem, key)
                child_elem.text = str(value)
        tree = ET.ElementTree(root)
        tree.write(self.file_path)

    def add(self, entity):
        entity_id = len(self.data) + 1
        entity["id"] = entity_id
        self.data.append(entity)
        self._save_data()

    def get_by_id(self, entity_id):
        return next((e for e in self.data if e["id"] == entity_id), None)

    def get_all(self):
        return self.data

    def delete(self, entity_id):
        self.data = [e for e in self.data if e["id"] != entity_id]
        self._save_data()

    def update(self, entity):
        for i, e in enumerate(self.data):
            if e["id"] == entity["id"]:
                self.data[i] = entity
                break
        self._save_data()
