import os

def add_prefix_to_files(folder_path, prefix, file_extension=None):
    """
    批量给指定目录下的文件添加前缀
    """
    try:
        if not os.path.isdir(folder_path):
            print("错误：指定的路径不是有效的文件夹！")
            return

        for filename in os.listdir(folder_path):
            old_path = os.path.join(folder_path, filename)

            if os.path.isfile(old_path):
                if file_extension is None or filename.endswith(file_extension):
                    new_filename = prefix + filename
                    new_path = os.path.join(folder_path, new_filename)

                    os.rename(old_path, new_path)
                    print(f"重命名成功: {filename} → {new_filename}")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    folder_path = "/Users/llwh/Desktop/Contract"  # 直接写死文件夹路径
    prefix = input("请输入要添加的前缀: ").strip()
    file_extension = input("请输入要处理的文件类型（例如.txt），不输入则处理所有文件: ").strip()

    if file_extension == "":
        file_extension = None

    add_prefix_to_files(folder_path, prefix, file_extension)
