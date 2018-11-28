"""
Generator for Siemens PLC
Author: dgrill
Date: 24 Nov 2018
"""
from CodeGenerator.conf.config import *
from datetime import datetime
import logging
from CodeGenerator.generators import BaseGenerator as bg


#Class for generating the source code in Structured Text
class ST(bg.BaseGen):

    def __init__(self, destPath, instances):
        #prepare function name
        values = instances.values
        temp_func_name = values[0]

        self.destPath = destPath
        self.function_name = temp_func_name[1]
        self.version = 'V0.9.0'

        ST._getInputs(self) #TEST


    #typ(UDT)
    def writeTyp(self, ctrl, sts, prm):
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
            with open(self.destPath + '/' + self.function_name + '.scl', 'wt') as f:


                # Generate ctrl type
                f.write('TYPE ' + '"' + self.function_name + '_CTRL' + '"' '\n')
                f.write('VERSION' + ' : ' + '1.0' + '\n')
                f.write('\t' + 'STRUCT' + '\n')
                for lstitems in lst_ctrl_values:
                    lst_ctrl = lstitems
                    f.write('\t' + '\t' + lst_ctrl[0] + ' : ' + lst_ctrl[1] + '; ' + '//' + lst_ctrl[2] + '\n')
                f.write('\t' + 'END_STRUCT;' + '\n')
                f.write('END_TYPE' + '\n')
                f.write('\n')

                # Generate sts type
                f.write('TYPE ' + '"' + self.function_name + '_STS' + '"' '\n')
                f.write('VERSION' + ' : ' + '1.0' + '\n')
                f.write('\t' + 'STRUCT' + '\n')
                for lstitems in lst_sts_values:
                    lst_sts = lstitems
                    f.write('\t' + '\t' + lst_sts[0] + ' : ' + lst_sts[1] + '; ' + '//' + lst_sts[2] + '\n')
                f.write('\t' + 'END_STRUCT;' + '\n')
                f.write('END_TYPE' + '\n')
                f.write('\n')

                # Generate prm type
                f.write('TYPE ' + '"' + self.function_name + '_STS' + '"' '\n')
                f.write('VERSION' + ' : ' + '1.0' + '\n')
                f.write('\t' + 'STRUCT' + '\n')
                for lstitems in lst_prm_values:
                    lst_prm = lstitems
                    f.write('\t' + '\t' + lst_prm[0] + ' : ' + lst_prm[1] + '; ' + '//' + lst_prm[2] + '\n')
                f.write('\t' + 'END_STRUCT;' + '\n')
                f.write('END_TYPE' + '\n')
                f.write('\n')

                # Generate type
                f.write('TYPE ' + '"' + 'TYP_' + self.function_name  + '"' '\n')
                f.write('VERSION' + ' : ' + '1.0' + '\n')
                f.write('\t' + 'STRUCT' + '\n')
                f.write('\t' + '\t' +'CTRL' + ' : ' + self.function_name + '_CTRL;' + '\n')
                f.write('\t' + '\t' +'STS' + ' : ' + self.function_name + '_STS;' + '\n')
                f.write('\t' + '\t' +'PRM' + ' : ' + self.function_name + '_PRM;' + '\n')
                f.write('\t' + 'END_STRUCT;' + '\n')
                f.write('END_TYPE' + '\n')
                f.write('\n')


        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.scl', exc_info=True)

    #FB
    def writeFB(self, var_input, var_output, var_in_out, author='user', version='V0.9.0' ):
        var_options = '{ ExternalAccessible := "False"; ExternalVisible := "False"; ExternalWritable := "False"}'
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
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:
                f.write('FUNCTION_BLOCK ' + '"' +  self.function_name + '"' + '\n')
                f.write('{ S7_Optimized_Access := "TRUE" }' + '\n')
                f.write('AUTHOR' + ' : ' + author + '\n')
                f.write('Version' + ' : ' + version + '\n')
                # write input interface
                f.write('\t'+ 'VAR_INPUT' + '\n')
                for items in lst_var_input_values:
                    f.write('\t' * 2 + items[0] + ' ' + var_options + ':' + '\t' + items[1]  + '\t' + '// ' + items[2] + '\n')
                f.write('\t'+ 'END_VAR' + '\n')

                # write output interface
                f.write('\t'+ 'VAR_OUTPUT' + '\n')
                for items in lst_var_output_values:
                    f.write('\t' * 2 + items[0] + ' ' + var_options + ':' + '\t' + items[1] + '\t' + '// ' + items[2] + '\n')
                f.write('\t'+ 'END_VAR' + '\n')

                # write in_out interface
                f.write('\t'+ 'VAR_IN_OUT' + '\n')
                for items in lst_var_in_out_values:
                    f.write('\t' * 2 + items[0] + ' ' + var_options + ':' + '\t' + items[1] + '\t' + '// ' + items[2] + '\n')
                f.write('\t'+ 'END_VAR' + '\n')

                f.write('BEGIN' + '\n')
                f.write('//***********************************************\n')
                f.write('// ' + self.function_name  + '\n')
                f.write('// Author: ' + author + '\n')
                f.write('// Version: ' + version + '\n')
                f.write('// Date: {0}\n'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write('// Description: ' + '\n')
                f.write('// ' + '\n')
                f.write('// Rev: ' + '\n')
                f.write('// ' + '\n')
                f.write('//***********************************************\n')

                f.write('\n')
                f.write('// TODO - Insert Code here' + '\n')
                f.write('\n')
                f.write('END_FUNCTION_BLOCK' + '\n')
                f.write('\n')
        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #DB
    def writeDB(self, instances, author='user', version='V0.9.0'):
        values = instances.values
        keys = instances.keys()
        function_name = values[0]
        lstValues = []
        lstVar = []

        try:
            # write DB
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:
                for val in values:
                    lstVar.append(val)

                f.write('DATA_BLOCK ' + '"' + 'DB_' + self.function_name + '"')
                f.write('{ S7_Optimized_Access := "TRUE" }' + '\n')
                f.write('AUTHOR' + ' : ' + author + '\n')
                f.write('Version' + ' : ' + version + '\n')
                f.write('VAR' + '\n')
                for lstitems in lstVar:
                    lst = lstitems
                    f.write('\t' + lst[0] + ' : ' + 'TYP_' + lst[1] + '; ' + '// ' + lst[2]  + '\n' )

                f.write('END_VAR' + '\n')
                f.write('BEGIN' + '\n')
                f.write('\n')
                f.write('END_DATA_BLOCK' + '\n')
                f.write('\n')
            

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #callFB
    def writeCall(self,instances, var_input, var_output, var_in_out, author='user', version='V0.9.0'):
        var_options = '{ ExternalAccessible := "False"; ExternalVisible := "False"; ExternalWritable := "False"}'
        values = instances.values
        keys = instances.keys()
        function_name = values[0]
        lstValues = []
        lstVar = []
        var_input_values = var_input.values
        var_output_values = var_output.values
        var_in_out_values = var_in_out.values
        lst_var_input_values = []
        lst_var_output_values = []
        lst_var_in_out_values = []
        var_output_sorted = []

        for valuesI in var_input_values:
            lst_var_input_values.append(valuesI)

        for valuesO in var_output_values:
            lst_var_output_values.append(valuesO)

        #get var_output datapoint by name
        for cnt_var_output, valuesOO in enumerate(lst_var_output_values):
            var_output_sorted.append (lst_var_output_values[cnt_var_output][0])


        for valuesIO in var_in_out_values:
            lst_var_in_out_values.append(valuesIO)

        try:
            #File.st
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:
                for val in values:
                    lstValues.append(val)

                f.write('FUNCTION_BLOCK ' + '"' +  self.function_name + '"' + '\n')
                f.write('{ S7_Optimized_Access := "TRUE" }' + '\n')
                f.write('AUTHOR' + ' : ' + author + '\n')
                f.write('Version' + ' : ' + version + '\n')
                f.write('VAR' + '\n')
                f.write('I_' + self.function_name + ' ' + var_options + ': ' + 'Array[0..' + str(values.shape[0]) + '] of ' + '"' + self.function_name + '";' + '\n' )
                f.write('END_VAR' + '\n')                
                f.write('BEGIN' + '\n' * 2)
                for cnt_,lstitems in enumerate(lstValues):
                    lst = lstitems
                    f.write('REGION ' + lst[2] + ' ' + lst[3] + '\n' * 2)

                    f.write('#' + 'I_' + self.function_name + '[' +  str(cnt_) + ']' + '(' + '\n')
                    for cnt, items in enumerate(lst):
                        lstitems = items
                        #Colum Offset for Parameters
                        if cnt > 3 and cnt < (len(lst) - 1):
                            # detect outputs
                            if keys[cnt] in var_output_sorted:
                                f.write('\t' + keys[cnt] + ' => ' + str(lstitems) + ',' + '\n')
                            else:
                                f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ',' + '\n')
                        elif cnt >= (len(lst) - 1):
                            f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ');' + '\n')

                    f.write('\n')
                    f.write('END_REGION ' + '\n')
                    f.write('\n')

                f.write('END_FUNCTION_BLOCK' + '\n')
                f.write('\n')

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)


class CPP:

    def __init__(self,destPath):
        self.destPath = destPath
        pass

    def development(self):
        print('Cpp was not supported on Siemens PLC')