import numpy as np
from collections import defaultdict
import pickle

# initializing default dictionary with default value = None
# and songID dictionary with default value also = None

fingerprints = defaultdict(None)
songID = defaultdict(None)

def addFingerprint(key: tuple, value: list):  #fp (1,2,3) : [(1,2), (1,3)] --song
    #fdlfajfl
    if key not in fingerprints:
        fingerprints[key] = [value]
    else:
        fingerprints[key].append(value)

def removeFingerprint(key: tuple):

    """
    Removes input fingerprint from dictionary 
    """

    if key not in fingerprints:
        return "No such finger print exists :("
    else:
        del fingerprints[key]
        print("Fingerprint deleted :)")

def addSongID(id: int, songInfo: tuple): 
    """
    Add new song ID and informatino to the songID dictionary

    Parameters
    ----------
    
    """
    if id not in songID:
        songID[id] = [songInfo]
    

def removeSongID(id: tuple):

    """
    Removes input id from songID dictionary 
    """

    if id not in songID:
        return "No such song exists :("
    else:
        del songID[id]
        print("Song deleted :)")        

def saveFingerprints():
    """
    Saves the fingerprints dictionary as fingerprints.pkl
    """
    with open("fingerprints.pkl", mode="wb") as opened_file:
        pickle.dump(fingerprints, opened_file)

def loadFingerprints():
    """
    Loads the previously saved fingerprints.pkl and sets the fingerprints
    dictionary equal to it
    """
    with open("fingerprints.pkl", mode="rb") as opened_file:
        fingerprints = pickle.load(fingerprints, opened_file)

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
        songID = pickle.load(songID, opened_file)

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
    