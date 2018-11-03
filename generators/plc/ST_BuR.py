"""
Generate source File for a B&R plc in Strutured Text .st
"""

import generators.Generator as Gen


object1 = Gen.CodeGenerator('test')
object1.hello()

class ST_BUR(Gen.CodeGenerator):
    pass