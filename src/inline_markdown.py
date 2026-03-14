from textnode import TextNode, TextType

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