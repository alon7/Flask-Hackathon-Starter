#/bin/bash

mkdir -p info
#cleaning previous cache 
touch textToPrint.txt
#adding text received by web form
cat ./info/greetingText.txt > ./info/textToPrint.txt
#print to screen:
echo "Converting image to text.."
#converting image to text
python getImageInfo.py >> ./info/textToPrint.txt

pushd braille
python main.py info/textToPrint.txt
popd

echo done

