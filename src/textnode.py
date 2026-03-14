from enum import Enum
from htmlnode import LeafNode, HTMLNode

class TextType(Enum):
    TEXT  = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, text_url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = text_url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    text = text_node.text
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text, {"href":text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.value})
    else:
        raise ValueError(f"Text Type Unsupported: {text_node.text_type}")