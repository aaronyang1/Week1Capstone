import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from microphone import record_audio

from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.morphology import iterate_structure
from numba import njit
from typing import Tuple, Callable, List



#spectrogram function
spectrogram, freqs, times = mlab.specgram(
    samples,
    NFFT=4096,
    Fs=sampling_rate,
    window=mlab.window_hanning,
    noverlap=int(4096 / 2)
)
spectrogram = map(lambda x: x if x != 0 else 10**(-12), spectrogram)
np.log10(spectrogram)


#peaks function 

@njit
def _peaks(
    data_2d: np.ndarray, nbrhd_row_offsets: np.ndarray, nbrhd_col_offsets: np.ndarray, amp_min: float
) -> List[Tuple[int, int]]:
    
    """
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected.

    nbrhd_row_offsets : numpy.ndarray, shape-(N,)
        The row-index offsets used to traverse the local neighborhood.
        
        E.g., given the row/col-offsets (dr, dc), the element at 
        index (r+dr, c+dc) will reside in the neighborhood centered at (r, c).
    
    nbrhd_col_offsets : numpy.ndarray, shape-(N,)
        The col-index offsets used to traverse the local neighborhood. See
        `nbrhd_row_offsets` for more details.
        
    amp_min : float
        All amplitudes equal to or below this value are excluded from being
        local peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location, returned in 
        column-major order
    """

    peaks = []
    for c, r in np.ndindex(*data_2d.shape[::-1]):
        if data_2d[r, c] <= amp_min:
            continue
    
    for dr, dc in zip(nbrhd_row_offsets, nbrhd_col_offsets):
        if dr == 0 and dc == 0:
            continue
        if not (0 <= r + dr < data_2d.shape[0]):    
            continue
        if data_2d[r, c] < data_2d[r + dr, c + dc]:
                
                break
        else:
            
            peaks.append((r, c))
    return peaks

def local_peak_locations(data_2d: np.ndarray, neighborhood: np.ndarray, amp_min: float):
    """
    Parameters
    ----------
    data_2d : numpy.ndarray, shape-(H, W)
        The 2D array of data in which local peaks will be detected
    
    neighborhood : numpy.ndarray, shape-(h, w)
        A boolean mask indicating the "neighborhood" in which each
        datum will be assessed to determine whether or not it is
        a local peak. h and w must be odd-valued numbers
        
    amp_min : float
        All amplitudes at and below this value are excluded from being local 
        peaks.
    
    Returns
    -------
    List[Tuple[int, int]]
        (row, col) index pair for each local peak location, returned
        in column-major ordering.
    
    """
    
    
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    nbrhd_row_indices, nbrhd_col_indices = np.where(neighborhood)
    

    nbrhd_row_offsets = nbrhd_row_indices - neighborhood.shape[0] // 2
    nbrhd_col_offsets = nbrhd_col_indices - neighborhood.shape[1] // 2

    return _peaks(data_2d, nbrhd_row_offsets, nbrhd_col_offsets, amp_min=amp_min)


#neighborhood

base_structure = generate_binary_structure(2,1)
neighborhood = iterate_structure(base_structure, 20s)

#fingerprints
def fingerprints(peaks: np.ndarray, fanout = 15):
    
    """
    
    
    Parameters:
        peaks : List[Tuple[int, int]]
            (row, col) index pair for each local peak location in column-major order
        
        fanout: int 
            Numbers of nearest peak connectionns
        
    
    Returns:
    
        fingerprints : List[Tuple[float, float, float]
            (initial peak frequency, fanout peak frequency, time between peaks)
    
    """
    fingerprints = []
    
    for i in range(len(peaks) - fanout):
        for j in range(fanout):
            fingerprints.append(peaks[i, 0], peaks[i + j, 0], peaks[i+j, 1] - peaks[i , 1])
            
    return fingerprints 
    

            
