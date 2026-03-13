import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello this is the props_to_html test", None , {"href":"https://www.google.com",  "target":"_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)
    
    def test_repr(self):
        node = HTMLNode("p", "Hello this is the repr test", None,{"href":"https://www.google.com","target":"_blank"})
        expected_output = """HTMLNode(p, Hello this is the repr test, None, {'href': 'https://www.google.com', 'target': '_blank'})"""
        self.assertEqual(node.__repr__(), expected_output)
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(),'<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_rep(self):
        node = LeafNode("p", "Hello this is the repr test", {"href":"https://www.google.com","target":"_blank"})
        expected_output = """LeafNode(p, Hello this is the repr test, {'href': 'https://www.google.com', 'target': '_blank'})"""
        self.assertEqual(node.__repr__(), expected_output)  
        
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
    )

if __name__ == "__main__":
    unittest.main()