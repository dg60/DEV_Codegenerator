"""
Generate source File for a B&R plc in Strutured Text .st
"""
from generators.lang.Base import *


object1 = BaseGenerator('Test')
object1.hello()

class StBuR(BaseGenerator):
    def __init__(self, destFile,language,lstInterface,lstPrm):
        BaseGenerator.__init__(self, destFile,language,lstInterface,lstPrm)

    pass