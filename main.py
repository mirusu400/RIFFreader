import sys
import os
import json
import binascii
class palette():
    def __init__(self):
        
        return
    
if __name__ == "__main__":
    src = sys.argv[1]
    try:
        dst = sys.argv[2]
    except IndexError:
        dst = os.path.splitext(src)[0] + ".json"
    data = {}

    size = os.path.getsize(src)
    count = (size - 0x18) // 4
    fin = open(src, "rb")
    fout = open(dst, "w")

    # Check the file is correct
    buf = fin.read(4)
    if buf != b'RIFF':
        print("It doesn't seems RIFF(palette) file!")
        sys.exit()

    data['size'] = size
    data['color'] = []
    fin.seek(0x18)
    for i in range(count):
        r = binascii.hexlify(fin.read(1)).decode('utf-8')
        g = binascii.hexlify(fin.read(1)).decode('utf-8')
        b = binascii.hexlify(fin.read(1)).decode('utf-8')
        a = binascii.hexlify(fin.read(1)).decode('utf-8')
        color = (i, r, g, b, a)
        data['color'].append(color)
    # print(data)
    json.dump(data, fout, indent=4)

    fin.close()
    fout.close()
