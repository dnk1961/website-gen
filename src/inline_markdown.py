from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        split_string = node.text.split(delimiter)
        if len(split_string) % 2 == 0:
            raise Exception(f"Invalid Markdown Syntax: {node.text}")
        substring_list = []
        for index in range(len(split_string)):
            if split_string[index] == "":
                continue
            if index % 2 == 0:
                new_node = TextNode(split_string[index], TextType.TEXT)
            else:
                new_node = TextNode(split_string[index], text_type)
            substring_list.append(new_node)
        result.extend(substring_list)
    return result

def extract_markdown_images(text: str) -> tuple:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text: str) -> tuple:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_images(old_nodes: list[TextNode]) -> list[TextNode]:
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        else:
            list_of_tuples = extract_markdown_images(node.text)
            if not list_of_tuples:
                result.append(node)
                continue
            else:
                remaining_text = node.text
                for image_alt, image_url in list_of_tuples:
                    sections = remaining_text.split(f"![{image_alt}]({image_url})",1)
                    if len(sections) != 2:
                        raise ValueError("invalid markdown, image section not closed")
                    if sections[0] != "":
                        result.append(TextNode(sections[0], TextType.TEXT))
                    result.append(TextNode(image_alt, TextType.IMAGE, image_url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    result.append(TextNode(remaining_text, TextType.TEXT))
    return result

def split_nodes_links(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
        else:
            list_of_tuples = extract_markdown_links(node.text)
            if not list_of_tuples:
                result.append(node)
                continue
            else:
                remaining_text = node.text
                for alt, url in list_of_tuples:
                    sections = remaining_text.split(f"[{alt}]({url})",1)
                    if sections[0] != "":
                        result.append(TextNode(sections[0], TextType.TEXT))
                    result.append(TextNode(alt, TextType.LINK, url))
                    remaining_text = sections[1]
                if remaining_text != "":
                    result.append(TextNode(remaining_text, TextType.TEXT))
    return result
    
def main():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_node = split_nodes_image([node])
    print(new_node)

if __name__ == '__main__':
    main()