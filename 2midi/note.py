import json
from enum import IntEnum
from typing import List

from mido import Message
from json import load

debug = False

if debug:
    with open('piano_midi.json', 'r') as piano_info:
        pif = json.load(piano_info)


class Last(IntEnum):
    normal = 400
    long = 600
    huge = 800

    def to_suffix(self):
        if self == Last.normal:
            return ''
        elif self == Last.long:
            return ' '
        elif self == Last.huge:
            return '\n'

    @staticmethod
    def from_suffix(suffix: str):
        if suffix == ' ':
            timing = Last.long
        elif suffix == '\n':
            timing = Last.huge
        else:
            timing = Last.normal
        return timing


class Note:
    def __init__(self, tune: int, rise: bool, pitch: int, timing: Last):  # pitch: (+1) 0 [-1], long: is long or not.
        self.tune: int = tune
        self.rise: bool = rise
        self.pitch: int = pitch
        self.timing: Last = timing

    def __str__(self):
        pre_str = f'{"#" if self.rise else ""}{self.tune}{self.timing.to_suffix()}'
        if self.pitch == 1:
            return f'({pre_str})'
        elif self.pitch == -1:
            return f'[{pre_str}]'
        else:
            return pre_str

    def to_midi_msg(self) -> List[Message]:
        t = (60, 62, 64, 65, 67, 69, 71)
        midi_note = t[self.tune - 1] + self.rise + 12 * self.pitch
        if debug:
            print(next((p['note_name'] for p in pif if p['midi'] == midi_note), None))
        return [Message('note_on', note=midi_note, velocity=100, time=0),
                Message('note_off', note=midi_note, velocity=100, time=self.timing)]
