import sys
import os
import whisper
import json # used to visualize output
from typing import Iterator, TextIO
import time

def vid_to_audio(file):
    '''extract audio from video using ffmpeg'''
    os.sys("ffmpeg -i {} -ab 160k -ac 2 -ar 44100 -vn audio.mp3".format(file))
    return

def get_working_dir():
    '''get working directory'''
    working_dir = os.getcwd()
    return working_dir

def whisper_transcribe_auto_lang(file="{}/audio.mp3".format(dir)):
    '''transcribe audio to text using whisper'''
    model = whisper.load_model("base")
    result = model.transcribe(file, fp16=False)
    json_object = json.dumps(result, indent=4)
    return result, json_object
def whisper_transcribe_en(file="{}/audio.mp3".format(dir)):
    '''transcribe audio to text using whisper'''
    model = whisper.load_model("base")
    result = model.transcribe(file, fp16 = False, language="English")
    json_object = json.dumps(result, indent=4)
    return result, json_object
def whisper_transcribe_zh(file="{}/audio.mp3".format(dir)):
    '''transcribe audio to text using whisper'''
    model = whisper.load_model("base")
    result = model.transcribe(file, fp16 = False, language="Chinese")
    json_object = json.dumps(result, indent=4)
    return result, json_object

def whisper_result_preview_json(json_object):
    '''useful for debugging, preview the result in json format, this function is not used in the main function'''
    with open("result.json", "w") as f:
        f.write(json_object)
    return

def format_timestamp(seconds: float, always_include_hours: bool = False):
    '''format timestamp to SRT format'''
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    hours_marker = f"{hours}:" if always_include_hours or hours > 0 else ""
    return f"{hours_marker}{minutes:02d}:{seconds:02d}.{milliseconds:03d}"

def write_srt(transcript: Iterator[dict], file: TextIO):
    '''write transcript to SRT file'''
    for i, segment in enumerate(transcript, start=1):
        print(
            f"{i}\n"
            f"{format_timestamp(segment['start'], always_include_hours=True)} --> "
            f"{format_timestamp(segment['end'], always_include_hours=True)}\n"
            f"{segment['text'].strip().replace('-->', '->')}\n",
            file=file,
            flush=True,
        )

def whisper_result_to_srt(whisper_result):
    '''converts whisper result to SRT format'''
    name = file.split(".")[0]
    with open("{}.srt".format(name), "w", encoding="utf-8") as srt:
        write_srt(whisper_result["segments"], file=srt)
    return

def print_wait():
    print("Transcribing video with Whisper... This may take long, please wait...")
    return

if __name__ == "__main__":
    '''main function'''
    print("Getting working directory...")
    dir = get_working_dir()

    start_time = time.time()
    if len(sys.argv) == 2:
        '''default scenario, no language specified, proceeds to auto detect language'''
        print("no language specified, proceeds with base model to auto select...")
        print("Getting file name...")
        file = sys.argv[1]
        print_wait()
        result, json_object = whisper_transcribe_auto_lang(file)

    elif len(sys.argv) == 3 and sys.argv[1] in ["-zh", "-en"]:
        file = sys.argv[2]
        if sys.argv[1] == "-zh":
            print("model selected: base-zh")
            print_wait()
            result, json_object = whisper_transcribe_zh(file)
        elif sys.argv[1] == "-en":
            print("model selected: base-en")
            print_wait()
            result, json_object = whisper_transcribe_en(file)
        else:
            sys.exit("I don't know how you reached here")
            
    else:
        sys.exit("Invalid arguments. Please use -zh or -en or visit https://github.com/madeyexz/whisper_subtitle/ for usage information.")

    
    print("Turning transcription into SRT subtitle file... ")
    whisper_result_to_srt(result) 
        
    end_time = time.time()
    runtime = end_time - start_time
     
    os.system("clear")
    print("Done! Please check the SRT file in the working directory: {}".format(dir))
    print("Runtime: {} seconds, or {} minutes".format(runtime, runtime/60))
