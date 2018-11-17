"""
Baseclass for the code generators
"""


class BaseGenerator:
    def __init__(self, destFile,language,lstInterface,lstPrm):
        self.f = destFile
        self.lang = language
        self.lstInterface = lstInterface
        self.lstPrm = lstPrm

    def hello(self):
        print('Hello from the CodeGenerator')

    def generateDescription(self):
        pass

    def generateCall(self):
        pass
