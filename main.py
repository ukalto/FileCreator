import os

path = 'Files'


def create():
    if not os.path.exists(path):
        os.mkdir(path)
    while True:
        filename = input("Filename: ") + ".txt"
        text = input(f"Text to create SQL {filename} file: ")
        file1 = open(os.path.join(path, filename), "w")
        file1.write(text)
        file1.close()
        if len(input("Want to continue?")) == 0:
            break


if __name__ == '__main__':
    create()
