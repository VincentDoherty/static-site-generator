def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = []

    for block in blocks:
        lines = block.split("\n")
        stripped_lines = [line.strip() for line in lines]
        cleaned_block = "\n".join(stripped_lines).strip()

        if cleaned_block:
            cleaned_blocks.append(cleaned_block)

    return cleaned_blocks