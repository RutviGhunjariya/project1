from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip, concatenate_videoclips

class VideoGenerator:
    def generate_scene_video(self, text, background_video_path, speech_audio_path, output_path):
        background_clip = VideoFileClip(background_video_path).subclip(0, 5)
        audio_clip = AudioFileClip(speech_audio_path)

        text_clip = TextClip(text, fontsize=50, color='white', bg_color='transparent', size=background_clip.size)
        text_clip = text_clip.set_position('center').set_duration(audio_clip.duration).fadein(1).fadeout(1)

        background_clip = background_clip.set_duration(audio_clip.duration)

        final_clip = CompositeVideoClip([background_clip, text_clip]).set_audio(audio_clip)
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

    def combine_scene_videos(self, scene_video_paths, output_path):
        clips = [VideoFileClip(path) for path in scene_video_paths]
        final_video = concatenate_videoclips(clips)
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
