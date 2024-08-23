import re


def extract_markdown_images(text):
    matches_alt = list(map(lambda x: x.strip("![]"), re.findall(r"(\!\[\w.*?\])", text)))
    matches_link = list(map(lambda x: x.strip("()"), re.findall(r"(\(.*?\))", text)))
    
    zipped = list(zip(matches_alt, matches_link))
    return zipped

def extract_markdown_links(text):
    matches_anchor = list(map(lambda x: x.strip('[]'), re.findall(r"(\[\w.*?\])", text)))
    matches_link = list(map(lambda x: x.strip("()"), re.findall(r"(\(.*?\))", text)))

    zipped = list(zip(matches_anchor,matches_link))
    return zipped
