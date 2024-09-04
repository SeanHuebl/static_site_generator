import re


def extract_markdown_images(text):
    """
    Parses a markdown document to find matches for image syntax patterns and extracts the alt text and URL.

    This function searches for patterns in the format of `![alt text](url)` in the provided string,
    then strips the characters `!`, `[`, `]`, `(`, and `)` from each match to extract the alt text and URL.

    Args:
        text (str): The markdown document, as a single string, to be parsed.
    
    Returns:
        list of tuple: A list where each tuple contains two elements:
            - alt text (str): The alt text from the matched pattern.
            - url (str): The URL from the matched pattern.
    """

    # Use regex to find all occurrences of image syntax `![alt text](url)` in the input text
    # This pattern captures any text inside the square brackets and parentheses
    matches = re.findall(r"!\[.*?\]\(.*?\)", text)

    # If no matches are found, return an empty list to indicate no images were detected
    if not matches:
        return []

    # For each match, split it into the alt text and URL components using regex
    # This step isolates the `![alt text]` part from the `(url)` part
    split_matches = [re.findall(r"!\[.*?\]|\(.*?\)", match) for match in matches]

    # Clean up each component by stripping unnecessary characters (`!`, `[`, `]`, `(`, `)`)
    # and return a list of tuples containing the alt text and URL
    final_matches = [tuple(component.strip('![]()') for component in match) for match in split_matches]

    return final_matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[\w.*?\]\(.*?\)", text)
    if not matches:
        return
    split_matches = list(map(lambda x: re.findall(r"\[\w.*?\]|\(.*?\)", x), matches))
    
    final_matches = list((map(lambda inner_list: tuple(map(lambda x: x.strip('[]()'), inner_list)), split_matches)))
    
    return final_matches
    
