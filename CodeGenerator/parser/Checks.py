"""
Class for checking the values from the spreadsheet
Author: dgrill
Date: 06 Dez 2018
"""
import logging

class ValidateData():

    plcTypes = (
        'BOOL',
        'BYTE',
        'INT',
        'DINT',
        'WORD',
        'DWORD',
        'REAL',
        'TIME',
    )

    invalidCharacters = (
        'ä',
        'Ä',
        'ö',
        'Ö',
        'Ü',
        'ü',
        '$',
        '&',

    )

    def __init__(self):
        self.max_length_name = 50
        self.max_length_comment = 100


    def checkDataType(self,datatypes,modulname):
        valid = False

        for line,types in enumerate(datatypes.values):
            for cnt,plc_type in enumerate(ValidateData.plcTypes):

                if plc_type == types:
                    valid = True

                if (cnt == (len(ValidateData.plcTypes)) - 1) and not valid:
                    logging.warning('Unknown datatype: ' + types + ' in worksheet ' + modulname + ' Line ' + str(line + 2))

                # reset valid flag after iteration
                if (cnt == (len(ValidateData.plcTypes)) - 1):
                    valid = False

    def checkName(self,name, modulname):

        for cnt, names in enumerate(name):

            if any(i in names for i in ValidateData.invalidCharacters):
                logging.warning('Not allowed character ' + str(ValidateData.invalidCharacters) +  ' in worksheet ' + modulname + ' Line ' + str((cnt + 2)))

            if len(names) > self.max_length_name:
                logging.warning('Name was too long in worksheet ' + modulname + ' Line ' + str((cnt + 2)) +
                                ' | ' + names + ' was ' + str(len(names)) + ' characters long ' + '| Allowed max: ' + str(self.max_length_name))


