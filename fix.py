import os
import sys
os.chdir(sys.path[0])

import xml.etree.ElementTree as ET
tree = ET.parse('./src/playlists.xml')
root = tree.getroot()

# Optional Functionality:
# I keep my playlists local to my music folder instead of on my hard drive
# Example: 
# directory = "D:\\0\\audio\\music\\"
directory = ""

for child in root:
    filename = child.attrib['filename']
    title = child.attrib['title'].replace("/", "-")

    input = open('./src/' + filename)
    input_read = input.read().splitlines()
    
    output = open('./out/' + title + ".m3u", "w")
    
    for line in input_read:
        if "#EXT" not in line:
            x = line.replace(directory, "").replace("\\", "/")
            output.write(x + "\n")
