All bytes are written in little-endian.

palette_size = 256 colors (4 bytes/color)

file_size = palette_size * 4 + 24 = 1048

```
ascii   :'RIFF'           hex  :   52 49 46 46
number  :filesize - 8     hex  :   10 04 00 00
ascii   :'PAL '           hex  :   50 41 4C 20
ascii   :'data'           hex  :   64 61 74 61 
number  :filesize - 20    hex  :   04 04 00 00
number  :03 palette_size  hex  :   00 03 00 01
number  :RGBA components  hex  :   FF 00 00 00 #for red color


```