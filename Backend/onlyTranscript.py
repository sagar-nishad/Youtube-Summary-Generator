from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
youtube_video = "https://www.youtube.com/watch?v=iOjthKqDlFg"
video_id = youtube_video.split("=")[1]
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
transcript = transcript_list.find_generated_transcript(['hi'])
transcript = transcript_list.find_transcript(['hi'])
translated_transcript = transcript.translate('en')
# print(transcript.fetch())
final_transated_transcript = translated_transcript.fetch()
for i in final_transated_transcript:
    print(i)