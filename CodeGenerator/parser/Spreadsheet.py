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

        try:
            var_input = Structure._readExcel(self,CONST['Column_VAR_INPUT'])
        except:
            logging.error('Error reading var_input',exc_info=True)

        #read values from colum Datatyp
        datatyp = var_input['Datatyp']
        name = var_input['Name']

        self.valid_data.checkDataType(datatyp,CONST['Column_VAR_INPUT'])
        self.valid_data.checkName(name, CONST['Column_VAR_INPUT'])

        return var_input

    def readVarOutput(self):
        var_output = None

        try:
            var_output = Structure._readExcel(self,CONST['Column_VAR_OUTPUT'])
        except:
            logging.error('Error reading var_output',exc_info=True)
        return var_output

    def readVarInOut(self):
        var_in_out = None
        try:
            var_in_out = Structure._readExcel(self,CONST['Column_VAR_INOUT'])
        except:
            logging.error('Error reading var_in_out',exc_info=True)
        return var_in_out

    def readCtrl(self):
        ctrl = None

        try:
            ctrl = Structure._readExcel(self, CONST['Column_CTRL'])
        except:
            logging.error('Error reading CTRL',exc_info=False)
        return ctrl

    def readSTS(self):
        sts = None
        try:
            sts = Structure._readExcel(self, CONST['Column_STS'])
        except:
            logging.error('Error reading STS',exc_info=True)
        return sts

    def readPRM(self):
        prm = None

        try:
            prm = Structure._readExcel(self, CONST['Column_PRM'])
        except:
            logging.error('Error reading PRM',exc_info=True)
        return prm


    def readInstances(self):
        instances = None

        try:
            instances = Structure._readExcel(self,CONST['Column_Objects'])
        except:
            logging.error('Error reading Instances',exc_info=True)
        return instances
