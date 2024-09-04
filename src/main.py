import os
import shutil

from generate_page import generate_page

def copy_all_contents(source, destination):
    if not os.path.exists(source):
        raise ValueError('Check source path for errors and make sure the path exists.')
    if not os.path.exists(destination):
        os.mkdir(destination)
        copy_files(source, destination)
    else:    
        remove_destination_dir_contents(destination)
        copy_files(source, destination)
    print('Copy completed')

def copy_files(source, destination):
    contents = os.listdir(source)
    for content in contents:
        src_path = os.path.join(source, content)
        dest_path = os.path.join(destination, content)
        if os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_files(src_path, dest_path)
        elif os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)     
        
        else:
            raise ValueError("Path is not a file nor a directory")
            
def remove_destination_dir_contents(destination_dir):   

    contents = os.listdir(destination_dir)
    
    for content in contents:
        path = os.path.join(destination_dir, content)
        if os.path.isdir(path):
            remove_destination_dir_contents(path)
            os.rmdir(path)
        elif os.path.isfile(path):
            os.remove(path)
        else:
            raise ValueError("Path is not a file nor a directory")
    
        

def main():
    copy_all_contents('./static', './public')
    generate_page('./content/index.md', './template.html', './public/index.html')



if __name__ == "__main__":
    main()