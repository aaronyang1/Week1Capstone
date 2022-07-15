import audio
import database as db
import defaults
import fingerprints as fp
import librosa
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab
import numpy as np
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure


'''
audio.mp3_input("/Users/aaronyang/Desktop/BWSI/Week1/mp3s/Rickroll.mp3", "Never Gonna Give You Up", "Rick Astley")
audio.mp3_input("/Users/aaronyang/Desktop/BWSI/Week1/mp3s/CallMeMaybe.mp3", "Call Me Maybe", "Carly Rae Jepsen")
'''
samples, sampling_rate = librosa.load("/Users/aaronyang/Desktop/BWSI/Week1/mp3s/Rickroll.mp3", sr=44100, mono=True)

spectrogram, cutoff = fp.samples_to_spectogram(samples, sampling_rate)

base_structure = generate_binary_structure(2,1)
neighborhood = iterate_structure(base_structure, 20)

print(cutoff)

L_peaks = fp.local_peak_locations(spectrogram, neighborhood, cutoff)
print(L_peaks[:100])