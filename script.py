from time import sleep

import vlc

p = vlc.MediaPlayer('''data/scream.mp3''')
p.play()
sleep(1)
p.stop()


