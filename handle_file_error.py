def handle_file_error():
    filename = input("Enter the filename to read: ")
    
    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print(f"File content:\n{content}")
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
    except IOError:
        print(f"Error: The file {filename} could not be read.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the error handling function
handle_file_error()
