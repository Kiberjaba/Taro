from PIL import Image
import os

def convert_jpg_to_png(directory):
    # Получаем список всех файлов в директории
    files = os.listdir(directory)
    # Фильтруем только файлы с расширением .jpg
    jpg_files = [f for f in files if f.lower().endswith('.jpg')]

    # Проходимся по каждому JPG-изображению
    for jpg_file in jpg_files:
        jpg_path = os.path.join(directory, jpg_file)
        # Открываем изображение с помощью Pillow
        with Image.open(jpg_path) as img:
            # Изменяем формат на PNG
            png_path = os.path.splitext(jpg_path)[0] + ".png"
            # Сохраняем изображение в новом формате
            img.save(png_path, "PNG")
            print(f"Converted {jpg_path} to {png_path}")

# Укажите путь к директории с JPG-изображениями
jpg_directory = 'images'
convert_jpg_to_png(jpg_directory)
