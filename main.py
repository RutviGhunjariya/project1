from text_processor import split_text_into_scenes
from speech_generator import generate_speech
from video_fetcher import fetch_background_video
from video_generator import VideoGenerator
import os

def main(input_text):
    scenes = split_text_into_scenes(input_text)
    os.makedirs("temp", exist_ok=True)
    os.makedirs("output", exist_ok=True)
    video_gen = VideoGenerator()
    scene_video_paths = []

    for idx, scene in enumerate(scenes):
        keyword = scene.split()[0] if scene.split() else "nature"
        background_path = fetch_background_video(keyword)
        if not background_path:
            continue

        speech_path = f"temp/speech_{idx}.mp3"
        scene_video_path = f"temp/scene_{idx}.mp4"

        generate_speech(scene, speech_path)
        video_gen.generate_scene_video(scene, background_path, speech_path, scene_video_path)

        scene_video_paths.append(scene_video_path)

    final_output = "output/final_video.mp4"
    video_gen.combine_scene_videos(scene_video_paths, final_output)
    return final_output
