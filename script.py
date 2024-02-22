import os
import zipfile

# Define the directory containing your zip files
zip_directory = 'dir_name'

# Define the directory where you want to save the extracted data
output_directory = 'dir_name'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all files in the zip directory
for zip_file_name in os.listdir(zip_directory):
    if zip_file_name.endswith('.zip'):
        # Construct the full path to the zip file
        zip_file_path = os.path.join(zip_directory, zip_file_name)

        # Create a subdirectory for the current zip file
        subdirectory_name = os.path.splitext(zip_file_name)[0]
        subdirectory_path = os.path.join(output_directory, subdirectory_name)

        # Create the subdirectory if it doesn't exist
        if not os.path.exists(subdirectory_path):
            os.makedirs(subdirectory_path)

        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
            # Extract all contents of the zip file to the subdirectory
            zip_file.extractall(subdirectory_path)
        
        print("Extraction complete.", zip_file_name,"Data saved in:", output_directory)
