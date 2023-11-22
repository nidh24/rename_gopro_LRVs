import os

def rename_files(folder_path, old_letter, new_letter, old_extension, new_extension):
    # Ensure the folder path ends with a '/'

    # Iterate through each file in the folder
    for filename in os.listdir(folder_path):
        # Check if the file has the specified old extension
        if filename.endswith(old_extension):
            # Create the new filename by replacing letters and changing extension
            new_filename = filename.replace(old_extension, new_extension).replace(old_letter, new_letter)
    
            # Construct the full file paths
            old_filepath = folder_path + filename
            new_filepath = folder_path + new_filename

            # Rename the file
            os.rename(old_filepath, new_filepath)

            # Print a message for each file renamed
            print(f'Renamed: {old_filepath}  ->  {new_filepath}')

# Example usage:
folder_path = r"C:\\Users\\PATH\\TO\\YOUR\\FOLDER\\"
old_letter = 'L'
new_letter = 'X'
old_extension = '.LRV'
new_extension = '.MP4'

rename_files(folder_path, old_letter, new_letter, old_extension, new_extension)
