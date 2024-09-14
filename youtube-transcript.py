from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter

# The video ID extracted from the given URL
video_id = 'Ilk7UXzV_Qc'

# Get the transcript for the video
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Format the transcript to JSON format
formatter = JSONFormatter()
json_formatted_transcript = formatter.format_transcript(transcript, indent=2)

# Save the transcript to a JSON file
output_file = 'youtube_transcript.json'
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(json_formatted_transcript)

print(f"Transcript saved to {output_file}")
