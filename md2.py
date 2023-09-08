import os
import shutil
import re

def copy_and_update_images(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                if content.startswith('---') and '---' in content[3:]:
                    content = content.split('---', 2)[2].lstrip()
                images_dir = os.path.join(root, "images")
                os.makedirs(images_dir, exist_ok=True)
                image_paths = re.findall(r"!\[img\]\((.*?)\)", content)
                for image_path in image_paths:
                    old_image_path = os.path.join("图片路径自行修改", image_path)
                    if os.path.exists(old_image_path):
                        image_name = os.path.basename(image_path)
                        new_image_path = os.path.join(images_dir, image_name)
                        shutil.copy(old_image_path, new_image_path)
                        content = content.replace(image_path, "images/" + image_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)

# 指定md文件所在的目录
directory = 'xxxx'

copy_and_update_images(directory)
