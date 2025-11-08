import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import TypeVar
from abc import ABC, abstractmethod


class IXMLElement(ABC):
    """Общий интерфейс для описания всех XML элементов"""
    
    @abstractmethod
    def to_xml(self) -> ET.Element:
        pass

def pretty_print_xml_minidom(element: IXMLElement) -> None:
    """
    Красиво выводит XML элемент используя xml.dom.minidom
    
    Args:
        element: Элемент, реализующий интерфейс IXMLElement
    """
    import xml.dom.minidom
    
    xml_elem = element.to_xml()
    
    # Конвертируем Element в строку и парсим через minidom
    rough_string = ET.tostring(xml_elem, 'utf-8')
    reparsed = xml.dom.minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")
    
    # Убираем лишние пустые строки
    lines = pretty_xml.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    print('\n'.join(non_empty_lines))


XMLElementType = TypeVar('XMLElementType', bound=IXMLElement)


class DocBody(IXMLElement):
    """Класс для описания DocBody"""
    def __init__(self, content: IXMLElement = None):
        self.content = content

    def to_xml(self) -> ET.Element:
        """Преобразовать объект в XML элемент"""
        doc_body_elem = ET.Element('DocBody')
        if self.content:
            content_elem = self.content.to_xml()
            doc_body_elem.append(content_elem)
        return doc_body_elem


class EDContainer(IXMLElement):
    def __init__(self, document_mode_id="1006058E", document_id=None):
        self.document_mode_id = document_mode_id
        self.document_id = document_id
        # согласно XML у нас три элемента
        self.ESADout_CU: DocBody = None
        self.DTSout_CU: DocBody = None
        self.GTDoutCustomsMark: DocBody = None

    def to_xml(self) -> ET.Element:
        """Преобразовать объект в XML элемент"""
        # Создаем корневой элемент
        root = ET.Element('EDContainer')
        
        # Добавляем атрибут DocumentModeID
        root.set('DocumentModeID', self.document_mode_id)
        
        # Добавляем document_id если он есть
        if self.document_id:
            root.append(self.document_id.to_xml())
        
        # Добавляем дочерние элементы если они заданы
        if self.ESADout_CU:
            esad_elem = self.ESADout_CU.to_xml()
            root.append(esad_elem)
            
        if self.DTSout_CU:
            dts_elem = self.DTSout_CU.to_xml()
            root.append(dts_elem)
            
        if self.GTDoutCustomsMark:
            gtd_elem = self.GTDoutCustomsMark.to_xml()
            root.append(gtd_elem)
            
        return root

