from concurrent.futures import ThreadPoolExecutor, as_completed
from dankware import clr_banner, align, clr, cls
from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
from win10toast import ToastNotifier
from playsound import playsound
import time
import os

banner = '''

                                                               
   _         _             _               _ _     _           
 _| |___ ___| |_   ___ _ _| |_ ___ ___ ___| |_|___| |_ ___ ___ 
| . | .'|   | '_|_| .'| | |  _| . |___|  _| | |  _| '_| -_|  _|
|___|__,|_|_|_,_|_|__,|___|_| |___|   |___|_|_|___|_,_|___|_|  
                                                               

'''

os.chdir(os.path.dirname(__file__))
cls(); print(align(clr_banner(banner)))
delay = float(input(clr("  > Click Delay: ")))
toast = ToastNotifier()
mouse = Controller()
resume_key = Key.f1 
pause_key = Key.f2
exit_key = Key.f3
running = True
pause = True
print(clr(f"\n  > Controls: Resume = {resume_key} | Pause = {pause_key} | Exit = {exit_key}".replace("Key.","")))

def notify(mode):
    
    def start():
        try:playsound('start.mp3')
        except:pass
        toast.show_toast("dank.auto-clicker","✅ Started",duration = 3,icon_path = "dankware.ico",threaded = False)
    
    def stop():
        try:playsound('stop.mp3')
        except:pass
        toast.show_toast("dank.auto-clicker","❌ Stopped",duration = 3,icon_path = "dankware.ico",threaded = False)
    
    def terminate():
        try:playsound('stop.mp3')
        except:pass
    
    if mode == 1:as_completed(ThreadPoolExecutor(1).submit(start))
    elif mode == 2:as_completed(ThreadPoolExecutor(1).submit(stop))
    elif mode == 3:as_completed(ThreadPoolExecutor(1).submit(terminate))

def on_press(key):
    
    global running, pause
    if key == resume_key and pause: pause = False; notify(1)
    elif key == pause_key and not pause: pause = True; notify(2)
    elif key == exit_key and running: running = False; notify(3)
    
def main():

    toast.show_toast("dank.auto-clicker","😎 Online!",duration = 3,icon_path = "dankware.ico",threaded = False)
    
    listener = Listener(on_press=on_press)
    listener.start()
    while running:
        if not pause:
            mouse.click(Button.left, 1)
            time.sleep(delay)
        else:time.sleep(2)
    listener.stop()

    toast.show_toast("dank.auto-clicker","😁 Goodbye!",duration = 3,icon_path = "dankware.ico",threaded = False)

if __name__ == "__main__":
    main()