from src.blocktype import BlockType, block_to_block_type
import unittest

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```code```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> Quote"), BlockType.QUOTE)
        self.assertEqual(block_to_block_type("- List item"), BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type("1. Ordered item"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("Just a paragraph."), BlockType.PARAGRAPH)