import os
import shutil

Image = []
Document = []
Video = []
Music = []
Unknown = []

dir_path = input("Enter the directory path: ")

class Utility:
    @staticmethod
    def Check_dir():
        if not os.path.exists(dir_path):
            print(f"Directory '{dir_path}' does not exist.")
            return
        files = os.listdir(dir_path)
        if not files:
            print(f"Directory '{dir_path}' is empty.")
            return 
        print("Organizing files in the directory...")

        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                Image.append(file)
            elif file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.txt'):
                Document.append(file)
            elif file.endswith('.mp4') or file.endswith('.mkv'):
                Video.append(file)
            elif file.endswith('.mp3') or file.endswith('.wav'):
                Music.append(file)
            else:
                Unknown.append(file)

    @staticmethod
    def put_files():
        # Create target folders if not exist
        folders = {
            "Images": Image,
            "Documents": Document,
            "Videos": Video,
            "Music": Music,
            "Others": Unknown
        }

        for folder, file_list in folders.items():
            folder_path = os.path.join(dir_path, folder)
            os.makedirs(folder_path, exist_ok=True)

            for file in file_list:
                source = os.path.join(dir_path, file)
                destination = os.path.join(folder_path, file)
                try:
                    shutil.move(source, destination)
                    print(f"Moved: {file} → {folder}/")
                except Exception as e:
                    print(f"Error moving {file}: {e}")


# Call the methods
Utility.Check_dir()
Utility.put_files()