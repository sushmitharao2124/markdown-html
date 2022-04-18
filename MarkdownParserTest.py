import pytest
from MarkdownParser import *


def test_markdownParser():
    for i in range(1, 4):
        testFileName = "testCase" + str(i) + ".txt"
        testOutputFile = "testOutput" + str(i) + ".txt"
        markdownParser = MarkdownParser(testFileName)
        assert markdownParser.parseMarkdown() == open(testOutputFile, "r").read()
