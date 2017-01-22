#!/usr/bin/env python

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.plaintext.writer import PlaintextWriter

### Assign a tempfile name, open it, and truncate it in case any data is in it
tempfilename = "tmp.rtf"
tempfile = open(tempfilename,'w')
tempfile.truncate()

### Set the RTF string to a variable
rtfdata = str("{\\rtf1\\ansi\\deff0{\\colortbl;\\red0\\green0\\blue0;\\red255\\green0\\blue0;}This line is the default color\\line\\cf2This line is red\\line\\cf1This line is the default color}")

### Write the RTF data to the tempfile
tempfile.write(rtfdata)
tempfile.close()

### Read RTF file using Rtf15Reader and print text to screen
rtffile = Rtf15Reader.read(open('tmp.rtf'))
outval = PlaintextWriter.write(rtffile).getvalue()
outval = ' '.join(outval.split())
print outval

### Open and truncate the temp file
tempfile = open(tempfilename,'w')
tempfile.truncate()
tempfile.close()
