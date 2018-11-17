"""
Generate source File for a B&R plc in C++ .cpp
"""

from generators.lang.Base import *

object1 = BaseGenerator('Test')
object1.hello()

class CppBuR(BaseGenerator):

    def __init__(self, destFile,language,lstInterface,lstPrm):
        BaseGenerator.__init__(self, destFile,language,lstInterface,lstPrm)

    def test(self):
        self.f
        pass