import os

while True:
    command = input().split("-")

    if command[0] == "End":
        break

    if command[0] == "Create":
        file_name = command[1]

        open(file_name, "w").close()

    elif command[0] == "Add":
        file_name = command[1]
        content = command[2]
        with open(file_name, "a") as f:
            f.write(content + "\n")

    elif command[0] == "Replace":
        file_name = command[1]
        old_content = command[2]
        new_content = command[3]
        if os.path.exists(file_name):
            with open(file_name, "r+") as f:
                content = f.read()
                content = content.replace(old_content, new_content)

            with open(file_name, "w") as f:
                f.write(content)
        else:
            print("An error occurred")
    elif command[0] == "Delete":
        file_name = command[1]
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")