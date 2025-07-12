
from collections import defaultdict
from music21 import *

def analyze_musicxml(file_path):
    score = converter.parse(file_path)
    key = score.analyze('key')
    note_counts = defaultdict(int)
    for note in score.flat.notes:
        degree = note.pitches[0].transpose(-key.tonic.pitchClass).name
        note_counts[degree] += 1
    return note_counts

# Example usage
file_path = 'https://www.musicxml.com/music-in-musicxml/'
print(analyze_musicxml(file_path))
