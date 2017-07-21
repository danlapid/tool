import os
import zipfile

srcs_folder = "src"
packages = ["google"]
srcs = [
    "__init__.py",
    "__main__.py",
    "tool/__init__.py",
    "tool/main.py",
    "tool/messages/__init__.py",
    "tool/messages/messages_pb2.py"
]


def add_files(zip_file, files):
    """
    :param zip: open zip file
    :param files: list of file paths
    :return: None
    """
    for file_path in files:
        file_path = os.path.join(srcs_folder, file_path)
        zip_file.write(file_path, file_path.lstrip(srcs_folder))


def add_packages(zip_file, folders):
    for package in folders:
        for root, dirs, files in os.walk(os.path.join(srcs_folder, package)):
            for f in files:
                file_path = os.path.join(root, f)
                zip_file.write(file_path, file_path.lstrip(srcs_folder))


if __name__ == '__main__':
    try:
        os.mkdir(r"bin")
    except:
        pass
    try:
        os.mkdir(r"bin\tool")
    except:
        pass
    zip_file = zipfile.ZipFile(r'bin\tool\tool.py', 'w')
    add_packages(zip_file, packages)
    add_files(zip_file, srcs)
    zip_file.close()
