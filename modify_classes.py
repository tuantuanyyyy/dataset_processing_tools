import os

# 指定标签文件所在的目录
labels_dir = r'C:\Users\86187\Desktop\1'

# 遍历目录下的所有文件
for filename in os.listdir(labels_dir):
    if filename.endswith('.txt'):
        file_path = os.path.join(labels_dir, filename)

        # 读取文件内容
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # 修改行内容
        modified_lines = []
        for line in lines:
            parts = line.split()
            if parts:
                # 将1改为0，将2改为1
                if parts[0] == '1':
                    parts[0] = '0'
                elif parts[0] == '0':
                    parts[0] = '1'
            modified_lines.append(' '.join(parts))

        # 将修改后的内容写回文件
        with open(file_path, 'w') as file:
            file.write('\n'.join(modified_lines) + '\n')

print("标签修改完成！")