from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})


# =========================================================================
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
summarizer = pipeline('summarization')
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
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

# =========================================================================

@app.route('/api/summarize')
def keyword_search():
    inputText = request.args.get('text', '').lower()
    text = divide_string(inputText)
    result = ""
    for i in text:
        result = result + " " + summarizer(i)[0]["summary_text"]
    # print(">>>>>", searchTerm)
    return jsonify({"text":result})

# =========================================================================
@app.route('/api/youtubesummaryHindi', methods=['GET'])
def get_summary():

    # inputText = request.args.get('link', '').lower()
    # youtube_video = "https://www.youtube.com/watch?v=iHHrr9m0Gqc"
    inputText = request.json.get('link')
    
    youtube_video = inputText
    video_id = youtube_video.split("=")[1]
    transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    transcript = transcript_list.find_generated_transcript(['hi'])
    transcript = transcript_list.find_transcript(['hi'])
    translated_transcript = transcript.translate('en')
    final_transated_transcript = translated_transcript.fetch()
    text=""
    for i in final_transated_transcript:
        text = text + " "+i["text"]
    sentence = divide_string(text)

    
    summarizer = pipeline('summarization')
    result = []
    for i in sentence:
        summary = summarizer(i)[0]["summary_text"]
        result.append(summary)
 
    return jsonify({'summary': result})
    # return jsonify({'summary': ["point 1" , "point 2"]})
# =========================================================================
@app.route('/api/youtubesummaryEnglish', methods=['POST'])
def get_Default_summary():

    # inputText = request.args.get('link', '').lower()
    inputText = request.json.get('link')
    youtube_video = inputText
    # youtube_video = "https://www.youtube.com/watch?v=y8qRq9PMCh8"
    video_id = youtube_video.split("=")[1]
    YouTubeTranscriptApi.get_transcript(video_id)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    final_transated_transcript = transcript
    text=""
    for i in final_transated_transcript:
        text = text + " "+i["text"]
    sentence = divide_string(text)

    
    summarizer = pipeline('summarization')
    result = []
    for i in sentence:
        summary = summarizer(i)[0]["summary_text"]
        result.append(summary)
 
    return jsonify({'summary': result})
    # return jsonify({'summary': ["point 1" , "point 2"]})
# =========================================================================

if __name__ == '__main__':
    app.run(debug=True)