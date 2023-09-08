import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        rawdata = file.read()
        result = chardet.detect(rawdata)
        return result['encoding']

def modify_image_paths(file_path, new_path):
    try:
        encoding = detect_encoding(file_path)
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()

        # 替换 "../../../xxxxx" md图片的路径
        modified_content = content.replace("![img](../../../xxx", f"![img]({new_path}/xxxx")

        # 替换 "../../../xxxxx" md图片的路径
        modified_content = modified_content.replace("![img](../../../xxxx", f"![img]({new_path}/xxxx")

        with open(file_path, 'w', encoding=encoding) as file:
            file.write(modified_content)

        print(f"成功修改文件: {file_path}")
    except Exception as e:
        print(f"修改文件时出现错误: {file_path}")
        print(f"错误信息: {str(e)}")

# 指定md文件所在的目录
directory = 'xxxxx'

# 指定新的图片路径
new_image_path = 'xxxx'

# 遍历目录下的所有md文件
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            modify_image_paths(file_path, new_image_path)
