# Composition parts (Car creates them, they live and die with the Car)
class AudioSystem:
    def play_sound(self):
        print("Audio: playing music...")
 
    def stop_sound(self):
        print("Audio: music stopped")