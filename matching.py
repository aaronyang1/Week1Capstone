import fingerprints as fp
import audio as ad
import database as db
from collections import defaultdict

def matching(listen_time, database : list , fanout = 15):
    """

    Parameters:

    listen_time : 

    database:
    
    Returns:
        song_ID: song ID corresponding to song in database that matches input_audio the best. Returns -1 if no match found.

    """
    samples, sample_rate, songName = ad.mic_to_np_array(listen_time)
    spectrogram = fp.samples_to_spectrogram(samples, sample_rate) 

    peaks = fp.local_peak_locations(spectrogram, fp.neighborhood, find_min_amp(spectrogram))

    
    fingerprints_input = fp.fingerprints(peaks, fanout) #Fingerprint function returns one arr (fps, ti)
    
    song_tally = defaultdict(None)
    
    for fingerprint in fingerprints_input:
        songs = db.getFingerprint(fingerprint) #songs is list of tuples of form songid, times 
        #from songs, check if empty then make every songid a key and add 1 to corresponding value
        if songs is not None:
            for song_tuple in songs:
                # wait do we need to add a case where the id is not yet in the dictionary 
                song_tally[song_tuple[0]] += 1 
        else:
            #is this the case when the input song is not in the dictionary?
        

def find_min_amp(spectrogram):
    """
    Finds minimum threshold for amplitude such that peaks are significant. 
    Identified as 75th percentile amplitude from spectrogram.
    """
    

    
    # song_count_dict

