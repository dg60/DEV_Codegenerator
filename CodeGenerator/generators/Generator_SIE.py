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
        self.s7_opt_access = "{ S7_Optimized_Access := 'TRUE' }"
        self.var_options = "{ ExternalAccessible := 'False'; ExternalVisible := 'False'; ExternalWritable := 'False'}"

    def _writeTypStart(self,f):
        f.write(syn.Scl['s_type'] + '"' + self.function_name + '_CTRL' + '"' + self.nl)
        f.write('VERSION' + syn.Scl[':'] + '1.0' + self.nl)
        f.write('\t' + syn.Scl['s_struct'] + self.nl)

    def _writeTypEnd(self,f):
        f.write('\t' + syn.Scl['e_struct'] + self.nl)
        f.write(syn.Scl['e_type'] + self.nl)
        f.write(self.nl)

    def _writeHeader(self,f):
        now = datetime.now()

        f.write('//***********************************************' + self.nl)
        f.write('// Codegenerator Siemens ' + conf['Version'] + self.nl)
        f.write('// by ' + conf['Author'] + self.nl)
        f.write('// ' + conf['URL'] + self.nl)
        f.write('// ' + conf['Email'] + self.nl)
        f.write('// Date of generation: {0}'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
        f.write(self.nl)
        f.write('//***********************************************' + self.nl)
        f.write(self.nl)

    #typ(UDT)
    def writeTyp(self, ctrl, sts, prm):
        lst_ctrl_values = ST._readValues(self,ctrl)
        lst_sts_values = ST._readValues(self,sts)
        lst_prm_values = ST._readValues(self,prm)

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
    def writeFB(self, var_input, var_output, var_in_out, author='user', version='1.0' ):
        now = datetime.now()
        lst_var_input_values = ST._readValues(self,var_input)
        lst_var_output_values = ST._readValues(self,var_output)
        lst_var_in_out_values = ST._readValues(self,var_in_out)


        try:
            # File.typ
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:

                f.write(syn.Scl['s_fb'] + '"' +  self.function_name + '"' + self.nl)
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)

                # write input interface
                f.write('\t'+ syn.Scl['var_input'] + self.nl)
                for items in lst_var_input_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + syn.Scl[':'] + '\t' + items[1] + syn.Scl[';']  + '\t' + syn.Scl['comment'] + items[2] + self.nl)
                f.write('\t'+ syn.Scl['end_var'] + self.nl)

                # write output interface
                f.write('\t'+ syn.Scl['var_output'] + self.nl)
                for items in lst_var_output_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + syn.Scl[':'] + '\t' + items[1] + syn.Scl[';'] + '\t' + syn.Scl['comment'] + items[2] + self.nl)
                f.write('\t'+ syn.Scl['end_var'] + self.nl)

                # write in_out interface
                f.write('\t'+ syn.Scl['var_in_out'] + self.nl)
                for items in lst_var_in_out_values:
                    f.write('\t' * 2 + items[0] + ' ' + self.var_options + syn.Scl[':'] + '\t' + items[1] + syn.Scl[';'] + '\t' + syn.Scl['comment'] + items[2] + self.nl)
                f.write('\t'+ syn.Scl['end_var'] + self.nl)

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
                f.write(syn.Scl['e_fb'] + self.nl)
                f.write(self.nl)

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #DB
    def writeDB(self, instances, author='user', version='1.0'):
        values = instances.values
        lstVar = []

        try:
            # write DB
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:

                for val in values:
                    lstVar.append(val)

                f.write(syn.Scl['s_data_block'] + '"' + 'DB_' + self.function_name + '"')
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)
                f.write('VAR' + self.nl)

                for lstitems in lstVar:
                    lst = lstitems
                    f.write('\t' + '"' + lst[0] + '"' + syn.Scl[':'] + '"' + 'TYP_' + lst[1] + '"' + syn.Scl[';'] + '// ' + lst[2]  + self.nl )

                f.write(syn.Scl['end_var'] + self.nl)
                f.write('BEGIN' + self.nl)
                f.write(self.nl)
                f.write(syn.Scl['e_data_block'] + self.nl)
                f.write(self.nl)
            

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)

    #callFB
    def writeCall(self,instances, var_input, var_output, var_in_out, author='user', version='1.0'):
        values = instances.values
        keys = instances.keys()
        lstValues = []
        lst_var_input_values = ST._readValues(self,var_input)
        lst_var_output_values = ST._readValues(self,var_output)
        lst_var_in_out_values = ST._readValues(self,var_in_out)
        var_output_sorted = []

        #get var_output datapoint by name
        for cnt_var_output in range(len(lst_var_output_values)):
            var_output_sorted.append (lst_var_output_values[cnt_var_output][0])

        try:
            #File.st
            with open(self.destPath + '/' + self.function_name + '.scl', 'a+') as f:
                for val in values:
                    lstValues.append(val)

                f.write(syn.Scl['s_fb'] + '"' + 'Call_' + self.function_name + '"' + self.nl)
                f.write(self.s7_opt_access + self.nl)
                f.write('AUTHOR' + syn.Scl[':'] + author + self.nl)
                f.write('Version' + syn.Scl[':'] + version + self.nl)
                f.write(syn.Scl['var'] + self.nl)
                f.write('I_' + self.function_name + ' ' + self.var_options + ': ' + 'Array[0..' + str(values.shape[0]) + '] of ' + '"' + self.function_name + '";' + self.nl )
                f.write(syn.Scl['end_var'] + self.nl)
                f.write('BEGIN' + self.nl * 2)

                ST._writeHeader(self,f)

                for cnt_,lstitems in enumerate(lstValues):

                    lst = lstitems
                    f.write(syn.Scl['region'] + lst[2] + ' ' + lst[3] + self.nl * 2)
                    f.write('#' + 'I_' + self.function_name + '[' +  str(cnt_) + ']' + '(' + self.nl)

                    for cnt, items in enumerate(lst):
                        lstitems = items
                        #Colum Offset for Parameters
                        if cnt > 3 and cnt < (len(lst) - 1):
                            # detect outputs
                            if keys[cnt] in var_output_sorted:
                                f.write('\t' + keys[cnt] + syn.Scl['=>'] + str(lstitems) + ',' + self.nl)
                            else:
                                f.write('\t' + keys[cnt] + syn.Scl[':='] + str(lstitems) + ',' + self.nl)

                        elif cnt >= (len(lst) - 1):
                            f.write('\t' + keys[cnt] + syn.Scl[':='] + str(lstitems) + ');' + self.nl)

                    f.write(self.nl)
                    f.write(syn.Scl['e_region'] + self.nl)
                    f.write(self.nl)

                f.write(syn.Scl['e_fb'] + self.nl)
                f.write(self.nl)

        except Exception as e:
            logging.error(self.destPath + '/' + self.function_name + '.scl',exc_info=True)


class CPP:

    def __init__(self,destPath):
        self.destPath = destPath
        pass

    def development(self):
        print('Cpp was not supported on Siemens PLC')