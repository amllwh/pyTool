import os

def remove_prefix_from_files(folder_path, prefix, file_extension=None):
    """
    批量去掉指定目录下文件名的前缀
    :param folder_path: 文件夹路径
    :param prefix: 要去掉的前缀
    :param file_extension: 可选，指定只处理某种类型的文件（如'.txt'）
    """
    try:
        if not os.path.isdir(folder_path):
            print("错误：指定的路径不是有效的文件夹！")
            return

        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)

            if os.path.isfile(old_path):
                if file_extension is None or filename.endswith(file_extension):
                    # 判断文件名是不是以这个前缀开头
                    if filename.startswith(prefix):
                        new_filename = filename[len(prefix):]  # 删掉前缀
                        new_path = os.path.join(folder_path, new_filename)

                        os.rename(old_path, new_path)
                        print(f"重命名成功: {filename} → {new_filename}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    folder_path = "/Users/llwh/Desktop/Contract"  # 文件夹路径
    prefix = input("请输入要删除的前缀: ").strip()
    file_extension = input("请输入要处理的文件类型（例如.txt），不输入则处理所有文件: ").strip()

    if file_extension == "":
        file_extension = None

    remove_prefix_from_files(folder_path, prefix, file_extension)
