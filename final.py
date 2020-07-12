# Code to rotate all images in an input directory
# in increments of 30 degrees and store them
# in an output directory  
# The rotation increment can be changed to any degree as required in the i loop


# import the Python Image processing Library 
from PIL import Image 

# import os module
import os 


def main():
     
    # path of the folder / directory containing the raw images, 
    # note the escape sequence 
    input_dir ="E:\\LiClipse\\InputDir"

    # imagePath contains name of the image
    imagevar = 0
    for imagevar in os.listdir(input_dir): 
         
        inputpath = os.path.join(input_dir, imagevar) 

        # inputPath contains the full directory name 
        im = Image.open(inputpath) 

        i = 0
        for i in range(0, 360, 30):
            # Rotate image
            new = im.rotate(i)
            # new.show()
            
            # Change to output directory to store rotated images 
            os.chdir("E:\\LiClipse\\OutputDir")
            
            # Change name of output file to denote its name and rotation degree
            new = new.save("Rotate" + str(i) +imagevar)
 

# Driver Function 
if __name__ == '__main__': 
    main() 
