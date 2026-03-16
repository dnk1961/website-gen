import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_images, split_nodes_links

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
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_text(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        self.assertListEqual( [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)
        
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.COM/IMAGE.PNG)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_images([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://www.example.COM/IMAGE.PNG"),
            ],
            new_nodes,
        )
    def test_split_links(self):
        node = TextNode(
            "This is text with links to [boot.dev](https://boot.dev) and to [Youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_links([node])
        self.assertListEqual(
            [
                TextNode("This is text with links to ", TextType.TEXT),
                TextNode("boot.dev", TextType.LINK, "https://boot.dev"),
                TextNode(" and to ", TextType.TEXT),
                TextNode(
                    "Youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )
if __name__ == "__main__":
    unittest.main()