#!/usr/bin/python3
"""Serialize and Deserialize using XML as an alternative to JSON"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    with open(filename, 'wb') as file:
        tree.write(file)


def deserialize_from_xml(filename):
    """Deserialize an XML file to a dictionary"""
    tree = ET.ElementTree(file=filename)
    root = tree.getroot()

    dictionary = {}
    for element in root:
        dictionary[element.tag] = element.text

    return dictionary

