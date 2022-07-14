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
    
    
    assert neighborhood.shape[0] % 2 == 1
    assert neighborhood.shape[1] % 2 == 1

    nbrhd_row_indices, nbrhd_col_indices = np.where(neighborhood)
    

    nbrhd_row_offsets = nbrhd_row_indices - neighborhood.shape[0] // 2
    nbrhd_col_offsets = nbrhd_col_indices - neighborhood.shape[1] // 2

    return _peaks(data_2d, nbrhd_row_offsets, nbrhd_col_offsets, amp_min=amp_min)

def local_peaks_mask(data: np.ndarray, cutoff: float) -> np.ndarray:
   
    neighborhood_array = generate_binary_structure(2, 2)  

    peak_locations = local_peak_locations(data, neighborhood_array, cutoff)  

 
    peak_locations = np.array(peak_locations)

 
    mask = np.zeros(data.shape, dtype=bool)


    mask[peak_locations[:, 0], peak_locations[:, 1]] = 1
  
    return mask

#neighborhood

base_structure = generate_binary_structure(2,1)
neighborhood = iterate_structure(base_structure, 20s)

#fingerprints
def fingerprints(data):
    fanout = 15
    s = peak_locations.shape

    
    

            
