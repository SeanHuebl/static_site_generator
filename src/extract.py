import re


def extract_markdown_images(text):
    matches = re.findall(r"(\!\[\w.*?\]|(\(.*?\)))", text)
    if not matches:
        return
    
    split_matches = re.findall(r"\!\[\w.*?\]|\(.*?\)", matches[0])
    
    final_matches = list(map(lambda x :x.strip('![]()'), split_matches))
    return final_matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!\!)\[\w.*?\]\(.*?\)", text)
    if not matches:
        return
    split_matches = list(map(lambda x: re.findall(r"\[\w.*?\]|\(.*?\)", x), matches))
    
    final_matches = list((map(lambda inner_list: tuple(map(lambda x: x.strip('[]()'), inner_list)), split_matches)))
    
    return final_matches
    
