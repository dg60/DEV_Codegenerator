from generators.lang.ST_BuR import *
from generators.lang.CPP_BuR import *
from generators.lang.Base import *

from conf.config import *


class CodeGeneratorBuR():
    def __init__(self, destFile,language,lstInterface,lstPrm):
        self.f = destFile
        self.lang = language
        self.lstInterface = lstInterface
        self.lstPrm = lstPrm

    def generate(self):

        if self.lang == CONST['St']:
            self.generateSt()
        elif self.lang == CONST['Cpp']:
            self.generateCpp()

    def generateSt(self):
        st = StBuR()
        pass

    def generateCpp(self):
        cpp = CppBuR()

        pass