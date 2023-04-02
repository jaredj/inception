import chardet
import os


def get_file_contents(filepath, fallback_encoding='utf-8'):
    with open(filepath, "rb") as f:
        content = None
        if os.path.getsize(filepath) == 0:
            return None
        encoding = chardet.detect(f.read())['encoding']
        f.seek(0)
        try:
            content = f.read().decode(encoding)
        except UnicodeDecodeError:
            print(f"File {filepath} has an invalid encoding ({encoding}), falling back to {fallback_encoding}")
            content = f.read().decode(fallback_encoding)
    return content

