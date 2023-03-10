from time import sleep

import vlc

p = vlc.MediaPlayer('''scream.mp3''')
p.play()
sleep(1)
p.stop()


