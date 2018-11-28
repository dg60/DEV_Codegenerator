"""
Parser for the Structure spreadsheet
Author: dgrill
Date: 17 Nov 2018
"""
import pandas as pd
from pandas import Series,DataFrame
from CodeGenerator.conf.config import *
import logging

class Structure:

    def __init__(self,srcPath):
        self.srcPath = srcPath
        self.lines = 0
        self.columns = 0

    def _readExcel(self,column):
        data = None
        try:
            data = pd.read_excel(self.srcPath, column)
        except:
            logging.error('Error while reading the excel File' + self.srcPath,exc_info=False)
        return data

    def readVarInput(self):
        var_input = None
        try:
            var_input = Structure._readExcel(self,CONST['Column_VAR_INPUT'])
            print('var_input: ', var_input)
        except:
            logging.error('Error reading var_input',exc_info=True)
        return var_input

    def readVarOutput(self):
        var_output = None
        try:
            var_output = Structure._readExcel(self,CONST['Column_VAR_OUTPUT'])
            print('var_output: ', var_output)
        except:
            logging.error('Error reading var_output',exc_info=True)
        return var_output

    def readVarInOut(self):
        var_in_out = None
        try:
            var_in_out = Structure._readExcel(self,CONST['Column_VAR_INOUT'])
            print('var_in_out: ', var_in_out)
        except:
            logging.error('Error reading var_in_out',exc_info=True)
        return var_in_out

    def readCtrl(self):
        ctrl = None
        try:
            ctrl = Structure._readExcel(self, CONST['Column_CTRL'])
            print('CTRL: ', ctrl)
        except:
            logging.error('Error reading CTRL',exc_info=False)
        return ctrl

    def readSTS(self):
        sts = None
        try:
            sts = Structure._readExcel(self, CONST['Column_STS'])
            print('STS: ', sts)
        except:
            logging.error('Error reading STS',exc_info=True)
        return sts

    def readPRM(self):
        prm = None
        try:
            prm = Structure._readExcel(self, CONST['Column_PRM'])
            print('PRM: ', prm)
        except:
            logging.error('Error reading PRM',exc_info=True)
        return prm


    def readInstances(self):
        instances = None
        try:
            instances = Structure._readExcel(self,CONST['Column_Objects'])
            print('Instances: ', instances)
        except:
            logging.error('Error reading Instances',exc_info=True)
        return instances
