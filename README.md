# Image-Search-Engine-

This repository contains a Python-based Image Search Engine project that indexes an image dataset, searches for similar images, and accepts a query image using argparse. The search engine uses image descriptors to compare images based on their color and texture features.

Project Overview
The Image Search Engine project has the following components:

index.py: This script is responsible for indexing the image dataset. It extracts color and texture features from each image and stores them in a CSV file called index.csv. The features are used to compare images during the search process.

search.py: This script performs the image search. It loads the query image provided through argparse, extracts its features, compares it with the features of indexed images in index.csv, and returns a set of similar images ranked by similarity.

Installation
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/yourusername/image-search-engine.git
Install the required dependencies:


Usage
Indexing the Image Dataset
To index the image dataset, run the index.py script

Images for this project have been collected from this source: 
http://lear.inrialpes.fr/people/jegou/data.php

css
Copy code
python indexe.py --dataset dataset_folder --index index.csv
dataset_folder: The path to the folder containing the image dataset.
index.csv: The output CSV file to store the image features.
Searching for Similar Images
To search for similar images based on a query image, run the search.py script:

css
Copy code
python search.py --query query_image.jpg --index index.csv
query_image.jpg: The path to the query image you want to search for.
index.csv: The CSV file containing the image features that were generated during the indexing process.
The search script will display a ranked list of similar images based on their similarity to the query image.

Contributing
Contributions to this project are welcome. If you find any bugs or want to add new features, feel free to open an issue or submit a pull request.


Acknowledgments
Special thanks to OpenCV for providing the image processing library used in this project.

With this README documentation, users and contributors will have a clear understanding of the project's purpose, how to install and use it, and the license under which it is distributed. Remember to replace "yourusername" in the GitHub repository URL with your actual GitHub username. Additionally, add any relevant information, credits, or acknowledgments as needed to provide a comprehensive overview of your Image Search Engine project.
