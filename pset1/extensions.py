def main():
    extensions()


def extensions():
    user_input = input("File name: ").lower().strip().split(".")
    extension = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
    }
    if user_input[1] in extension:
        print(extension[user_input[1]])
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()