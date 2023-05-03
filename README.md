[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/madeyexz/whisper_subtitle/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-blue.svg)](https://github.com/madeyexz/whisper_subtitle/blob/main/README.zh.md)


> *This project is only available to Linux/MacOS users.*

## About This Project 
This project
  
- uses [openai/Whisper](https://github.com/openai/whisper) from OpenAI to generate video subtitles automatically.

- adapted some codes from [m1guelpf/auto-subtitle](https://github.com/m1guelpf/auto-subtitle).
- uses the [base model](https://github.com/openai/whisper#available-models-and-languages) from [openai/Whisper](https://github.com/openai/whisper). Which is multi-lingual and fairly fast. If you want to use a smaller model, you can change the model in `main.py` to `tiny`. However, the accuracy will be lower.
- has been tested on a youtube video of 8 min duration. It took around 2 min to generate the subtitles on my mac (CPU, Quad-Core Intel Core i5).
## Potential Application
- Generate time-stamped subtitles for your video. Would be helpful in video editing.
- Add subtitles to lesson recordings to learn 3x faster by reading subtitles instead of listening. You might also navigate lectures via keywords.
- and more...
## Installation
Dependency:
1. `ffmpeg`: used to extract audio from video
2. `whisper`: used to generate text from audio
   ``` bash
   pip install whisper, ffmpeg
   # or
   pip3 install whisper, ffmpeg
   ```
It might take a while to install `whisper`. Please be patient.
## Usage
It's fairly simple, just copy and paste the following commands in your terminal.
1. Download the project
   ``` bash
   git clone https://github.com/madeyexz/whisper_subtitle.git
   ```
2. Run `main.py`, where `video_path` is the path to your video file and `-LanguageCode` is where you choose the language of the subtitles. 
   - Currently only `-en` and `-zh` is available for English and Chinese subtitles respectively. However if you don't specify the language, it will choose language automatically.
   - If its your first project with `whisper` (especially with `base` model), it will take a while to download the model. Please be patient.

   ``` zsh
   python3 main.py -LanguageCode video_path
   ```
   e.g. 
   ```python
   python3 main.py -en video.mp4
   ```
3. Collect the result. The result will be saved in the same directory as the video file and will be named as the video file name with `.srt` extension.
4. Play the video with subtitles. You can use VLC or any other video player. Just put the `.srt` subtitle file in the same directory with the original video and play the video via the video player. Also, check if the subtitle file has the same name with the video.





