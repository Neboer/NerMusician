import random
import sys
from typing import List

from mido import Message, MidiFile, MidiTrack, MetaMessage

from note import Note
from parser import parse


def notes_to_midi(input_notes: List[Note]) -> MidiTrack:
    track = MidiTrack()
    track.append(Message('program_change', program=0))
    for note in input_notes:
        track += note.to_midi_msg()
    return track


if __name__ == '__main__':
    outfile = MidiFile()
    input_string = '''2#12(23#12)6 #467 6 #4\n3#45#435#47(#12)(#1)#5#67(#1)\n4#4(23#12)6 #467 6 #4\n3#4567(#123#45#43#12)7'''
    notes = parse(input_string)
    # print(' '.join((str(x.timing) for x in notes)))
    track = notes_to_midi(notes)
    outfile.tracks.append(track)
    outfile.save('test.mid')
