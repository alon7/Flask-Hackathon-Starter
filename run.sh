#/bin/bash

#cleaning previous cache 
> textToPrint.txt
#adding text received by web form
cat /Users/Tomeraharoni/Documents/MakeHarvard/info/greetingText.txt > /Users/Tomeraharoni/Documents/MakeHarvard/info/textToPrint.txt
#print to screen:
echo "Converting image to text.."
#converting image to text
python getImageInfo.py >> /Users/Tomeraharoni/Documents/MakeHarvard/info/textToPrint.txt
echo done

