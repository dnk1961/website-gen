from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    lines = block.split('\n')
    default = BlockType.PARAGRAPH
    heading_checker = ("# ", "## ", "### ", "#### ", "##### ", "###### ")
    if block.startswith(heading_checker):
        return BlockType.HEADING
    if block.startswith("```"):
        if lines[-1].endswith("```"):
            return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return default
        return BlockType.QUOTE
    if block.startswith("-"):
        for line in lines:
            if not line.startswith("- "):
                return default
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return default
            i += 1
        return BlockType.ORDERED_LIST
    return default