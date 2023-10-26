import wave # <- Biblioteca para reproduzir arquivos WAV
from music21 import midi # <- Biblioteca para reproduzir arquivos MIDI
from numpy import *
from IPython.display import Audio

max_amplitude = iinfo('uint16').max # 2**NUM_BITS-1

def audioread(filename):
    """
    Carrega os dados do som em um arquivo e retorna os dados no array 'soundx'
    com tipo de dado 'numpy.float', junto com a frequencia de amostragem 'fs'
    Cada canal de som será uma coluna do array.
    """
    ifile = wave.open(filename)
    channels = ifile.getnchannels()
    fs = ifile.getframerate()
    frames = ifile.getnframes()
    x = ifile.readframes(frames)
    x = fromstring(x, dtype='uint16')
    x = x.astype('int16')
    x = x.astype(float)/max_amplitude
    soundx = x
    if channels > 1:
        soundx = x.reshape((int(len(x)/channels), channels))
    
    return soundx, fs

def play(x, fs=None):
    """
    Reproduz arquivos de Audio (WAV, OGG)
    """
    display(Audio(data=x, rate=fs))

def playMIDI(filename):
    """
    Reproduz um arquivo MIDI
    """
    mf = midi.MidiFile()
    mf.open(filename)
    mf.read()
    mf.close()
    s = midi.translate.midiFileToStream(mf)
    s.show('midi')