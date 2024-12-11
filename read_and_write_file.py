def read_and_write_file(input_filename, output_filename):
    try:
        # Open the input file in read mode
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the content (you can perform any modification here)
        modified_content = content.upper()  # Example: converting to uppercase

        # Write the modified content to a new file
        with open(output_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content has been written to {output_filename}")
    except FileNotFoundError:
        print(f"The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = "example.txt"
output_filename = "modified_example.txt"
read_and_write_file(input_filename, output_filename)
