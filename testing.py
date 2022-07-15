import audio
import database as db
import defaults
import fingerprints as fp

audio.mp3_input("/Users/aaronyang/Desktop/BWSI/Week1/mp3s/Rickroll.mp3", "Never Gonna Give You Up", "Rick Astley")
audio.mp3_input("/Users/aaronyang/Desktop/BWSI/Week1/mp3s/CallMeMaybe.mp3", "Call Me Maybe", "Carly Rae Jepsen")

print(db.fingerprints)