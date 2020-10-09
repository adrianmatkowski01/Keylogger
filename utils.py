def write_file(file_path, data):
    with open(file_path, "a") as f:
        f.write(data)
