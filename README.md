# RIFFreader
A simple RIFF(Microsoft palette file) reader, written in Python3.

# Usage
```
from rreader import palette

# palette(src, dst)
p = palette("./example/TLP.pal")

# return a palette as an tuple array
p.getpalette()

# dump a palette to json
p.dump()
```

Or just simply...
```
python3 rreader.py ./example/TLP.pal ./example/TLP.json
```
# See also..
* https://github.com/antonvladyka/palette

* https://www.cyotek.com/blog/loading-microsoft-riff-palette-pal-files-with-csharp