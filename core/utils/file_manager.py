from typing import Optional


def file_to_list(
        filename: str
):
    with open(filename, 'r+') as f:
        all_lines = filter(bool, f.read().splitlines())
        no_comments = filter(lambda s: not(s.startswith("#")), all_lines)

        return list(no_comments)


def str_to_file(file_name: str, msg: str, mode: Optional[str] = "a"):
    with open(
            file_name,
            mode
    ) as text_file:
        text_file.write(f"{msg}\n")


def shift_file(file):
    with open(file, 'r+') as f:  # open file in read / write mode
        first_line = f.readline()  # read the first line and throw it out
        data = f.read()  # read the rest
        f.seek(0)  # set the cursor to the top of the file
        f.write(data)  # write the data back
        f.truncate()  # set the file size to the current size
        return first_line.strip()
