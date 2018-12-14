"""
Parser for the Structure spreadsheet
Author: dgrill
Date: 17 Nov 2018
"""
import pandas as pd
from pandas import Series,DataFrame
from CodeGenerator.conf.config import *
from CodeGenerator.parser.Checks import ValidateData
import logging

class Structure:

    def __init__(self,srcPath):
        self.srcPath = srcPath
        self.lines = 0
        self.columns = 0
        self.valid_data = ValidateData()

    def _readExcel(self,column):
        data = None

        try:
            data = pd.read_excel(self.srcPath, column)
        except:
            logging.error('Error while reading the excel File' + self.srcPath,exc_info=False)
        return data

    def readVarInput(self):
        var_input = None
        datatyp = None
        name = None
        comment = None

        try:
            var_input = Structure._readExcel(self,CONST['Column_VAR_INPUT'])
        except:
            logging.error('Error reading var_input',exc_info=True)

        # read values from colums
        datatyp = var_input['Datatyp']
        name = var_input['Name']
        comment = var_input['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_VAR_INPUT'])
        self.valid_data.checkName(name, CONST['Column_VAR_INPUT'])
        self.valid_data.checkComment(comment,CONST['Column_VAR_INPUT'])

        return var_input

    def readVarOutput(self):
        var_output = None
        datatyp = None
        name = None
        comment = None

        try:
            var_output = Structure._readExcel(self,CONST['Column_VAR_OUTPUT'])
        except:
            logging.error('Error reading var_output',exc_info=True)

        # read values from colums
        datatyp = var_output['Datatyp']
        name = var_output['Name']
        comment = var_output['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_VAR_OUTPUT'])
        self.valid_data.checkName(name, CONST['Column_VAR_OUTPUT'])
        self.valid_data.checkComment(comment,CONST['Column_VAR_OUTPUT'])

        return var_output

    def readVarInOut(self):
        var_in_out = None
        datatyp = None
        name = None
        comment = None

        try:
            var_in_out = Structure._readExcel(self,CONST['Column_VAR_INOUT'])
        except:
            logging.error('Error reading var_in_out',exc_info=True)

        # read values from colums
        datatyp = var_in_out['Datatyp']
        name = var_in_out['Name']
        comment = var_in_out['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_VAR_INOUT'])
        self.valid_data.checkName(name, CONST['Column_VAR_INOUT'])
        self.valid_data.checkComment(comment,CONST['Column_VAR_INOUT'])

        return var_in_out

    def readCtrl(self):
        ctrl = None
        datatyp = None
        name = None
        comment = None

        try:
            ctrl = Structure._readExcel(self, CONST['Column_CTRL'])
        except:
            logging.error('Error reading CTRL',exc_info=False)

        # read values from colums
        datatyp = ctrl['Datatyp']
        name = ctrl['Name']
        comment = ctrl['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_CTRL'])
        self.valid_data.checkName(name, CONST['Column_CTRL'])
        self.valid_data.checkComment(comment,CONST['Column_CTRL'])


        return ctrl

    def readSTS(self):
        sts = None
        datatyp = None
        name = None
        comment = None

        try:
            sts = Structure._readExcel(self, CONST['Column_STS'])
        except:
            logging.error('Error reading STS',exc_info=True)

        # read values from colums
        datatyp = sts['Datatyp']
        name = sts['Name']
        comment = sts['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_STS'])
        self.valid_data.checkName(name, CONST['Column_STS'])
        self.valid_data.checkComment(comment,CONST['Column_STS'])

        return sts

    def readPRM(self):
        prm = None
        datatyp = None
        name = None
        comment = None

        try:
            prm = Structure._readExcel(self, CONST['Column_PRM'])
        except:
            logging.error('Error reading PRM',exc_info=True)

        # read values from colums
        datatyp = prm['Datatyp']
        name = prm['Name']
        comment = prm['Comment']

        # check the values
        self.valid_data.checkDataType(datatyp,CONST['Column_PRM'])
        self.valid_data.checkName(name, CONST['Column_PRM'])
        self.valid_data.checkComment(comment,CONST['Column_PRM'])

        return prm


    def readInstances(self):
        instances = None

        try:
            instances = Structure._readExcel(self,CONST['Column_Objects'])
        except:
            logging.error('Error reading Instances',exc_info=True)
        return instances
