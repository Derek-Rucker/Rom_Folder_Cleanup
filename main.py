import os
from shutil import move

def menu():    
    dir_path = input('Please enter a directory: ')
    japan_path = os.path.join(dir_path, 'Japan')
    europe_path = os.path.join(dir_path, 'Europe')
    usa_path = os.path.join(dir_path, 'USA')
    world_path = os.path.join(dir_path, 'World')
    other_path = os.path.join(dir_path, 'Other')
    
    paths = [japan_path, europe_path, usa_path, other_path, world_path]

    if os.path.exists(dir_path):
        create_directories(paths)
        files = os.scandir(dir_path)
        for file in files:
            if file.name.find('[BIOS]') > -1:
                continue
            open_paren = file.name.find('(')
            if open_paren is -1:
                continue
            if file.name.find('USA', open_paren) > -1:
                move(file.path, usa_path)
            elif file.name.find('World', open_paren) > -1:
                move(file.path, world_path)
            elif file.name.find('Japan', open_paren) > -1:
                move(file.path, japan_path)
            elif file.name.find('Europe', open_paren) > -1:
                move(file.path, europe_path)
            else:
                move (file.path, other_path)
        print('Cleanup finished.')
    else:
        print('Invalid path. Try again.')


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
    menu()


if __name__ == '__main__':
    main()
