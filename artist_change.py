import os
from mutagen.id3 import ID3, TIT2, TPE1, TALB
from mutagen.id3 import ID3NoHeaderError
from mutagen.easyid3 import EasyID3

def update_metadata(folder_path, artist_name, album_name):
    # Supported audio file extensions
    audio_extensions = ['.mp3']

    # Iterate through all files in the folder
    for file_name in os.listdir(folder_path):
        if any(file_name.lower().endswith(ext) for ext in audio_extensions):
            file_path = os.path.join(folder_path, file_name)
            try:
                # Load existing ID3 tags or create new ones
                audio_file = ID3(file_path)
            except ID3NoHeaderError:
                audio_file = ID3()

            # Extract the current title without the extension
            current_title = os.path.splitext(file_name)[0]
            # Set new metadata
            audio_file['TIT2'] = TIT2(encoding=3, text=f'{artist_name} - {current_title}')
            audio_file['TPE1'] = TPE1(encoding=3, text=artist_name)
            audio_file['TALB'] = TALB(encoding=3, text=album_name)
            
            # Save changes
            audio_file.save()

# Example usage
folder_path = r'C:\Users\sherwin\Desktop\My music\Instrumental'
artist_name = 'Esphiel'
album_name = 'First Drop'
update_metadata(folder_path, artist_name, album_name)
