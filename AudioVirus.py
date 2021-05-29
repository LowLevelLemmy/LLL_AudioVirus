# Get all mp3s
# Play them all

import time
import sys
import os
import fnmatch
from pydub import AudioSegment
from pydub.playback import play

import webbrowser
import PySimpleGUI as sg
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def GetMP3s(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                yield os.path.join(root, name)

def MakeMP3List():
    totalCount = 0
    mp3List = list()
    startTime = time.time()
    for i in GetMP3s('*.mp3', 'C:\\'):
        mp3List.append(str(i))
        totalCount = totalCount + 1
        if totalCount > 100:
            break

        if time.time() - startTime >= 60:  # a min has elapsed
            return mp3List

    return mp3List

def GetMasterAudSeg():
    mp3s = MakeMP3List()
    master = AudioSegment.silent(duration=10 * 1000)
    for i in mp3s:
        sound = AudioSegment.from_file(i)
        master = master.overlay(sound)
    master = master.fade_out(duration=1 * 1000)
    # TODO: increase gain torwards end?
    return master

def GetAndPlayMaster():
    myvoice = AudioSegment.from_file(resource_path("intro.mp3"))
    play(myvoice)
    master = GetMasterAudSeg()
    play(master)
    myvoice = AudioSegment.from_file(resource_path("outro.mp3"))
    play(myvoice)
    os._exit(1)

sg.theme('Black')
layout = [[sg.Image(resource_path("Logo.png"))], [sg.Text("Wait 60 secs...", key="-txt-", enable_events=True)], [sg.Button("Youtube")], [sg.Button("TikTok")],]

window = sg.Window("", layout, size=(200, 300)).Finalize()  # Create the window

t = threading.Thread(target=GetAndPlayMaster,)
t.start()

while True:  # Create an event loop
    window.Refresh()
    event, values = window.read()
    if event == "Youtube":
        webbrowser.open('https://www.youtube.com/channel/UCYwRPV5Wi6C00HE3Yl2Qlqg/videos')
    
    if event == "TikTok":
        webbrowser.open('https://www.tiktok.com/@lowlevellemmy')

    if event == sg.WIN_CLOSED:  # exit program
        break
        


window.close()
os._exit(1)
