import webvtt

def parse_vtt_file(file):
    """
    Parses a .vtt file and extracts meaningful text content.

    Args:
        file: Uploaded .vtt file.

    Returns:
        str: Combined text content from the .vtt file.
    """
    content = []
    for caption in webvtt.read_buffer(file):
        content.append(caption.text)
    return " ".join(content)