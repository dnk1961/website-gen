import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a text node", TextType.ITALICS)
        node2 = TextNode("This is a text node", TextType.ITALICS, "www.google.com")
        self.assertNotEqual(node, node2)
    
    def test_noteq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALICS)
        self.assertNotEqual(node, node2)
    

if __name__ == "__main__":
    unittest.main()
