import os
import shutil


DOWNLOADS_DIR = '/path/to/your/downloads' 
ORGANIZED_DIR = os.path.join(DOWNLOADS_DIR, 'Organized')


file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx'],
    'sheets': ['.xls', '.xlsx', '.csv'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

def organize_files():
    if not os.path.exists(ORGANIZED_DIR):
        os.makedirs(ORGANIZED_DIR)

    for filename in os.listdir(DOWNLOADS_DIR):
        file_path = os.path.join(DOWNLOADS_DIR, filename)

        if os.path.isdir(file_path):
            continue

        moved = False
        for category, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                category_dir = os.path.join(ORGANIZED_DIR, category)
                if not os.path.exists(category_dir):
                    os.makedirs(category_dir)
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f'Moved: {filename} to {category}')
                moved = True
                break

        if not moved:
            others_dir = os.path.join(ORGANIZED_DIR, 'Others')
            if not os.path.exists(others_dir):
                os.makedirs(others_dir)
            shutil.move(file_path, os.path.join(others_dir, filename))
            print(f'Moved: {filename} to Others')

if __name__ == '__main__':
    organize_files()