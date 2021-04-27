import json
import glob
import sys

from extract_data import ExtractData
from preprocess_data import PreprocessData
from utils import read_json

if __name__ == '__main__':
    path_documents = ""
    list_documents = glob.glob(path_documents + '*.json')

    # Path of each document
    for path_doc in list_documents:
        # Load json
        data = read_json(path_doc)
        # object
        obj_data = ExtractData(data)
        # call get_paper_id method

        # call get_title method

        # call get_text method

        # Object to pre-process the text
        obj_preprocess = PreprocessData(text)
        # Convert the text to lower case

        # Remove punctuation

        # Remove numbers

        # Remove stop words

        # Remove the special characters

        # Lemmatization

        # Write the documents


