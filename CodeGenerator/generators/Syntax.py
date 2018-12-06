"""
Class for syntax snippets
Author: dgrill
Date: 06 Dez 2018
"""

class Syntax():

    # Structured Text (BuR)
    St = {
        'comment': '//',
        ':': ' : ',
        ';': '; ',
        ':=': ':= ',
        'var_input': 'VAR_INPUT',
        'var_output': 'VAR_OUTPUT',
        'var_in_out': 'VAR_IN_OUT',
        'end_var': 'END_VAR',
        's_type': 'TYPE',
        'e_type': 'END_TYPE',
        's_struct': 'STRUCT',
        'e_struct': 'END_STRUCT;',
        's_fc': 'FUNCTION',
        'e_fc': 'END_FUNCTION',
        's_fb': 'FUNCTION_BLOCK ',
        'e_fb': 'END_FUNCTION_BLOCK'
    }
    # Scl (SIE)
    Scl = {
        'comment': '//',
        ':': ' : ',
        ';': '; ',
        ':=': ':= ',
        '=>': '=>',
        'var_input': 'VAR_INPUT',
        'var_output': 'VAR_OUTPUT',
        'var_in_out': 'VAR_IN_OUT',
        'end_var': 'END_VAR',
        's_type': 'TYPE ',
        'e_type': 'END_TYPE',
        's_struct': 'STRUCT',
        'e_struct': 'END_STRUCT;',
        's_fc': 'FUNCTION',
        'e_fc': 'END_FUNCTION',
        's_fb': 'FUNCTION_BLOCK ',
        'e_fb': 'END_FUNCTION_BLOCK',
        's_data_block': 'DATA_BLOCK',
        'e_data_block': 'END_DATA_BLOCK',
        'region': 'REGION',
        'e_region': 'END_REGION',
    }
    # C++ (BuR)
    Cpp = {
        'comment': '//',
        ';': ';',
        '=': '=',
        's_block_comment': '/*',
        'e_block_comment': '*/',
    }

print(Syntax.St)

