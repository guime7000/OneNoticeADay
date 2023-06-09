import requests
from dotenv import dotenv_values
import json
import glob


def get_numpy_doc_version(inPath: str) -> str:
    """
    Gets the online numpy documentation version number accessible from inPath

    Returns the version as a vx.xx string
    """
    r = requests.get(inPath)

    docVersion = r.text.split("title")

    docVersion = "".join(docVersion[1]).split(" ")

    return docVersion[-2]


def build_doc_directory_functions_index(docDirPath: str) -> list[str]:
    """
    Builds the index of all available functions in the generated Doc Directory
    # This index will be used to randomly pull a function name in the doc and then wget
    # the corresponding file on the numpy documentation official website
    """

    return glob.glob(os.path.join(docDirPath, "*.html"))


def process_html_file(
    functionIndex: list[str], saveDirPath: str, libraryName: str = "numpy"
):
    """
    For each html file in functionIndex list, will extract the relevant content and save it to a
    new html file.
    """

    if libraryName == "numpy":
        for functionFile in functionIndex:
            fileName = functionFile.split("/")[-1]

            sectionId = fileName.split(".")
            if sectionId[-2][0:2] == "__":
                sectionId[-2] = sectionId[-2][2:-2]
            sectionId = "-".join(sectionId[:-1])
            with open(functionFile, "r") as inFile:
                fileContent = inFile.read()

            docTitle = fileContent.split(f'<section id="{sectionId}">')
            docTitle = "".join(docTitle[1]).split("</section>")

            with open(os.path.join(saveDirPath, fileName), "w") as outFile:
                outFile.write(docTitle[0])


directoriesConfig = dotenv_values("../Config/.env.dir_config")

docFilesArboRead = directoriesConfig["DOC_FILES_DIRECTORY_READ"]
docFilesArboSave = directoriesConfig["PROCESSED_FILES_DIRECTORY_SAVE"]


func_index = build_doc_directory_functions_index(docFilesArboRead)

process_html_file(func_index, docFilesArboSave, "numpy")
