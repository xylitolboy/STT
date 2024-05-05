import moviepy.editor as mp

class vid_to_audio:
    def __init__(self,video_path,audio_path):
        self.video = video_path
        self.audio = audio_path
    
    def transform(self):
        video = mp.VideoFileClip(self.video_path)
        print("Converting Video to Audio....")
        video.audio.write_audiofile(self.audio_path)
    
    