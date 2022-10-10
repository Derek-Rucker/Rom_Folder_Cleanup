from enum import Enum
import os
from shutil import move

class Regions(Enum):
    USA = "USA"
    JAPAN = "JAPAN"
    EUROPE = "EUROPE"
    WORLD = "WORLD"

def traverse_files(dir_path, usa_path, world_path, japan_path, europe_path, other_path, dup_path):
    existing_titles = {}
    files = os.scandir(dir_path)
    for file in files:        
        if file.name.find('[BIOS]') > -1:
            continue
        open_paren = file.name.find('(')
        close_paren = file.name.find(')') + 1
        region = file.name[open_paren:close_paren]
        title = file.name[0: open_paren]        
        combined_title = "".join([title, region])
        if combined_title in existing_titles:
            move(file.path, dup_path)
            continue
        else:
            existing_titles[combined_title] = True
        if open_paren == -1:
            continue
        if region.upper().find(Regions.USA.value) > 0:
            move(file.path, usa_path)
        elif region.upper().find(Regions.WORLD.value) > 0:
            move(file.path, world_path)
        elif region.upper().find(Regions.JAPAN.value) > 0:
            move(file.path, japan_path)
        elif region.upper().find(Regions.EUROPE.value) > 0:
            move(file.path, europe_path)
        else:
            move (file.path, other_path)


def create_directories(paths):
    for i in range(len(paths)):
        if not os.path.exists(paths[i]):
            try:
                os.mkdir(paths[i])
                print(f'{paths[i]} created')
            except Exception as e:
                print(f'There was an error of: {str(e)}')        
    return


def main():
    dir_path = input('Please enter a directory: ')
    japan_path = os.path.join(dir_path, 'Japan')
    europe_path = os.path.join(dir_path, 'Europe')
    usa_path = os.path.join(dir_path, 'USA')
    world_path = os.path.join(dir_path, 'World')
    other_path = os.path.join(dir_path, 'Other')
    dup_path = os.path.join(dir_path, 'Duplicates')
    
    paths = [japan_path, europe_path, usa_path, other_path, world_path, dup_path]

    if os.path.exists(dir_path):
        create_directories(paths)
        traverse_files(dir_path, usa_path, world_path, japan_path, europe_path, other_path, dup_path)
        print('Cleanup finished.')
    else:
        print('Invalid path. Try again.')


if __name__ == '__main__':
    main()
