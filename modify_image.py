#!/usr/bin/env python
# coding=utf-8
 
from PIL import Image
import os
import sys

def modify_image(image_path , image_name):
	origin = Image.open(image_path)


	height = origin.size[1]
	width_modified = int(height * 1.675) 

	canvas = Image.new(mode='RGBA', size=(width_modified, height))



	canvas.paste(origin,(int((width_modified-height)/2) ,0))

	modified_dir = "images_modified"
    # 创建存储的文件夹
	if not os.path.exists(modified_dir):
		# 如果不存在则创建目录
		os.makedirs(modified_dir) 

	#canvas.show()  # 直接显示图片
	canvas.save(modified_dir + "/" + image_name, 'PNG')  # 保存在当前路径下，格式为PNG
	canvas.close()



if __name__ == "__main__":
	# 接收参数作为文件夹名
	rootdir = sys.argv[1]
	list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
	for i in range(0, len(list)):
		file_path = os.path.join(rootdir, list[i])
		modify_image(file_path , list[i])