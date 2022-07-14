#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from IPython.display import Audio
from typing import Tuple
from microphone import record_audio


# In[7]:


def mic_to_np_array(listen_time: float, file_path: str):
    frames, sample_rate = record_audio(listen_time)
    samples = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    array_with_sample_rate = np.hstack((sample_rate, samples))
    np.save(file_path, array_with_sample_rate)
    
def mp3_to_np_array(file_path: str) -> Tuple[np.ndarray, int]:
    loaded_array = np.load(file_path)
    sample_rate = loaded_array[0]
    signal = loaded_array[1:]
    return signal, sample_rate


# In[ ]:




