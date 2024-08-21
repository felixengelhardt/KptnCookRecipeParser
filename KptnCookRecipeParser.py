import json

class KptnCookCollectionObject:
    rawJSONString = None
    collectionJSONObject = None

    def __init__(self,rawJSONString=None):
       self.setRawJSONString(rawJSONString)
    
    def setRawJSONString(self,inputRecipeJSONString):
       self.rawJSONString = inputRecipeJSONString

    def convertRawStringToJSONObject(self):
        self.collectionJSONObject = json.loads(self.rawJSONString)


class InputFileHandler:
    filename = ""
    rawContent = ""

    def __init__(self, filename = ""):
        self.filename = filename
        with open(self.filename,"r") as inputFile:
            self.rawContent = self.__readCompleteFileContent(inputFile)

    def __readCompleteFileContent(self, fileHandler):
        return fileHandler.read()
    
    def getCompleteFileContent(self):
        return self.rawContent
    

if __name__ == "__main__":
    inputFileHandler = InputFileHandler("kptncook_1.json")
    kptnCookCollecction = KptnCookCollectionObject(inputFileHandler.getCompleteFileContent())
    kptnCookCollecction.convertRawStringToJSONObject()
    pass