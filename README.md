# YouTube to RTSP Streamer

A Python script that redirects a YouTube video stream to a local RTSP server using `mediamtx`, `yt-dlp`, and `ffmpeg`. This is useful to test object detection models like YOLO and go beyond your local webcam or skip the chore of downloading test videos.

## Prerequisites

Ensure the following tools are installed and available in your system `PATH`:

* **Python 3.x**
* **[FFmpeg](https://ffmpeg.org/)**: For stream conversion and pushing to RTSP.
* **[yt-dlp](https://github.com/yt-dlp/yt-dlp)**: For extracting the video stream URL.
* **[MediaMTX](https://github.com/bluenviron/mediamtx)**: The RTSP server implementation.

## Configuration

Edit the variables inside the `main()` function within the script:

```python
youtube_url = "[https://www.youtube.com/watch?v=] # Target YouTube Video
rtsp_output = "rtsp://localhost:8554/mystream" # Stream address
```

## Usage

After editing the variables, run the Python file directly.

```bash
python rtsp-stream.py
```


