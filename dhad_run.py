import os
import argparse

from dhad_lexer import dhad_lexer
from dhad_parser import dhad_parser
from dhad_interpreter import DhadInterpreter

def read_dhad_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        code = file.read()
    return code

def read_dhad_directory(directory):
    dhad_files = []
    for filename in os.listdir(directory):
        if filename.endswith('.ض'):
            file_path = os.path.join(directory, filename)
            dhad_files.append(file_path)
    return dhad_files

def run_dhad_code(code):
    # Lexical analysis (tokenization)
    tokens = dhad_lexer(code)
    
    # Parsing
    ast = dhad_parser(tokens)
    
    # Interpretation
    interpreter = DhadInterpreter()
    interpreter.interpret(ast)

def main():
    parser = argparse.ArgumentParser(description='Dhad Language Interpreter CLI')
    parser.add_argument('path', metavar='path', type=str, help='Path to .ض file or directory of .ض files')
    
    args = parser.parse_args()
    path = args.path
    
    if os.path.isfile(path):
        # Single file provided
        code = read_dhad_file(path)
        run_dhad_code(code)
    elif os.path.isdir(path):
        # Directory provided
        dhad_files = read_dhad_directory(path)
        for file in dhad_files:
            run_dhad_code(file)
    else:
        print(f"Error: {path} is not a valid file or directory")

if __name__ == "__main__":
    main()