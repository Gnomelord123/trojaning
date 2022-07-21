import os

# 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

def run(**args):
    print("[*] in dirlister module.")
    files = os.listdir(".")
    return str(files)