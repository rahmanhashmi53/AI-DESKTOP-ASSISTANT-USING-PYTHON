import vlc
import os
import random
import time

# Define the directory where your music files are stored
music_dir = r"C:/Users/rahma/Desktop/AI Desktop Voice Assistant Using Python/songs"

class MusicController:
    def __init__(self):
        self.player = vlc.MediaPlayer()
        self.is_paused = False
        self.current_music = None

    def play_random_music(self):
        # Get a list of all music files in the directory
        music_files = os.listdir(music_dir)
        # Select a random music file from the list
        random_music = random.choice(music_files)
        self.current_music = os.path.join(music_dir, random_music)
        # Load and play the selected music file
        self.player.set_media(vlc.Media(self.current_music))
        self.player.play()
        self.is_paused = False

    def pause_music(self):
        if self.player.is_playing():
            self.player.pause()
            self.is_paused = True

    def resume_music(self):
        if self.is_paused:
            self.player.play()
            self.is_paused = False
        else:
            print("No music to resume")

    def stop_music(self):
        self.player.stop()
        self.is_paused = False

    def next_song(self):
        self.stop_music()
        self.play_random_music()

# Test the functions
if __name__ == "__main__":
    mc = MusicController()
    mc.play_random_music()
    time.sleep(5)  # Let the music play for 5 seconds
    mc.pause_music()
    time.sleep(2)  # Pause for 2 seconds
    mc.resume_music()
    time.sleep(5)  # Let the music play for 5 more seconds
    mc.next_song()
