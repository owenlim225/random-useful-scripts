import os

def list_all_files(folder_path):
    file_list = []  # Initialize an empty list to store filenames
    
    # Iterate over all files in the given folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and filename.endswith('.mp3'):  # Ensure it's an MP3 file
            # Remove the .mp3 extension from the filename
            file_list.append(os.path.splitext(filename)[0])
    
    return file_list

if __name__ == "__main__":
    # Folder path
    folder_path = r"C:\Users\sherwin\Desktop\My music\Yuwan's Music Pack #1"
    
    # Get the list of all MP3 files without the .mp3 extension
    files = list_all_files(folder_path)
    
    # Print out the filenames without the .mp3 extension
    for file in files:
        print(file)
