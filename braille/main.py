import os
import sys

if __name__ == "__main__":
    f = open(os.path.join("..", sys.argv[1]))
    r = f.read().split("\n")
    blenderLocation = "./blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
    # os.system(blenderLocation + " --background  test.blend --python clear.py")
    # os.system(blenderLocation + " --background test.blend --python blend.py -- \"Tomer Aharoni: MakeHarvard 2018 1st Place\" \"This picture contains two dancing people\"")
    # os.system(blenderLocation + " --background test.blend --python blend.py -- \"With a friend like you, I can really count myself lucky. May your birthday be wonderful!\" \"Two people dancing in a club and smiling\"")
    os.system(blenderLocation + " --background test.blend --python blend.py -- %s %s".format(r[0], r[1]))