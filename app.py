import os
from pathlib import Path
from tracking_app import start_tracking

def main(video_path):
    try:
        start_tracking(video_path)
    except Exception as e:
        raise e

if __name__ == '__main__':
    video_path = "mal/video_1662704502381-curr_time-3300.mp4"
    print(video_path)
    main(video_path)

