import os
import shutil

# Define the source directory
source_dir = 'forg'

# Create a dictionary to map file extensions to their corresponding folder
file_type_mapping = {
    'txt': 'TextFiles',
    'pdf': 'PDFFiles',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'csv': 'CSVFiles',
    'docx': 'WordDocuments'
    # Add more mappings as needed
}

# Function to organize files based on file extension
def organize_files(source_dir):
    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        # Get the full path of the file
        file_path = os.path.join(source_dir, filename)

        # Skip directories, only process files
        if os.path.isfile(file_path):
            # Get the file extension
            file_extension = filename.split('.')[-1]

            # Check if the file extension is in the mapping dictionary
            if file_extension in file_type_mapping:
                # Determine the target directory based on file extension
                target_folder = os.path.join(source_dir, file_type_mapping[file_extension])

                # Create the target directory if it doesn't exist
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Move the file to the target directory
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f'Moved: {filename} to {target_folder}')

# Call the function to organize files
organize_files(source_dir)
