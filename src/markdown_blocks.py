from textnode import *
from blocknode import *
from inline_markdown import *
from htmlnode import *
import textwrap

def markdown_to_html_node(markdown):
    html_nodes = []
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    
    return ParentNode("div", html_nodes) 

def block_to_html_node(block): 
    block_type = block_to_block_type(block)
    if block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDERED_LIST:
        return ul_to_html_node(block)
    elif block_type == BlockType.ORDERED_LIST:
        return ol_to_html_node(block)

def code_to_html_node(block):
    code_content = "\n".join(block.split("\n")[1:-1])
    code_content = textwrap.dedent(code_content) + '\n'
    code_text_node = TextNode(code_content, TextType.CODE)
    code_html_node = text_node_to_html_node(code_text_node)
    return ParentNode("pre",[code_html_node])

def quote_to_html_node(block):
    formatted_string = format_string(block, "<")
    children = text_to_children(formatted_string)
    return ParentNode("blockquote", children)

def ol_to_html_node(block):
    children = list_block_to_children(block, 3)
    return ParentNode("ol", children)

def ul_to_html_node(block):
    children = list_block_to_children(block, 2)
    return ParentNode("ul", children)

def heading_to_html_node(block):
    level = 0
    while block[level] == '#':
        level += 1
    block_text = block[level+1:]
    formatted_string = format_string(block_text)
    children = text_to_children(formatted_string)
    return ParentNode(f"h{level}", children)

def paragraph_to_html_node(block):
    formatted_string = format_string(block)
    children = text_to_children(formatted_string)
    return ParentNode("p",children)   

def text_to_children(text):
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]

def format_string(string_block, prefix=""):
    stripped_lines = []
    lines = string_block.split("\n")
    for line in lines:
        stripped_lines.append(line[len(prefix):].strip())
    return " ".join(stripped_lines)

def list_block_to_children(string_block, prefix):
    items = string_block.split("\n")
    children = []
    for item in items:
        grandchild = text_to_children(item[prefix:])
        children.append(ParentNode("li", grandchild))
    return children