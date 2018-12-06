"""
Generator for Siemens PLC
Author: dgrill
Date: 24 Nov 2018
"""
from CodeGenerator.conf.config import *
from datetime import datetime
import logging
from CodeGenerator.generators import BaseGenerator as bg
from CodeGenerator.generators.Syntax import Syntax as syn


#Class for generating the source code in Scl
class ST(bg.BaseGen):

    def __init__(self, destPath, instances):
        #prepare function name
        values = instances.values
        temp_func_name = values[0]
        self.nl = '\r\n'
        self.destPath = destPath
        self.function_name = temp_func_name[1]
        self.version = 'V0.9.0'
        self.s7_opt_access = '{ S7_Optimized_Access := "TRUE" }'
        self.var_options = "{ ExternalAccessible := 'False'; ExternalVisible := 'False'; ExternalWritable := 'False'}"

    def _writeTypStart(self,f):
        f.write(syn.Scl['s_type'] + '"' + self.function_name + '_CTRL' + '"' + self.nl)
        f.write('VERSION' + syn.Scl[':'] + '1.0' + self.nl)
        f.write('\t' + syn.Scl['s_struct'] + self.nl)

    def _writeTypEnd(self,f):
        f.write('\t' + syn.Scl['e_struct'] + self.nl)
        f.write(syn.Scl['e_type'] + self.nl)
        f.write(self.nl)


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
                ST._writeTypStart(self, f)
                for lstitems in lst_ctrl_values:
                    lst_ctrl = lstitems
                    f.write('\t' + '\t' + lst_ctrl[0] + syn.Scl[':'] + lst_ctrl[1] + syn.Scl[';'] + syn.Scl['comment'] + lst_ctrl[2] + self.nl)
                ST._writeTypEnd(self, f)

                # Generate sts type
                ST._writeTypStart(self, f)
                for lstitems in lst_sts_values:
                    lst_sts = lstitems
                    f.write('\t' + '\t' + lst_sts[0] + syn.Scl[':'] + lst_sts[1] + syn.Scl[';'] + syn.Scl['comment'] + lst_sts[2] + self.nl)
                ST._writeTypEnd(self, f)

                # Generate prm type
                ST._writeTypStart(self, f)
                for lstitems in lst_prm_values:
                    lst_prm = lstitems
                    f.write('\t' + '\t' + lst_prm[0] + syn.Scl[':'] + lst_prm[1] + syn.Scl[';'] + syn.Scl['comment'] + lst_prm[2] + self.nl)
                ST._writeTypEnd(self, f)

                # Generate type
                f.write(syn.Scl['s_type'] + '"' + 'TYP_' + self.function_name  + '"' + self.nl)
                f.write('VERSION' + syn.Scl[':'] + '1.0' + self.nl)
                f.write('\t' + syn.Scl['s_struct'] + self.nl)
                f.write('\t' + '\t' +'CTRL' + syn.Scl[':'] + self.function_name + '_CTRL;' + self.nl)
                f.write('\t' + '\t' +'STS' + syn.Scl[':'] + self.function_name + '_STS;' + self.nl)
                f.write('\t' + '\t' +'PRM' + syn.Scl[':'] + self.function_name + '_PRM;' + self.nl)
                f.write('\t' + syn.Scl['e_struct'] + self.nl)
                f.write(syn.Scl['e_type'] + self.nl)
                f.write(self.nl)


        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.scl', exc_info=True)

    #FB
    def writeFB(self, var_input, var_output, var_in_out, author='user', version='0.9' ):
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
                f.write('FUNCTION_BLOCK ' + '"' +  self.function_name + '"' + self.nl)
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)
                # write input interface
                f.write('\t'+ 'VAR_INPUT' + self.nl)
                for items in lst_var_input_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + ':' + '\t' + items[1] + ';'  + '\t' + '// ' + items[2] + self.nl)
                f.write('\t'+ 'END_VAR' + self.nl)

                # write output interface
                f.write('\t'+ 'VAR_OUTPUT' + self.nl)
                for items in lst_var_output_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + ':' + '\t' + items[1] + ';' + '\t' + '// ' + items[2] + self.nl)
                f.write('\t'+ 'END_VAR' + self.nl)

                # write in_out interface
                f.write('\t'+ 'VAR_IN_OUT' + self.nl)
                for items in lst_var_in_out_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + ':' + '\t' + items[1] + ';' + '\t' + '// ' + items[2] + self.nl)
                f.write('\t'+ 'END_VAR' + self.nl)

                f.write('BEGIN' + self.nl)
                f.write('//***********************************************\n')
                f.write('// ' + self.function_name  + self.nl)
                f.write('// Author: ' + author + self.nl)
                f.write('// Version: ' + version + self.nl)
                f.write('// Date: {0}\n'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write('// Description: ' + self.nl)
                f.write('// ' + self.nl)
                f.write('// Rev: ' + self.nl)
                f.write('// ' + self.nl)
                f.write('//***********************************************\n')

                f.write(self.nl)
                f.write('// TODO - Insert Code here' + self.nl)
                f.write(self.nl)
                f.write('END_FUNCTION_BLOCK' + self.nl)
                f.write(self.nl)
        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #DB
    def writeDB(self, instances, author='user', version='0.9'):
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
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)
                f.write('VAR' + self.nl)

                for lstitems in lstVar:
                    lst = lstitems
                    f.write('\t' + '"' + lst[0] + '"' + syn.Scl[':'] + '"' + 'TYP_' + lst[1] + '"' + syn.Scl[';'] + '// ' + lst[2]  + self.nl )

                f.write('END_VAR' + self.nl)
                f.write('BEGIN' + self.nl)
                f.write(self.nl)
                f.write('END_DATA_BLOCK' + self.nl)
                f.write(self.nl)
            

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #callFB
    def writeCall(self,instances, var_input, var_output, var_in_out, author='user', version='0.9'):
        var_options = "{ ExternalAccessible := 'False'; ExternalVisible := 'False'; ExternalWritable := 'False'}"
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

                f.write('FUNCTION_BLOCK ' + '"' + 'Call_' + self.function_name + '"' + self.nl)
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)
                f.write('VAR' + self.nl)
                f.write('I_' + self.function_name + ' ' + var_options + ': ' + 'Array[0..' + str(values.shape[0]) + '] of ' + '"' + self.function_name + '";' + self.nl )
                f.write('END_VAR' + self.nl)                
                f.write('BEGIN' + self.nl * 2)
                for cnt_,lstitems in enumerate(lstValues):
                    lst = lstitems
                    f.write('REGION ' + lst[2] + ' ' + lst[3] + self.nl * 2)

                    f.write('#' + 'I_' + self.function_name + '[' +  str(cnt_) + ']' + '(' + self.nl)
                    for cnt, items in enumerate(lst):
                        lstitems = items
                        #Colum Offset for Parameters
                        if cnt > 3 and cnt < (len(lst) - 1):
                            # detect outputs
                            if keys[cnt] in var_output_sorted:
                                f.write('\t' + keys[cnt] + ' => ' + str(lstitems) + ',' + self.nl)
                            else:
                                f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ',' + self.nl)
                        elif cnt >= (len(lst) - 1):
                            f.write('\t' + keys[cnt] + ' := ' + str(lstitems) + ');' + self.nl)

                    f.write(self.nl)
                    f.write('END_REGION ' + self.nl)
                    f.write(self.nl)

                f.write('END_FUNCTION_BLOCK' + self.nl)
                f.write(self.nl)

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)


class CPP:

    def __init__(self,destPath):
        self.destPath = destPath
        pass

    def development(self):
        print('Cpp was not supported on Siemens PLC')