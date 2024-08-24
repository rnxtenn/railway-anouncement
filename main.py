import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    pass

# This function returns pydubs audio segment
def mergeAudios(audios):
    pass

def generateSkeleton():
    audio=AudioSegment.from_mp3('railwayAudio.mp3')
    # Generate 'Kripiya dheyan dijiye
    start=18000
    finish=20200
    audioProcessed= audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

def generateAnnouncement(filename):
    pass

if __name__== "__main__":
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement.....")
    generateAnnouncement("railway.xlsx")