import requests
import os
import json

# Get online stable doc version number

def get_numpy_doc_version(inPath : str ) -> str :
    """
    Gets the online numpy documentation version number accessible from inPath

    Returns the version as a vx.xx string
    """
    r = requests.get(inPath)

    docVersion = r.text.split('title')

    docVersion = "".join(docVersion[1]).split(' ')

    return docVersion[-2]# = docTitle[-2]

print(get_numpy_doc_version('https://numpy.org/doc/stable/reference/index.html'))

def build_function_index():
    """
    Builds the index of all available functions.
    This index will be used to randomly pull a function name ine the doc and then wget 
    the corresponding file on the numpy documentation official website
    """
