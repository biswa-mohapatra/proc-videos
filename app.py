import os
import pandas as pd
from pathlib import Path,PureWindowsPath
from tracking_app import start_tracking

def main(video_path):
    try:
        start_tracking(video_path)
    except Exception as e:
        raise e

if __name__ == '__main__':
    result = {
        "Video":[],
        "Human label":[],
        "Prediction":[]
    }
    folders = ["good","susp","mal"]
    for folder in folders:
        print(f"Accessing {folder}")
        videos = os.listdir(f"{folder}/")
        for video in videos:
            result["Video"].append(video)
            result["Human label"].append(folder)
            video_path = f"{folder}/{video}"
            print(f"Passing {video_path}")
            pred = main(video_path)
            result["Prediction"].append(pred)
            print(f"Prediction {pred}\n")
    data = pd.DataFrame(result)
    print(data)