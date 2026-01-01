import xml.etree.ElementTree as ET

SCRIPT_CLASSES = {
    "Script",
    "LocalScript",
    "ModuleScript",
}

def parse_rbxlx(path):
    tree = ET.parse(path)
    root = tree.getroot()

    items = []
    for item in root.findall("Item"):
        items.append(parse_item(item))

    return items


def parse_item(item):
    class_name = item.attrib.get("class")
    name = "Unnamed"
    source = ""

    props = item.find("Properties")
    if props is not None:
        for prop in props:
            prop_name = prop.attrib.get("name")
            if prop_name == "Name":
                name = prop.text or "Unnamed"
            elif prop_name == "Source":
                source = prop.text or ""

    children = []
    for child in item.findall("Item"):
        children.append(parse_item(child))

    return {
        "class": class_name,
        "name": sanitize(name),
        "source": source,
        "is_script": class_name in SCRIPT_CLASSES and source.strip() != "",
        "children": children,
    }


def sanitize(name):
    return name.replace("/", "_").replace("\\", "_")
