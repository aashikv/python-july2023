def get_file_extension(filename):
    if "." in filename:
        parts = filename.split(".")
        extension = parts[-1]
        return extension
    else:
        return "No extension found"

def main():
    filename = input("Enter the filename: ")
    extension = get_file_extension(filename)
    print(f"The extension of the file is: {extension}")

if __name__ == "__main__":
    main()
