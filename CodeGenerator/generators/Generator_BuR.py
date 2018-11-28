"""
Generator for BuR PLC
Author: dgrill
Date: 17 Nov 2018
"""
from CodeGenerator.conf.config import *
from datetime import datetime
import logging
from CodeGenerator.generators import BaseGenerator as bg


#Class for generating the source code in Structured Text
class ST(bg.BaseGen):

    def __init__(self,destPath):
        self.destPath = destPath
        self.version = 'V0.9.0'

    def _writeHeader(self,function_name):
        now = datetime.now()

        try:
            with open(self.destPath + function_name + '.st','wt') as f:
                f.write('//***********************************************\n')
                f.write('// Codegenerator BuR ' + self.version + '\n')
                f.write('// by ' + conf['Author'] + '\n')
                f.write('// ' + conf['URL'] + '\n')
                f.write('// ' + conf['Email'] + '\n')
                f.write('// Date of generation: {0}\n'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write('//***********************************************\n')
                f.write('\n')
        except Exception as e:
            logging.error("Error openinng " + self.destPath + function_name + '.st',exc_info=True)

    #Create the source file for the function calls
    def writeInstances(self,instances):
        values = instances.values
        keys = instances.keys()
        function_name = values[0]
        lstValues = []
        lstVar = []

        #Create Header
        ST._writeHeader(self,function_name[1])

        try:
            #File.st
            with open(self.destPath + '/' + function_name[1] + '.st','a+') as f:
                for val in values:
                    lstValues.append(val)

                for lstitems in lstValues:
                    lst = lstitems
                    f.write('//***********************************************\n')
                    f.write('// ' + lst[2] + ' ' + lst[3] + '\n')
                    f.write('//***********************************************\n')

                    f.write(lst[0] + '(' + '\n')

                    for cnt, items in enumerate(lst):
                        lstitems = items
                        #Colum Offset for Parameters
                        if cnt > 3 and cnt < (len(lst) - 1):
                            f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ',' + '\n')
                        elif cnt >= (len(lst)- 1):
                            f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ');' + '\n')

                    f.write('\n')


            #File.var
            with open(self.destPath + '/' + function_name[1] + '.var','wt') as f:
                for val in values:
                    lstVar.append(val)

                f.write('VAR' + '\n')
                for lstitems in lstVar:
                    lst = lstitems
                    f.write(lst[0] + ' : ' + lst[1] + '; ' + '(*' + lst[2] + '*)' + '\n' )

                f.write('END_VAR')

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + function_name[1] + '.st',exc_info=True)

        return function_name[1]

    #types.typ
    def writeTypes(self,function_name, ctrl, sts, prm):
        ctrl_values = ctrl.values
        sts_values = sts.values
        prm_values = prm.values
        lst_ctrl_values = []
        lst_sts_values = []
        lst_prm_values = []

        for val in ctrl_values:
            lst_ctrl_values.append(val)

        for val in sts_values:
            lst_sts_values.append(val)

        for val in prm_values:
            lst_prm_values.append(val)

        try:
            # File.typ
            with open(self.destPath + '/' + function_name + '.typ', 'wt') as f:
    
                f.write('TYPE' + '\n')
                f.write('TYP_' + function_name + ' : ' + 'STRUCT' + '\n')
                f.write('CTRL' + ' : ' + function_name + '_CTRL;' + '\n')
                f.write('STS' + ' : ' + function_name + '_STS;' + '\n')
                f.write('PRM' + ' : ' + function_name + '_PRM;' + '\n')
                f.write('END_STRUCT;' + '\n')
                f.write('\n')
    
                #Generate ctrl type
                f.write(function_name + '_CTRL' + ' : ' + 'STRUCT' + '\n')
                for lstitems in lst_ctrl_values:
                    lst_ctrl = lstitems
                    f.write(lst_ctrl[0] + ' : ' + lst_ctrl[1] + '; ' + '(*' + lst_ctrl[2] + '*)' + '\n')
                f.write('END_STRUCT;' + '\n')
                f.write('\n')
    
                #Generate sts type
                f.write(function_name + '_STS' + ' : ' + 'STRUCT' + '\n')
                for lstitems in lst_sts_values:
                    lst_sts = lstitems
                    f.write(lst_sts[0] + ' : ' + lst_sts[1] + '; ' + '(*' + lst_sts[2] + '*)' + '\n')
                f.write('END_STRUCT;' + '\n')
                f.write('\n')
    
                #Generate prm type
                f.write(function_name + '_PRM' + ' : ' + 'STRUCT' + '\n')
                for lstitems in lst_prm_values:
                    lst_prm = lstitems
                    f.write(lst_prm[0] + ' : ' + lst_prm[1] + '; ' + '(*' + lst_prm[2] + '*)' + '\n')
                f.write('END_STRUCT;' + '\n')
                f.write('\n')
                f.write('END_TYPE' + '\n')
        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + function_name + '.typ',exc_info=True)

    #fb_lib.st
    def writeFB(self,function_name, var_input, var_output, var_in_out, author='user', version='V0.9.0' ):
        now = datetime.now()
        var_input_values = var_input.values
        var_output_values = var_output.values
        var_in_out_values = var_in_out.values
        lst_var_input_values = []
        lst_var_output_values = []
        lst_var_in_out_values = []

        for values in var_input_values:
            lst_var_input_values.append(values)

        for values in var_output_values:
            lst_var_output_values.append(values)

        for values in var_in_out_values:
            lst_var_in_out_values.append(values)

        try:
            # File.typ
            with open(self.destPath + '/' + function_name + '_lib' + '.st', 'wt') as f:
                f.write('//***********************************************\n')
                f.write('// ' + function_name  + '\n')
                f.write('// Author: ' + author + '\n')
                f.write('// Version: ' + version + '\n')
                f.write('// Date: {0}\n'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write('// Description: ' + '\n')
                f.write('// ' + '\n')
                f.write('// Interface: ' + '\n')

                #write input interface
                f.write('// VAR_INPUT:' + '\n')
                for items in lst_var_input_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + '\n')
                f.write('// ' + '\n')

                #write output interface
                f.write('// VAR_OUTPUT:' + '\n')
                for items in lst_var_output_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + '\n')
                f.write('// ' + '\n')

                #write in_out interface
                f.write('// VAR_IN_OUT:' + '\n')
                for items in lst_var_in_out_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + '\n')

                f.write('// ' + '\n')
                f.write('// Rev: ' + '\n')
                f.write('// ' + '\n')
                f.write('//***********************************************\n')
                f.write('\n')

                f.write('FUNCTION_BLOCK' + ' ' + function_name + '\n')



                f.write('\n')
                f.write('// TODO - Insert Code here' + '\n')
                f.write('\n')
                f.write('END_FUNCTION_BLOCK')
        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + function_name + '_lib' + '.st',exc_info=True)


    #lib.fun
    def writeInterface(self,function_name, var_input, var_output, var_in_out):
        var_input_values = var_input.values
        var_output_values = var_output.values
        var_in_out_values = var_in_out.values
        lst_var_input_values = []
        lst_var_output_values = []
        lst_var_in_out_values = []

        for val in var_input_values:
            lst_var_input_values.append(val)

        for val in var_output_values:
            lst_var_output_values.append(val)

        for val in var_in_out_values:
            lst_var_in_out_values.append(val)

        try:
            # File.typ
            with open(self.destPath + '/' + function_name + '.fun', 'wt') as f:

                f.write('FUNCTION_BLOCK' + ' ' + function_name +  '\n')

                # Generate var_input
                f.write('VAR_INPUT' '\n')
                for lstitems in var_input_values:
                    lst_var_input = lstitems
                    f.write(lst_var_input[0] + ' : ' + lst_var_input[1] + '; ' + '(*' + lst_var_input[2] + '*)' + '\n')
                f.write('END_VAR' + '\n')

                # Generate var_output
                f.write('VAR_OUTPUT' '\n')
                for lstitems in lst_var_output_values:
                    lst_var_output = lstitems
                    f.write(lst_var_output[0] + ' : ' + lst_var_output[1] + '; ' + '(*' + lst_var_output[2] + '*)' + '\n')
                f.write('END_VAR' + '\n')

                # Generate var_output
                f.write('VAR_IN_OUT' '\n')
                for lstitems in lst_var_in_out_values:
                    lst_var_in_out = lstitems
                    f.write(lst_var_in_out[0] + ' : ' + lst_var_in_out[1] + '; ' + '(*' + lst_var_in_out[2] + '*)' + '\n')
                f.write('END_VAR' + '\n')

                f.write('END_FUNCTION_BLOCK')

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + function_name + '.fun', exc_info=True)

class CPP:

    def __init__(self,destPath):
        self.destPath = destPath
        pass

    def development(self):
        print('CPP Generator was in Development')