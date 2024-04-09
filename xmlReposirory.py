from BaseRepository import BaseRepository
from lxml import etree as ET
import os


class XMLRepository(BaseRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None

    def create_or_open_xml(self):
        if not os.path.exists(self.file_path):
            root = ET.Element("root")
            self.tree = ET.ElementTree(root)
            with open(self.file_path, 'wb') as f:
                self.tree.write(f, xml_declaration=True, encoding='utf-8', pretty_print=True)
        else:
            self.tree = ET.parse(self.file_path)

        return self.tree.getroot(), self.tree

    def check_or_create_class_directory(self, root, class_name):
        class_dir = root.find(class_name)
        if class_dir is None:
            class_dir = ET.SubElement(root, class_name)
        return class_dir

    def check_or_create_instance_directory(self, class_dir, obj_id):
        instance_dir = class_dir.find(f"instance[@id='{obj_id}']")
        if instance_dir is None:
            instance_dir = ET.SubElement(class_dir, "instance", id=str(obj_id))
        return instance_dir

    def write_data_to_class_directory(self, root, obj):
        class_name = obj.__class__.__name__
        class_dir = self.check_or_create_class_directory(root, class_name)
        obj_id = obj.id
        instance_dir = self.check_or_create_instance_directory(class_dir, obj_id)

        for key, value in obj.__dict__.items():
            if not key.startswith('_'):  # Пропускаем приватные атрибуты
                prop_element = ET.SubElement(instance_dir, key)
                prop_element.text = str(value)

    def save(self, obj):
        root, _ = self.create_or_open_xml()  # Используем только корневой элемент
        self.write_data_to_class_directory(root, obj)

        # Перезаписываем весь XML-документ с новыми данными
        with open(self.file_path, 'wb') as f:
            self.tree.write(f, xml_declaration=True, encoding='utf-8', pretty_print=True)

        self.ppxml('base.xml')

    def ppxml(self, xml):
        parser = ET.XMLParser(remove_blank_text=True)
        tree = ET.parse(xml, parser)
        tree.write(xml, encoding='utf-8', pretty_print=True, xml_declaration=True)

    def find(self, **kwargs):
        pass