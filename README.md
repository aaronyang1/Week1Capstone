defaults.py (hyperparameters) 

database.py (Aaron, Kate, Josh)
  - [defaultdict (f1,f2, dt): list (SongId, T)]
  -   pickle save
  -   pickle load
  -   add songs
  -     prevent duplicate songs
  -   remove songs
  -   query for songs
  - [SongID:name]
  -   pickle save
  -   pickle load
  -   add songs
  -     prevent duplicate songs
  -   remove songs
  -   query for songs

audio.py (Jamie)
  - record audio from microphone
  -   turn audio file into numpy array of samples
  - take in existing MP3 files
  -   turn audio file into numpy array of samples

fingerprinting.py (everyone else)
  - function to turn array of samples into spectrogram
  - function that uses spectrogram to find peaks & fingerprints
  -   save fingerprints in database
 
 matching.py
  - function to take new audio files and match them to songs in database
  
