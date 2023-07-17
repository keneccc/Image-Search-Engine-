# import the necessary packages
from descriptor import ColorDescriptor
import cv2
import os 

cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output = open("index.csv", "w")
# use glob to grab the image paths and loop over them
image_folder = "Images/"
           


for root,dir,files in os.walk(image_folder):
	for file in files:
		# extract the image ID (i.e. the unique filename) from the image
		# path and load the image itself
		imageID = file
		image_path= f"Images/{file}"
		image = cv2.imread(image_path)
		# describe the image
		features = cd.describe(image)
		# write the features to file
		features = [str(f) for f in features]
		output.write("%s,%s\n" % (imageID, ",".join(features)))
	# close the index file
	output.close() 