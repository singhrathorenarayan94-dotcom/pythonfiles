import os
while True:
    cmd = input(">>> ").strip().lower()

    match cmd:
        case "pwd":
            print(os.getcwd())
        case "ls":
            print(os.listdir())
        case "exit":
            print("Bye!")
            break
        case _:
            print("Unknown Command")
