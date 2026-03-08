from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
    
def block_to_block_type(block):
    lines = block.split("\n")
    
    # Check for heading (1-6 # followed by space)
    if re.match(r"^#{1,6} ", lines[0]):
        return BlockType.HEADING
    
    # Check for code block (starts and ends with ```)
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    
    # Check for quote block (all lines start with >)
    if all(re.match(r"^> ?", line) for line in lines):
        return BlockType.QUOTE
    
    # Check for unordered list (all lines start with - )
    if all(re.match(r"^- ", line) for line in lines):
        return BlockType.UNORDERED_LIST
    
    # Check for ordered list (lines start with 1., 2., etc. incrementing)
    if all(re.match(r"^\d+\. ", line) for line in lines):
        is_ordered = True
        for i, line in enumerate(lines):
            match = re.match(r"^(\d+)\. ", line)
            if not match or int(match.group(1)) != i + 1:
                is_ordered = False
                break
        if is_ordered:
            return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH