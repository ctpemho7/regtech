import xml.etree.ElementTree as ET
from typing import TypeVar
from abc import ABC, abstractmethod


class IXMLElement(ABC):
    """Общий интерфейс для описания всех XML элементов"""
    
    @abstractmethod
    def to_xml(self) -> ET.Element:
        pass

    
    def __str__(self) -> str:
        """
        Красиво выводит XML элемент используя xml.dom.minidom
        
        Args:
            element: Элемент, реализующий интерфейс IXMLElement
        """
        import xml.dom.minidom
        
        xml_elem = self.to_xml()
        
        # Конвертируем Element в строку и парсим через minidom
        rough_string = ET.tostring(xml_elem, 'utf-8')
        reparsed = xml.dom.minidom.parseString(rough_string)
        pretty_xml = reparsed.toprettyxml(indent="  ")
        
        # Убираем лишние пустые строки
        lines = pretty_xml.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        return '\n'.join(non_empty_lines)


    def save(self, filename, extension="xml"):
        with open(f"{filename}.{extension}", "w+", encoding="utf-8") as file:
            file.write(str(self))

XMLElementType = TypeVar('XMLElementType', bound=IXMLElement)
