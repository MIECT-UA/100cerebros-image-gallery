from hashlib import sha256
from ImageEditor.imageMenu import run_option
from ImageEditor.text_menu_server import menu_server
import sys
import os
 
def getEffects(path):
    # Paths stuff :P 
    nameFile     = os.path.basename(path).split(".")[0]
    imgExtension = os.path.basename(path).split(".")[1]
    
    folderPath = "effects/" + nameFile 
    if not (os.path.exists(folderPath)):  # creates dir if it doesn't exist
        os.makedirs(folderPath)

    # Get effects dictionary
    effects = run_option(path, 0)
    
    # Save effects dictionary
    for i in effects:
        for key, value in i.items():
            filePath = folderPath + "/" + key + "." + imgExtension
            value.save(filePath)
            print("Saved " + key + " effect/filter sucessfully.")

    print("Operation done sucessfully.")
    exit(0)

if __name__ == "__main__":
    getEffects(sys.argv[1])
