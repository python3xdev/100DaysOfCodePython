# from playsound import playsound
from just_playback import Playback


class SoundManager:
    def __init__(self):
        self.playback = Playback()
        self.brick_hit_sound = "sounds/brick.wav"
        self.player_hit_sound = "sounds/player.wav"
        self.wall_hit_sound = "sounds/wall.wav"
        self.lost_life_sound = "sounds/lost_life.wav"
        self.win_sound = "sounds/win.wav"

    def brick_hit(self):
        # if not self.playback.active:
        self.playback.load_file(self.brick_hit_sound)
        self.playback.play()

    def player_hit(self):
        self.playback.load_file(self.player_hit_sound)
        self.playback.play()

    def wall_hit(self):
        self.playback.load_file(self.wall_hit_sound)
        self.playback.play()

    def lost_life(self):
        self.playback.load_file(self.lost_life_sound)
        self.playback.play()

    def win(self):
        self.playback.load_file(self.win_sound)
        self.playback.play()
