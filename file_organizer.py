import os
import shutil

# Define file type folders
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Code": [".py", ".js", ".html", ".css", ".php"],
    "Media": [".mp3", ".mp4", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
    "Others": []
}

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        print("Path does not exist.")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            moved = False
            for category, extensions in file_types.items():
                if ext.lower() in extensions:
                    category_path = os.path.join(folder_path, category)
                    os.makedirs(category_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_path, file))
                    moved = True
                    break
            if not moved:
                others_path = os.path.join(folder_path, "Others")
                os.makedirs(others_path, exist_ok=True)
                shutil.move(file_path, os.path.join(others_path, file))
    print("Files organized successfully!")

# Example usage
if __name__ == "__main__":
    path = input("Enter the folder path to organize: ")
    organize_files(path)
