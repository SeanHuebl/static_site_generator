import os

from enums import TextType
from textnode import TextNode

def copy_all_contents(source, destination):
    if not os.path.exists(source) or not os.path.exists(destination):
        raise ValueError('Check source and destination paths for errors and make sure the paths exist.')
    return remove_destination_dir_contents(destination)
            
def remove_destination_dir_contents(destination_dir):
    if os.path.isfile(destination_dir):
        print(destination_dir)
    contents = os.listdir(destination_dir)
    
    for content in contents:
        path = os.path.join(destination_dir, content)
        if os.path.isdir(path):
            remove_destination_dir_contents(path)

        

def main():
    print(copy_all_contents('./static', './public'))



if __name__ == "__main__":
    main()