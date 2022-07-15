#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
from IPython.display import Audio
from microphone import record_audio
import librosa

# In[7]:


def mic_to_np_array(listen_time):
    frames, sampling_rate = record_audio(listen_time)
    samples = np.hstack([np.frombuffer(i, np.int16) for i in frames])
    return samples, sampling_rate
    
def mp3_to_np_array(file_path):
    samples, sampling_rate = librosa.load(file_path, sr=44100, mono=True)
    return samples, sampling_rate


# In[ ]:




