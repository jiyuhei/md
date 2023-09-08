md.py
脚本中修改
![image](https://github.com/jiyuhei/md/assets/143597936/376775b5-3641-4cbb-b68d-266727664a82)
例如路径：![img](/Users/mac/Downloads/img/1.png)

modified_content = content.replace("![img](../../../xxx", f"![img]({new_path}/xxxx")xxx修改成图片中的路径，修改后的如下：

content.replace("![img](/Users/mac/Downloads/img", f"![img]({new_path}/img")

![image](https://github.com/jiyuhei/md/assets/143597936/1c44e504-c9ff-43ac-b4a0-89f57df58c7f)

指定图片路径就是你迁移后的目录

例如：（你迁移到/Users/mac/‍但是后缀img没有变化）

![image](https://github.com/jiyuhei/md/assets/143597936/cd559084-36c4-4ed3-aac0-79fda71420ec)

指定新的路径
new_image_path = 'xxxx'可以修改成如下格式

new_image_path = '/Users/mac/'

脚本完成后的情况
![image](https://github.com/jiyuhei/md/assets/143597936/cabe6daf-4198-49c0-97d7-008cd49e1e8d)

md2.py
作用是把md文件中对应的图片，复制图片在同文件目录下image下，并把md文件中的路径同步修改成新的图片路径。
