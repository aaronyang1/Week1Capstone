import numpy as np
from collections import defaultdict
import pickle

# initializing default dictionary with default value = None
# and songID dictionary with default value also = None

fingerprints = defaultdict(None)
songID = defaultdict(None)

def addFingerprint(key: tuple, value: tuple):  #fp (1,2,3) : [(1,2), (1,3)] --song
    """
    Adds fingerprint key/value pair to the fingerprints dictionary

    Parameters
    ----------
    key: tuple, shape = (3,)
        fingerprint in the form (f_i, f_j, ∆t_ij)
    
    value: tuple, shape = (2,)
        Tuple containing songID and time pair.
    """
    if key not in fingerprints:
        fingerprints[key] = [value]
    else:
        fingerprints[key].append(value)

def removeFingerprint(key: tuple, value: list):
    """
    Removes input fingerprint from dictionary 
    
    Parameters
    ----------
    key: tuple, shape = ()
    """

    if key not in fingerprints:
        return "No such finger print exists :("
    else:
        values = fingerprints[key]
        values.remove(value)
        fingerprints[key] = values
        
        print("Fingerprint value deleted :)")

def addSongID(id: int, songInfo: tuple): 
    """
    Add new song ID and informatino to the songID dictionary

    Parameters
    ----------
    id: int
        Value of the song ID to be added
    
    songInfo: tuple, shape = (2,)
        Tuple containing the song name and artist
    """
    songID[id] = [songInfo]
    

def removeSongID(id: int):

    """
    Removes input id from songID dictionary 

    Parameters
    -----------
    id: int
        Value of the song ID to be removed
    """

    if id not in songID:
        return "No such song exists :("
    else:
        del songID[id]
        print("Song deleted :)")        

def saveFingerprints(not_fingerprints):
    """
    Saves the fingerprints dictionary as fingerprints.pkl
    """
    with open("fingerprints.pkl", mode="wb") as opened_file:
        pickle.dump(not_fingerprints, opened_file)

def loadFingerprints():
    """
    Loads the previously saved fingerprints.pkl and sets the fingerprints
    dictionary equal to it
    """
    with open("fingerprints.pkl", mode="rb") as opened_file:
        fingerprints1 = pickle.load(opened_file)
    fingerprints = fingerprints1

def saveSongIDs():
    """
    Saves the songID dictionary as songID.pkl
    """
    with open("songID.pkl", mode="wb") as opened_file:
        pickle.dump(songID, opened_file)
        
def loadSongIDs():
    """
    Loads the previously saved songID.pkl and sets the v
    dictionary equal to it
    """
    with open("songID.pkl", mode="rb") as opened_file:
        songID = pickle.load(opened_file)

def getFingerprint(key: tuple):
    """
    Gets all times in all songs where a certain fingerprint occurs
    
    Parameters
    -----------
    key : tuple, shape = (3, )
        The fingerprint whos times and songs we want to retrieve

    Returns
    ------------
    list, shape = (N, 2)
        List of tuples containing songIDs and times
    """
    return fingerprints[key]

def getSong (key: int):
    """
    Gets name of song from songID dictionary given its songID.
    """
    return songID[key]

"""
addFingerprint((1, 2, 3), (4, 5, 6))
addFingerprint((1, 2, 3), (7, 8, 9))
addFingerprint((3, 2, 1), (10, 11, 12))
saveFingerprints(fingerprints)
"""

temp = loadFingerprints()
print(temp)

"""
addSongID(1, ("Halo Theme", "Ryan Soklaski"))
addSongID(2, ('Waluigiverse', 'Ryan Soklaski'))
addSongID(3, ('Never Gonna Give You Up', 'Ryan Soklaski'))
addSongID(4, ("Song of Storms", 'Ryan Soklaski'))
addSongID(2, ("Cotton Eye Joe", 'Ryan Soklaski'))
print(getSong(4))
"""