def markdown_to_blocks(markdown):
    if not isinstance(markdown, str) or not markdown:
        raise ValueError("Markdown argument must be a non-empty string")
    block_strings = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        if not block:
            continue
        block_strings.append(block.strip())
    return block_strings