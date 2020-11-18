from os import path
from pydub import AudioSegment
import speech_recognition as sr



def convert_mp3_to_wav(audio_file):
    
    src = audio_file
    dst = "result.wav"

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    return dst


def convert_audio_to_text(audio_file):

    r = sr.Recognizer()

    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        print ('Done!')

    try:
        text = r.recognize_google(audio)
        print (text)
        return text

    except Exception as e:
        print (e)
        return e