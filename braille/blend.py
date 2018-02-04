import bpy
import sys
import os

dir = os.path.dirname(bpy.data.filepath)

if not dir in sys.path:
    sys.path.append(dir)

import engToBraille

text = sys.argv[6].split()
text.insert(0, "Text:")
picture_text = sys.argv[7].split()
picture_text.insert(0, "Picture:")
input_text = engToBraille.translate_sentence(text)
input_picture = engToBraille.translate_sentence(picture_text)

def createBraille(my_bool,x,y):
    #create cube
    bpy.ops.mesh.primitive_cube_add(enter_editmode=False, location=(x, y, 0.5), rotation=(1.57, 0, 0), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
    #change dimensions of cube to (1, 1, 1)
    bpy.ops.transform.resize(value=(0.25, 0.25, 0.08), constraint_axis=(False, False, False), constraint_orientation='GLOBAL', mirror=False, proportional='DISABLED', proportional_edit_falloff='SMOOTH', proportional_size=1)
    if(my_bool):
        #add cylinder
        bpy.ops.mesh.primitive_cylinder_add(radius=0.125, depth=0.125, view_align=False, enter_editmode=False, location=(x, y, 0.625), layers=(True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False))
        obj = bpy.context.active_object
        mat = bpy.data.materials.new('Red')
        mat.diffuse_color = (1,0.1,0.1)
        obj.data.materials.append(mat)
    
        
    
initialX = 0
initialY = -8
letterCount = 0
lineCount = 0

lastLetterCount = 0
lastLineCount = 0
for word in input_text:
    for letter in word:
        letterCount += 1
        for i in range(0,3):
            createBraille(letter[2*i],initialX,initialY)
            createBraille(letter[2*i+1],initialX,initialY+0.5)
            createBraille(0,initialX,initialY+0.6)
            initialX += 0.5
        initialY += 1.1
        if letterCount == 14:
            letterCount = 0
            initialX = 1.5*lineCount
            initialX += 1.5
            lineCount += 1
            initialY = -8
        else:
            initialX = 1.5*lineCount
        lastLetterCount = letterCount
        
print('last letter count: ' + str(lastLetterCount))
for i in range (14, lastLetterCount, -1):
    for i in range(0,3):
        createBraille(0,initialX,initialY)
        createBraille(0,initialX,initialY+0.5)
        createBraille(0,initialX,initialY+0.6)
        initialX += 0.5
    initialY += 1.1
    initialX = 1.5*lineCount

initialY = -8
lastLineCount = lineCount
for i in range (6, lastLineCount, -1):
    for j in range (14, 0, -1):
        for h in range(0,3):
            createBraille(0,initialX,initialY)
            createBraille(0,initialX,initialY+0.5)
            createBraille(0,initialX,initialY+0.6)
            initialX += 0.5
        initialY += 1.1
        initialX = 1.5*lineCount
            
    initialX = 1.5*lineCount
    initialX += 1.5
    lineCount += 1
    initialY = -8
        

# Back part

initialX = 10
initialY = -8
letterCount = 0
lineCount = 0


for word in input_picture:
    for letter in word:
        letterCount += 1
        for i in range(0,3):
            createBraille(letter[2*i],initialX,initialY)
            createBraille(letter[2*i+1],initialX,initialY+0.5)
            createBraille(0,initialX,initialY+0.6)
            initialX += 0.5
        initialY += 1.1
        if letterCount == 14:
            letterCount = 0
            initialX = 10 + 1.5*lineCount
            initialX += 1.5
            lineCount += 1
            initialY = -8
        else:
            initialX = 10 + 1.5*lineCount
        lastLetterCount = letterCount

print('last letter count: ' + str(lastLetterCount))
for i in range (14, lastLetterCount, -1):
    for i in range(0,3):
        createBraille(0,initialX,initialY)
        createBraille(0,initialX,initialY+0.5)
        createBraille(0,initialX,initialY+0.6)
        initialX += 0.5
    initialY += 1.1
    initialX = 10 + 1.5*lineCount

initialY = -8
lastLineCount = lineCount
for i in range (6, lastLineCount, -1):
    for j in range (14, 0, -1):
        for h in range(0,3):
            createBraille(0,initialX,initialY)
            createBraille(0,initialX,initialY+0.5)
            createBraille(0,initialX,initialY+0.6)
            initialX += 0.5
        initialY += 1.1
        initialX = 10 + 1.5*lineCount
            
    initialX = 10 + 1.5*lineCount
    initialX += 1.5
    lineCount += 1
    initialY = -8
        
bpy.ops.wm.save_as_mainfile()
# bpy.context.scene.objects.active = Boundary
bpy.ops.export_mesh.stl(filepath="test.stl")