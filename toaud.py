# step 2: convert video to audio

# Python code to convert video to audio
import moviepy.editor as mp

# Insert Local Video File Path
clip = mp.VideoFileClip(r"<YOUR PATH TO VIDEO HERE/.mp4>") #replace the video path

# Insert Local Audio File Path
clip.audio.write_audiofile(r"YOUR PATH TO OUTPUT AUDIO/.mp3") #replace the audio path