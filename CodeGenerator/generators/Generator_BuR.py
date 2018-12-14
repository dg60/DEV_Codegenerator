"""
Generator for BuR PLC
Author: dgrill
Date: 17 Nov 2018
"""
from CodeGenerator.conf.config import *
from datetime import datetime
import logging
from CodeGenerator.generators import BaseGenerator as bg
from CodeGenerator.generators.Syntax import Syntax as syn


#Class for generating the source code in Structured Text
class ST(bg.BaseGen):

    def __init__(self,destPath, instances):
        #prepare function name
        values = instances.values
        temp_func_name = values[0]
        self.nl = '\r\n'
        self.destPath = destPath
        self.function_name = temp_func_name[1]
        self.version = 'V1.0'

    def _writeHeader(self):
        now = datetime.now()

        try:
            with open(self.destPath + '/' + self.function_name + '.st','wt') as f:
                f.write('//***********************************************' + self.nl)
                f.write('// Codegenerator BuR ' + conf['Version'] + self.nl)
                f.write('// by ' + conf['Author'] + self.nl)
                f.write('// ' + conf['URL'] + self.nl)
                f.write('// ' + conf['Email'] + self.nl)
                f.write('// Date of generation: {0}'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write(self.nl)
                f.write('//***********************************************' + self.nl)
                f.write(self.nl)

        except Exception as e:
            logging.error("Error openinng " + self.destPath + self.function_name + '.st',exc_info=True)


    #Create the source file for the function calls
    def writeInstances(self,instances, var_input, var_output, var_in_out,):
        values = instances.values
        keys = instances.keys()
        lst_var_input_values = ST._readValues(self,var_input)
        lst_var_output_values = ST._readValues(self,var_output)
        lst_var_in_out_values = ST._readValues(self,var_in_out)
        lstValues = []
        lstVar = []
        var_output_sorted = []
        tmp_lst_var_output =[]

        #get var_output datapoint by name
        for cnt_var_output in range(len(lst_var_output_values)):
            var_output_sorted.append (lst_var_output_values[cnt_var_output][0])

        #Create Header
        ST._writeHeader(self)

        try:
            #File.st
            with open(self.destPath + '/' + self.function_name + '.st','a+') as f:
                for val in values:
                    lstValues.append(val)

                for lstitems in lstValues:
                    lst = lstitems
                    f.write('//***********************************************' + self.nl)
                    f.write('// ' + lst[2] + ' ' + lst[3] + self.nl)
                    f.write('//***********************************************' + self.nl)
                    f.write(self.nl)

                    f.write(lst[0] + '(' + self.nl)

                    for cnt, items in enumerate(lst):
                        lstitems = items

                        # Colum Offset for Parameters
                        if cnt > 3 and cnt < (len(lst) - 1):
                            #detect outputs
                            if keys[cnt] in var_output_sorted:
                                tmp_lst_var_output.append('\t' + str(lstitems) + syn.St[':='] + lst[0] + '.' + keys[cnt] + syn.St[';'] + self.nl)
                            else:
                                f.write('\t' + keys[cnt] + syn.St[':='] + str(lstitems) + ',' + self.nl)

                        elif cnt >= (len(lst)- 1):
                            f.write('\t' + keys[cnt] + syn.St[':='] + str(lstitems) + ');' + self.nl)
                            f.write(self.nl)

                    # write output interface
                    for line_out in tmp_lst_var_output:
                        f.write(line_out)
                    tmp_lst_var_output = []

                    f.write(self.nl)

            #File.var
            with open(self.destPath + '/' + self.function_name + '.var','wt') as f:

                for val in values:
                    lstVar.append(val)

                f.write(syn.St['var'] + self.nl)
                for lstitems in lstVar:
                    lst = lstitems
                    f.write(lst[0] + ' : ' + lst[1] + syn.St[';'] + syn.St['s_block_comment'] + lst[2] + syn.St['e_block_comment'] + self.nl )

                f.write(syn.St['end_var'])

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.st',exc_info=True)


    #types.typ
    def writeTypes(self, ctrl, sts, prm):
        lst_ctrl_values = ST._readValues(self,ctrl)
        lst_sts_values = ST._readValues(self,sts)
        lst_prm_values = ST._readValues(self,prm)

        try:
            # File.typ
            with open(self.destPath + '/' + self.function_name + '.typ', 'wt') as f:
    
                f.write(syn.St['s_type'] + self.nl)
                f.write('TYP_' + self.function_name + syn.St[':'] + syn.St['s_struct'] + self.nl)
                f.write('CTRL' + syn.St[':'] + self.function_name + '_CTRL;' + self.nl)
                f.write('STS' + syn.St[':'] + self.function_name + '_STS;' + self.nl)
                f.write('PRM' + syn.St[':'] + self.function_name + '_PRM;' + self.nl)
                f.write(syn.St['e_struct'] + self.nl)
                f.write(self.nl)
    
                #Generate ctrl type
                f.write(self.function_name + '_CTRL' + syn.St[':'] + syn.St['s_struct'] + self.nl)

                for lstitems in lst_ctrl_values:
                    lst_ctrl = lstitems
                    f.write(lst_ctrl[0] + syn.St[':'] + lst_ctrl[1] + syn.St[';'] + syn.St['s_block_comment'] + lst_ctrl[2] + syn.St['e_block_comment'] + self.nl)

                f.write(syn.St['e_struct'] + self.nl)
                f.write(self.nl)
    
                #Generate sts type
                f.write(self.function_name + '_STS' + syn.St[':'] + syn.St['s_struct'] + self.nl)

                for lstitems in lst_sts_values:
                    lst_sts = lstitems
                    f.write(lst_sts[0] + syn.St[':'] + lst_sts[1] + syn.St[';'] + syn.St['s_block_comment'] + lst_sts[2] + syn.St['e_block_comment'] + self.nl)

                f.write(syn.St['e_struct'] + self.nl)
                f.write(self.nl)
    
                #Generate prm type
                f.write(self.function_name + '_PRM' + syn.St[':'] + syn.St['s_struct'] + self.nl)

                for lstitems in lst_prm_values:
                    lst_prm = lstitems
                    f.write(lst_prm[0] + syn.St[':'] + lst_prm[1] + syn.St[';'] + syn.St['s_block_comment'] + lst_prm[2] + syn.St['e_block_comment'] + self.nl)

                f.write(syn.St['e_struct'] + self.nl)
                f.write(self.nl)

                f.write(syn.St['e_type'] + self.nl)

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.typ',exc_info=True)

    #fb_lib.st
    def writeFB(self, var_input, var_output, var_in_out, author='user', version='V1.0' ):
        now = datetime.now()
        lst_var_input_values = ST._readValues(self,var_input)
        lst_var_output_values = ST._readValues(self,var_output)
        lst_var_in_out_values = ST._readValues(self,var_in_out)

        try:
            # File.typ
            with open(self.destPath + '/' + self.function_name + '_lib' + '.st', 'wt') as f:
                f.write('//***********************************************' + self.nl)
                f.write('// ' + self.function_name  + self.nl)
                f.write('// Author: ' + author + self.nl)
                f.write('// Version: ' + version + self.nl)
                f.write('// Date: {0}'.format(str(now.strftime('%d.%m.%Y %H:%M'))))
                f.write(self.nl)
                f.write('// Description: ' + self.nl)
                f.write('// ' + self.nl)
                f.write('// Interface: ' + self.nl)

                #write input interface
                f.write('// VAR_INPUT:' + self.nl)
                for items in lst_var_input_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + self.nl)
                f.write('// ' + self.nl)

                #write output interface
                f.write('// VAR_OUTPUT:' + self.nl)
                for items in lst_var_output_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + self.nl)
                f.write('// ' + self.nl)

                #write in_out interface
                f.write('// VAR_IN_OUT:' + self.nl)
                for items in lst_var_in_out_values:
                    f.write('// ' + items[0] + ':' + '\t' + items[1] + '\t' + items[2] + self.nl)

                f.write('// ' + self.nl)
                f.write('// Rev: ' + self.nl)
                f.write('// ' + self.nl)
                f.write('//***********************************************' + self.nl)
                f.write(self.nl)

                f.write(syn.St['s_fb'] + ' ' + self.function_name + self.nl)

                f.write(self.nl)
                f.write('// TODO - Insert Code here' + self.nl)
                f.write(self.nl)
                f.write(syn.St['e_fb'])

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '_lib' + '.st',exc_info=True)

    #lib.fun
    def writeInterface(self, var_input, var_output, var_in_out):
        lst_var_input_values = ST._readValues(self,var_input)
        lst_var_output_values = ST._readValues(self,var_output)
        lst_var_in_out_values = ST._readValues(self,var_in_out)

        try:
            # File.typ
            with open(self.destPath + '/' + self.function_name + '.fun', 'wt') as f:

                f.write(syn.St['s_fb'] + ' ' + self.function_name +  self.nl)

                # Generate var_input
                f.write(syn.St['var_input'] + self.nl)
                for lstitems in lst_var_input_values:
                    lst_var_input = lstitems
                    f.write(lst_var_input[0] + ' : ' + lst_var_input[1] + '; ' + syn.St['s_block_comment'] + lst_var_input[2] + syn.St['e_block_comment'] + self.nl)
                f.write(syn.St['end_var'] + self.nl)

                # Generate var_output
                f.write(syn.St['var_output'] + self.nl)
                for lstitems in lst_var_output_values:
                    lst_var_output = lstitems
                    f.write(lst_var_output[0] + ' : ' + lst_var_output[1] + '; ' + syn.St['s_block_comment'] + lst_var_output[2] + syn.St['e_block_comment'] + self.nl)
                f.write(syn.St['end_var'] + self.nl)

                # Generate var_in_out
                f.write(syn.St['var_in_out'] + self.nl)
                for lstitems in lst_var_in_out_values:
                    lst_var_in_out = lstitems
                    f.write(lst_var_in_out[0] + ' : ' + lst_var_in_out[1] + '; ' + syn.St['s_block_comment'] + lst_var_in_out[2] + syn.St['e_block_comment'] + self.nl)
                f.write(syn.St['end_var'] + self.nl)

                f.write(syn.St['e_fb'])

        except Exception as e:
            logging.error("Error openinng " + self.destPath + '/' + self.function_name + '.fun', exc_info=True)

class CPP:

    def __init__(self,destPath,instances):
        self.destPath = destPath
        pass

    def development(self):
        print('CPP Generator was in Development')