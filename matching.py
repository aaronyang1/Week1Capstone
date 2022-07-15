import fingerprints as fp
import audio as ad
import database as db
import defaults as df
from collections import defaultdict
import numpy as np

def matching(listen_time, database : list , fanout = 15):
    """
    Parameters:

    listen_time : 

    database: 
    
    Returns:
        matchedSong tuple[string, string]: 
        returns tuple with song name and song artist
        using song ID corresponding to song in database that matches input_audio the best. 
        Returns -1 if no match found.
    """
    samples, sample_rate  = ad.mic_to_np_array(listen_time) # process user inputted audio from mic into samples + sample rate
    spectrogram = fp.samples_to_spectrogram(samples, sample_rate) # turn processed user audio into spectrogram

    peaks = fp.local_peak_locations(spectrogram, fp.neighborhood, fp.find_min_amp(spectrogram))

    fingerprints_input = fp.fingerprints(peaks, fanout) #Fingerprint function returns one arr (fps, ti)
    
    song_tally = defaultdict(None)
    
    for fingerprint in fingerprints_input:
        songs = db.getFingerprint(fingerprint) #songs is list of tuples of form songid, times 
        #from songs, check if empty then make every songid a key and add 1 to corresponding value
        if songs is not None:
            for song_tuple in songs:
                t_offset = song_tuple[1] - fingerprint[2]
                if song_tally.has_key((song_tuple[0], t_offset)): 
                    song_tally[(song_tuple[0], t_offset)] += 1 
                else:
                    song_tally[(song_tuple[0], t_offset)] = 1 
    song_info = max(song_tally, key = song_tally.get) # gets key with max tally

    #threshold = 10
    if song_tally[song_info] >= df.THRESHOLD:     
        matchedSong = db.getSong(song_info[0]) # tuple with name, artist of matched song      
        return matchedSong
    else:
        return -1

