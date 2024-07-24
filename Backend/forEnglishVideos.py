from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
# https://www.youtube.com/watch?v=y8qRq9PMCh8   Krish Nayak
# https://www.youtube.com/watch?v=iOjthKqDlFg   Dhruv Rathi
# https://www.youtube.com/watch?v=iHHrr9m0Gqc Ayushi ka Interview
youtube_video = "https://www.youtube.com/watch?v=y8qRq9PMCh8"
video_id = youtube_video.split("=")[1]
YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# ====================
def divide_string(input_string):
    max_length = 1020
    words = input_string.split()
    divided_strings = []
    current_string = ""

    for word in words:
        if len(current_string) + len(word) + 1 <= max_length:
            if current_string:
                current_string += " "
            current_string += word
        else:
            divided_strings.append(current_string)
            current_string = word

    if current_string:
        divided_strings.append(current_string)

    return divided_strings
# ====================
text=""
for i in transcript:
    text = text + " "+i["text"]
sentence = divide_string(text)
print("len = " , len(sentence))

    
summarizer = pipeline('summarization')
result = ""
for i in sentence:
    print("TEXT>>>> \n" ,  i)
    print("SUMMARY>>> \n" , summarizer(i)[0]["summary_text"])
    


