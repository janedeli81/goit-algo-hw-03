import os
import shutil
import sys

def copy_files(source_dir, destination_dir="dist"):
    """
    Копіює файли з вихідної директорії до директорії призначення, сортуючи їх у піддиректорії за розширенням.
    """
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            try:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1][1:] # Видаляємо крапку з розширення
                if file_extension == "": # Якщо файл не має розширення, використовуємо спеціальну піддиректорію
                    file_extension = "no_extension"
                destination_folder = os.path.join(destination_dir, file_extension)
                os.makedirs(destination_folder, exist_ok=True)
                shutil.copy(file_path, destination_folder)
            except Exception as e:
                print(f"Помилка при копіюванні файлу {file}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Будь ласка, вкажіть шлях до вихідної директорії.")
        sys.exit(1)
    source_directory = sys.argv[1]
    destination_directory = sys.argv[2] if len(sys.argv) > 2 else "dist"
    copy_files(source_directory, destination_directory)
