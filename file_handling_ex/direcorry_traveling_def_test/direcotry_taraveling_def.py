import os

files = {}
def directory_taraveling(folder, level):

    if level == -1:
        return

    for element in os.listdir(folder):

        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = os.path.splitext(f)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(element)
        else:
            directory_taraveling(f, level - 1)


directory = "../"

directory_taraveling(directory, 1)


with open(os.path.join(directory, "files.txt"), "w") as output:
    for el, lines in sorted(files.items()):
        output.write(el + "\n")
        for line in sorted(lines):
            output.write(f"- - - {line}\n")