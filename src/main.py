from textnode import *
from blocknode import *
from inline_markdown import *
from htmlnode import *

def markdown_to_html_node(markdown):
    list_of_html_nodes = []
    list_of_string_blocks = markdown_to_blocks(markdown)

    for string_block in list_of_string_blocks:
        #Determine block type
        ##print(f"String Block: {string_block}")
        block_type = block_to_block_type(string_block)
        ##print(f"Block Type: {block_type}")
        #HEADING Case
        if block_type == BlockType.HEADING:
            level = 0
            while string_block[level] == '#':
                level += 1
            block_text = string_block[level+1:]
            formatted_string = format_string(block_text)
            children = text_to_children(formatted_string)
            list_of_html_nodes.append(ParentNode(f"h{level}", children))
        if block_type == BlockType.QUOTE:
            formatted_string = format_string(block_text, "<")
            children = text_to_children(formatted_string)
            list_of_html_nodes.append(ParentNode(f"blockquote", children))
        if block_type == BlockType.UNORDERED_LIST:
            children = format_ordered_string(string_block)
            list_of_html_nodes.append(ParentNode("ul", children))
        if block_type == BlockType.ORDERED_LIST: 
            children = format_ordered_string(string_block)
            list_of_html_nodes.append(ParentNode("ol", children))
        if block_type == BlockType.CODE:
            code_content = string_block.split('\n')
            lines = []
            for content in code_content:
                lines.append(content.lstrip())
            code_content2 = '\n'.join(lines[1:-1])
            code_TextNode = TextNode(code_content2+"\n", TextType.CODE)
            code_HTMLNode = text_node_to_html_node(code_TextNode)
            code_parentNode = ParentNode("pre",[code_HTMLNode])
            list_of_html_nodes.append(code_parentNode)
        if block_type == BlockType.PARAGRAPH:
            formatted_string = format_string(string_block)
            children = text_to_children(formatted_string)
            list_of_html_nodes.append(ParentNode("p",children))                                       
    return ParentNode("div", list_of_html_nodes)

def text_to_children(text):
    result = []
    list_of_textnodes = text_to_textnodes(text)
    for textnode in list_of_textnodes:
        result.append(text_node_to_html_node(textnode))
    return result

def format_string(string_block, prefix=""):
    stripped_lines = []
    lines = string_block.split("\n")
    for line in lines:
        stripped_lines.append(line[len(prefix):].strip())
    return " ".join(stripped_lines)

def format_ordered_string(string_block):
    list_of_items1 = string_block.split("\n")
    children = []
    for item in list_of_items1:
        grandchild = text_to_children(item[2:])
        children.append(ParentNode("li", grandchild))
    return children

def main():
    pass

if __name__ == "__main__":
    main()
