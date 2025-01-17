import string

def get_content(filename: string) -> string:
    with open(filename, 'r', encoding='utf-8') as fp:
        content = fp.read()

    return content