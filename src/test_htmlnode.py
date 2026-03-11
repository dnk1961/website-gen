import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("p", "Hello this is the props_to_html test", None , {"href":"https://www.google.com",  "target":"_blank"})
        expected_output = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_output)
    
    def test_repr(self):
        node = HTMLNode("p", "Hello this is the repr test", None,{"href":"https://www.google.com","target":"_blank"})
        expected_output = """HTMLNode(p, Hello this is the repr test, None, {'href': 'https://www.google.com', 'target': '_blank'})"""
        self.assertEqual(node.__repr__(), expected_output)

if __name__ == "__main__":
    unittest.main()