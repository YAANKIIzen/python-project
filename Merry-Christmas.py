import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyric = [
        ("Just one ticket out of your heavy gaze", 0.09 ),
        ("I want one ticket off your carousel", 0.1 ),
        ("I want one ticket out  of your heavy gaze", 0.11),
        ("I want one ticket off your carousel", 0.1),
        ("But you should know that I die slow", 0.13),
        ("Running through the halls of your haunted home", 0.09),
        ("And toughest part is that we both know", 0.11),
        ("What happened to you", 0.09),
        ("Why you're out on your own", 0.11),
        ("Merry Christmas, please don't call", 0.12),
        ("Merry Christmas, please, I'm not yours at all", 0.11  ),
        ("Merry Christmas, please don't call me", 0.11),        
    ]
    delays = [0.3, 3.9, 6.3, 11.1, 17.1, 20.5, 23.1, 26.1, 27.3, 31.3, 34.3, 42.5]

    threads = []
    for i in range(len(lyric)):
        text, speed = lyric[i]
        t = Thread(target=sing_lyric, args=(text, delays[i], speed))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join() 

if __name__ == "__main__":
    sing_song()

        
             
