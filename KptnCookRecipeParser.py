import json

class InputFileHandler:
    filename = ""
    raw_content = ""

    def ___init___(self, filename = ""):
        self.filename = filename
        with open(self.filename,"r") as inputFile:
            self.raw_content = self.__readCompleteFileContent(inputFile)

    def __readCompleteFileContent(self, fileHandler):
        return fileHandler.readlines()
    
    def getCompleteFileContent(self):
        return self.raw_content