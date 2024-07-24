
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
youtube_video = "https://www.youtube.com/watch?v=iHHrr9m0Gqc"
video_id = youtube_video.split("=")[1]
transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
transcript = transcript_list.find_generated_transcript(['hi'])
transcript = transcript_list.find_transcript(['hi'])
translated_transcript = transcript.translate('en')
# print(transcript.fetch())
final_transated_transcript = translated_transcript.fetch()


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
for i in final_transated_transcript:
    text = text + " "+i["text"]
sentence = divide_string(text)
print("len = " , len(sentence))

    
summarizer = pipeline('summarization')
result = []
for i in sentence:
    print("Transcript Segment > " , i, "\n")
    point = summarizer(i)[0]["summary_text"]
    print("# Summary >" , point , "\n")
    result.append(point )
    
