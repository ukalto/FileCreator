import os

path = 'Files'


def create():
    if not os.path.exists(path):
        os.mkdir(path)
    file_format = input("File-format: ")
    while True:
        filename = input("Filename: ") + "." + file_format
        text = input(f"Text to create {filename}.{file_format} file: ")
        file1 = open(os.path.join(path, filename), "w")
        file1.write(text)
        file1.close()
        if len(input("Want to continue?")) == 0:
            break


if __name__ == '__main__':
    create()
