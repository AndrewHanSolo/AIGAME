import scipy
from pydub import AudioSegment

songDir = "C:\Users\Andrew\Desktop/"
song1 = "TD"
song2 = "RW"

song1Path = songDir + song1
song2Path = songDir + song2




TD_mp3 = AudioSegment.from_mp3(song1Path)
TD_mp3.export(songDir + song1, format="wav")




RW_mp3 = AudioSegment.from_mp3(song2Path)
RW_mp3.export(songDir + song2, format="wav")


samplingRate, data = scipy.io.wavfile.read(songDir + song2 + ".wav")
samplingRate, data = scipy.io.wavfile.read(somefile + song2 + ".wav")