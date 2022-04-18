class MarkdownParser:
    def __init__(self, file):
        self.htmlResult = ""
        self.initializeLine()
        self.data = open(file).readlines()

    def initializeLine(self):
        self.i = 0
        self.hashCounter = 0
        self.hashFlag = 0
        self.linkState = 0
        self.linkText = ""
        self.link = ""

    def parseMarkdown(self):
        for line in self.data:
            if line == "\n":
                continue
            self.initializeLine()
            while self.i < len(line) - 1:
                if not self.hashFlag:
                    self.headerCheck(line)
                else:
                    self.linkCheck(line)
                self.i += 1
            if self.hashCounter:
                if self.linkState > 1:
                    self.htmlResult += self.linkText + self.link
                self.getEndHeadingTags()
            else:
                if self.linkState >= 1:
                    self.htmlResult += self.linkText + self.link
                self.htmlResult += "</p>"
            self.htmlResult += "\n"
        return self.htmlResult

    def getEndHeadingTags(self):
        if self.hashCounter > 6:
            self.htmlResult += "</h6>"
        else:
            self.htmlResult += "</h" + str(self.hashCounter) + ">"

    def linkCheck(self, line):
        if line[self.i] == "[" and self.linkState < 1:
            self.linkText += "["
            self.linkState = 1
        elif self.linkState == 1 and self.linkState < 2:
            if line[self.i] == "]":
                self.linkText += "]"
                self.linkState = 2
            else:
                self.linkText += line[self.i]
        elif self.linkState == 2 and self.linkState < 3:
            if line[self.i] == "(":
                self.link += "("
                self.linkState = 3
        elif self.linkState == 3:
            if line[self.i] == ")":
                self.link += ")"
                self.linkState = 0
                self.htmlResult += self.getAnchorTag()
                self.link = ""
                self.linkText = ""
            else:
                self.link += line[self.i]
        else:
            self.htmlResult += line[self.i]

    def getAnchorTag(self):
        return '<a href="' + self.link[1:-1] + '">' + self.linkText[1:-1] + "</a>"

    def headerCheck(self, line):
        if line[self.i] == "#":
            self.hashCounter += 1
        else:
            if self.hashCounter:
                self.getStartHeadingTag()
                self.htmlResult += line[self.i]
            elif line[self.i] == "[":
                self.linkText += "["
                self.linkState = 1
                self.htmlResult += "<p>"
            else:
                self.htmlResult += "<p>" + line[self.i]
            self.hashFlag = 1

    def getStartHeadingTag(self):
        if self.hashCounter > 6:
            self.htmlResult += "<h6>" + "#" * (self.hashCounter - 6)
        else:
            self.htmlResult += "<h" + str(self.hashCounter) + ">"
