"""
Class for checking the values from the spreadsheet
Author: dgrill
Date: 06 Dez 2018
"""
import logging

class ValidateData():

    plcTypes = [
        'BOOL',
        'BYTE',
        'INT',
        'DINT',
        'WORD',
        'DWORD',
        'REAL',
        'TIME',

    ]

    def checkDataType(self,datatypes,modulname):
        valid = False

        for line,types in enumerate(datatypes.values):
            for cnt,plc_type in enumerate(ValidateData.plcTypes):

                if plc_type == types:
                    valid = True

                if (cnt == (len(ValidateData.plcTypes)) - 1) and not valid:
                    logging.warning('Unknown datatype: ' + types + ' in colum ' + modulname + ' Line ' + str(line + 2))

                # reset valid flag after iteration
                if (cnt == (len(ValidateData.plcTypes)) - 1):
                    valid = False


