import os

if __name__ == "__main__":
    blenderLocation = "/Users/alon/Downloads/blender-2.79-macOS-10.6/blender.app/Contents/MacOS/blender"
    os.system(blenderLocation + " --background  test.blend --python clear.py")
    # os.system(blenderLocation + " --background test.blend --python blend.py -- \"Tomer Aharoni: MakeHarvard 2018 1st Place\" \"This picture contains two dancing people\"")
    os.system(blenderLocation + " --background test.blend --python blend.py -- \"With a friend like you, I can really count myself lucky. May your birthday be wonderful!\" \"Two people dancing in a club and smiling\"")