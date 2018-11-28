from CodeGenerator.parser import Spreadsheet
from CodeGenerator.generators import Generator_BuR
from CodeGenerator.generators import Generator_SIE
import glob
import os
import json
from gooey import Gooey, GooeyParser
import logging

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',level=logging.INFO)

def code_gen(conf):

    print('DataDirectory: ',conf.data_directory);
    print('Output_directory: ',conf.output_directory);
    print('target_plc: ',conf.target_plc);
    print('target_lang: ',conf.target_lang);

    #read the structure from the excel file
    parseExcel = Spreadsheet.Structure(conf.data_directory)
    ctrl = parseExcel.readCtrl()
    sts = parseExcel.readSTS()
    prm = parseExcel.readPRM()
    var_input = parseExcel.readVarInput()
    var_output = parseExcel.readVarOutput()
    var_in_out = parseExcel.readVarInOut()
    instances = parseExcel.readInstances()

    # Choose the wright generator
    if conf.target_plc == 'BuR':

        generator_bur_st = Generator_BuR.ST(conf.output_directory)
        generator_bur_cpp = Generator_BuR.CPP(conf.output_directory)

        if conf.target_lang == 'ST':
            function_name = generator_bur_st.writeInstances(instances)
            generator_bur_st.writeTypes(function_name, ctrl, sts, prm)
            generator_bur_st.writeInterface(function_name,var_input,var_output,var_in_out)
            generator_bur_st.writeFB(function_name, var_input, var_output, var_in_out ,'dgrill','V1.0.0')
        elif  conf.target_lang == 'CPP':
            generator_bur_cpp.development()

    elif conf.target_plc == 'Siemens':

        generator_sie_st = Generator_SIE.ST(conf.output_directory, instances)
        generator_sie_cpp = Generator_SIE.CPP(conf.output_directory)

        if conf.target_lang == 'ST':
            generator_sie_st.writeTyp(ctrl, sts ,prm)
            generator_sie_st.writeFB(var_input,var_output,var_in_out,'dgrill','V1.0.0')
            generator_sie_st.writeDB(instances)
            generator_sie_st.writeCall(instances,var_input,var_output,var_in_out)
        elif  conf.target_lang == 'CPP':
            generator_sie_cpp.development()

def code_gen_TEST():

    parseExcel = Spreadsheet.Structure('/home/dgrill/Schreibtisch/Projects/00_CodeGenerator/data/structure.xlsx')
    ctrl = parseExcel.readCtrl()
    sts = parseExcel.readSTS()
    prm = parseExcel.readPRM()
    var_input = parseExcel.readVarInput()
    var_output = parseExcel.readVarOutput()
    var_in_out = parseExcel.readVarInOut()
    instances = parseExcel.readInstances()

    # BuR
    generator_bur_st = Generator_BuR.ST('/home/dgrill/Schreibtisch/Projects/00_CodeGenerator/data/')
    function_name = generator_bur_st.writeInstances(instances)
    generator_bur_st.writeTypes(function_name, ctrl, sts, prm)
    generator_bur_st.writeInterface(function_name,var_input,var_output,var_in_out)
    generator_bur_st.writeFB(function_name, var_input, var_output, var_in_out ,'dgrill','V1.0.0')

    #SIE
    generator_sie_st = Generator_SIE.ST('/home/dgrill/Schreibtisch/Projects/00_CodeGenerator/data/',instances)
    generator_sie_st.writeTyp(ctrl, sts ,prm)
    generator_sie_st.writeFB(var_input,var_output,var_in_out,'dgrill','V1.0.0')
    generator_sie_st.writeDB(instances)
    generator_sie_st.writeCall(instances,var_input,var_output,var_in_out)

@Gooey(advanced=True,
    show_config=True,
    default_size=(800,680),
    program_name="Code Generator")
def parse_args():
    """ Use GooeyParser to build up the arguments we will use in our script
    Save the arguments in a default json file so that we can retrieve them
    every time we run the script.
    """
    stored_args = {}
    # get the script name without the extension & use it to build up
    # the json filename
    script_name = os.path.splitext(os.path.basename(__file__))[0]
    args_file = "{}-args.json".format(script_name)

    # Read in the prior arguments as a dictionary
    if os.path.isfile(args_file):
        with open(args_file) as data_file:
            stored_args = json.load(data_file)

    parser = GooeyParser(description='V0.9.0 \n' + 'www.dgrill.at')

    parser.add_argument('data_directory',
                        action='store',
                        default=stored_args.get('data_directory'),
                        widget='FileChooser',
                        help="Source directory that contains structure.xlsx")

    parser.add_argument('output_directory',
                        action='store',
                        widget='DirChooser',
                        default=stored_args.get('output_directory'),
                        help="Output directory for the source files")

    parser.add_argument('target_plc',
                        choices= ['BuR', 'Siemens'],
                        widget='Dropdown',
                        default=stored_args.get('target_plc'),
                        help="Choose the target PLC")

    parser.add_argument('target_lang',
                        choices= ['ST', 'CPP'],
                        widget='Dropdown',
                        default=stored_args.get('target_lang'),
                        help="Choose the target language")

    parser.add_argument('target_ide',
                        choices= ['AS4.x', 'TIA_V15'],
                        widget='Dropdown',
                        default=stored_args.get('target_ide'),
                        help="Choose the target IDE Version")

    parser.add_argument('create_type',
                        action='store_true',
                        default=stored_args.get('target_ide'),
                        help="TYPES")


    args = parser.parse_args()
    # Store the values of the arguments so we have them next time we run
    with open(args_file, 'w') as data_file:
        # Using vars(args) returns the data as a dictionary
        json.dump(vars(args), data_file)
    return args

if __name__ == '__main__':
    #conf = parse_args()
    #code_gen(conf)
    code_gen_TEST()

