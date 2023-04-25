from oneNoticeTools import process_html_file


def test_check_section_Id() -> None:
    functionIndex = ["numpy.titi.toto.html"]
    saveDirPath = "toto"
    assert (process_html_file(functionIndex, saveDirPath, "numpy")) == "titi-toto"
