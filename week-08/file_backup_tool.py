import os 

def copy_file():
    source = input("Enter the source file name: ")
    destination = input("Enter the destination file name: ")

    try:
        # Check if source exists
        if not os.path.exists(source):
            print("Error: Source file does not exist.")
            return
        
        # Prevents overwriting destination
        if os.path.exists(destination):
            print("Error: Destination file already exists. Backup cancelled to prevent overwrite.")
            return
        
        with open(source, "r") as src_file:
            content = src_file.read()

        with open(destination, "w") as dest_file:
            dest_file.write(content)
        
        print("File copied successfully!")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except IOError:
        print("Error: Unable to read or write file.")

    except Exception as error:
        print(f"Unexpected error occurred: {error}")

if __name__ == "__main__":
    copy_file()