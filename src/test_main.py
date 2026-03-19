from textnode import *
from blocknode import *
from inline_markdown import *
from htmlnode import *
from main import *
import unittest

class TestMain(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """## This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is <b>bolded</b> paragraph text in a p tag here</h2><p>This is another paragraph with <i>italic</i> text here</p></div>"
        )
    def test_unordered_list(self):
        md = """- This is **bolded** paragraph
- text in a p
- tag here

This is another paragraph with _italic_ text here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ul><p>This is another paragraph with <i>italic</i> text here</p></div>"
        )

    def test_ordered_list(self):
        md = """- This is **bolded** paragraph
- text in a p
- tag here

This is another paragraph with _italic_ text here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is <b>bolded</b> paragraph</li><li>text in a p</li><li>tag here</li></ul><p>This is another paragraph with <i>italic</i> text here</p></div>"
        )



if __name__ == '__main__':
    unittest.main()