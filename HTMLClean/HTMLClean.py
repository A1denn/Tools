import re

def remove_html_and_keep_chinese(file_path, output_path):
    # 读取文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # 替换 </br> 为换行符
    content = content.replace('</br>', '\n')

    # 使用正则表达式去除HTML标签
    content_without_tags = re.sub(r'<[^>]+>', '', content)

    # 保留汉字、中文标点和特殊符号
    chinese_content = re.sub(r'[^\u4e00-\u9fff，。、；：（）？！《》“”‘’「」\n]', '', content_without_tags)

    # 将清理后的内容写入新文件
    with open(output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(chinese_content)

# 输入和输出文件路径
input_file_path = 'd:/code/project/HTMLClean/input.txt'  # 替换为你的输入文件路径
output_file_path = 'd:/code/project/HTMLClean/result.txt'  # 替换为你想要的输出文件路径

# 运行函数
remove_html_and_keep_chinese(input_file_path, output_file_path)
