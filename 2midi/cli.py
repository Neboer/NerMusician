from mido import MidiFile

from midier import notes_to_midi
from parser import parse

import subprocess, os, platform


code = ''

while True:
    user_input_line = input()
    if user_input_line:
        code += f'\n{user_input_line}'
    else:
        break

outfile = MidiFile()
notes = parse(code)
track = notes_to_midi(notes)
outfile.tracks.append(track)
outfile.save('test.mid')

if platform.system() == 'Darwin':       # macOS
    subprocess.call(('open', 'test.mid'))
elif platform.system() == 'Windows':    # Windows
    os.startfile('test.mid')
else:                                   # linux variants
    subprocess.call(('xdg-open', 'test.mid'))