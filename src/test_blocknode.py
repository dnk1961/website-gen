import unittest
from blocknode import BlockType, block_to_block_type

class TestBlockNode(unittest.TestCase):
    def test_heading_type(self):
        node = "## Dylan is the best"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.HEADING)
    
    def test_code_type(self):
        node = "```\n this is the best```"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.CODE)

    def test_quote_type(self):
        node = ">This is the best" \
        ">Jenn is the best" \
        ">Dylan is the best"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.QUOTE)

    def test_quote_type(self):
        node = ">This is the best \nJenn is the best \n>Dylan is the best"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_unordered_list(self):
        node = "- Dylan\n- Jenn\n- Riku"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.UNORDERED_LIST)
    
    def test_ordered_list(self):
        node = "1. Dylan\n2. Jenn\n3. Riku"
        result = block_to_block_type(node)
        self.assertEqual(result, BlockType.ORDERED_LIST)
        
if __name__ == '__main__':
    unittest.main()