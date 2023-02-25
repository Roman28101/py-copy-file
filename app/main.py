def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3:
        if command_list[1] != command_list[2] and command_list[0] == "cp":
            try:
                with (
                    open(command_list[1], "r") as file_in,
                    open(command_list[2], "w") as file_out
                ):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file in directory")


copy_file(input("Enter your command: "))
