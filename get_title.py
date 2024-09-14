import os
import re

def natural_sort_key(text):
    """Generate a sorting key that sorts text in a natural order."""
    return [int(part) if part.isdigit() else part.lower() for part in re.split(r'(\d+)', text)]

def get_song_titles(folder_path):
    # Supported audio file extensions
    audio_extensions = ['.mp3', '.wav', '.flac', '.m4a', '.ogg', '.aac']

    # List to store song titles
    song_titles = []

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        # Check if the file is an audio file
        if any(file_name.lower().endswith(ext) for ext in audio_extensions):
            # Remove the extension and add the title to the list
            title = os.path.splitext(file_name)[0]
            song_titles.append(title)

    # Sort the song titles in natural descending order
    song_titles.sort(key=natural_sort_key, reverse=False)

    # Define the output file path inside the folder
    output_file = os.path.join(folder_path, 'instrumental_records.txt')

    # Write the sorted song titles to the output file
    with open(output_file, 'w') as f:
        for title in song_titles:
            f.write(title + '\n')

# Example usage
folder_path = r'C:\Users\sherwin\Desktop\My music\Instrumental'
get_song_titles(folder_path)
