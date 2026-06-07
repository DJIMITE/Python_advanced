import os

directory = "../"

file =  {}

for element in os.listdir(directory):
    f = os.path.join(directory, element)

    if os.path.isfile(f):
        ext = element.split(".")[-1]
        if ext not in file:
            file[ext] = []
        file[ext].append(element)
    else:
        for el in os.listdir(f):
            files = os.path.join(f, el)
            if os.path.isfile(files):
                ext_01 = el.split(".")[-1]
                if ext_01 not in file:
                    file[ext_01] = []
                file[ext_01].append(el)

with open(os.path.join(directory, "report.txt"), "w") as output_File:
    for ext, lines in sorted(file.items()):
        output_File.write(f"{ext}\n")
        for line in sorted(lines):
            output_File.write(f"- - - {line}\n")