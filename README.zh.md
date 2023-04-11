[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/madeyexz/whisper_subtitle/blob/main/README.md)
[![zh](https://img.shields.io/badge/lang-zh-blue.svg)](https://github.com/madeyexz/whisper_subtitle/blob/main/README.zh.md)

> *本项目仅适用于 Linux/MacOS 用户。*
## 项目概述
本项目

- 使用 [openai/Whisper](https://github.com/openai/whisper) 提供的人工智能技术，自动生成视频字幕。
- 从 [m1guelpf/auto-subtitle](https://github.com/m1guelpf/auto-subtitle) 中适配了一些代码。
- 使用 [openai/Whisper](https://github.com/openai/whisper) 的 [基础模型](https://github.com/openai/whisper#available-models-and-languages)，该模型支持多种语言且运行速度较快。如果您想使用更小的模型，可以在 `main.py` 中更改模型为 `tiny`。但准确性会降低。
- 已经在 8 分钟的 YouTube 视频上进行了测试。 在我的 Mac（CPU, Quad-Core Intel Core i5）上生成字幕大约需要 2 分钟。

## 应用场景
- 为视频生成带有时间戳的字幕，可简化视频编辑。
- 为课程录音添加字幕，*通过阅读字幕而不是听取录音，可以让您的学习速度提高 3 倍*。或许还能通过关键字快速检索、跳转影片。
- 等等...

## 安装依赖项
依赖项：
1. `ffmpeg`：用于从视频中提取音频。
2. `whisper`：用于从音频中生成文本。
    ``` bash
    pip install whisper, ffmpeg
    # 或者
    pip3 install whisper, ffmpeg
    ```

安装 `whisper` 可能需要一些时间，请耐心等待。
## 使用说明
非常简单，只需在终端中复制并粘贴以下命令。

1. 下载本项目：
    ``` bash
    git clone https://github.com/madeyexz/whisper_subtitle.git
    ```

2. 运行 `main.py`，其中 `video_path` 是您的视频文件路径。
如果您是第一次使用 `whisper`（特别是使用 `base` 模型），下载模型可能需要一些时间。请耐心等待。
    ``` python
    python3 main.py video_path
    ```

3. 收集结果。结果将保存在与视频文件相同的目录中，并以视频文件名和 `.srt` 扩展名命名。
播放带有字幕的视频。您可以使用 VLC 或任何其他视频播放器。只需将 `.srt `字幕文件放在原始视频的同一目录中，并通过视频播放器播放视频即可。同时，请确保字幕文件与视频名称相同。