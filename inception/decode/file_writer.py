def write_files(file_contents):
    for file_path, content_lines in file_contents.items():
        with open(file_path, 'w') as f:
            f.write('\n'.join(content_lines))

