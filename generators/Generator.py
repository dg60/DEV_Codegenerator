"""
Baseclass for the code generators
"""


class CodeGenerator:
    def __init__(self, inputFile):
        self.input = inputFile

    def hello(self):
        print('Hello from the CodeGenerator')

    def generateDescription(self):
        pass

    def generateCall(self):
        pass
