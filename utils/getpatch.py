#!/usr/bin/env python3

import mido
import sys

midi_devs = mido.get_ioport_names()

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " MIDI_device_no [file_prefix]")
    print("\nMidi devices:")
    for i in range(len(midi_devs)):
        print(str(i) + ": " + midi_devs[i])
    sys.exit(0)

if len(sys.argv) == 3:
    file_name = sys.argv[2]
else:
    file_name = ''

port = mido.open_input(midi_devs[int(sys.argv[1])])

while True:
    msg = port.receive()
    if msg.type == 'sysex':
        if (msg.data[0] == 65 and
                msg.data[1] == 53 and
                msg.data[2] == 0 and
                msg.data[3] == 35 and
                msg.data[4] == 32):
            alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 -"
            for i in range(42, 52):
                file_name += alpha[msg.data[i]]
            file_name = file_name.rstrip()
            file_name += '.syx'
            mido.write_syx_file(file_name, (msg,))
            break

port.close()
