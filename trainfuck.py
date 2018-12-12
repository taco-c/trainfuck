#!/usr/bin/env python3

""" Trainfuck.
    
    Usage: trainfuck.py <filename> """

""" The meat of Trainfuck. """
def interpret (code):
    code = prepare_code(code)
    cells, cell_ptr, code_ptr = [0], 0, 0
    loops = prepare_loops(code)
    
    while code_ptr < len(code):
        key, value = code[code_ptr]
        
        if key == "+":
            cells[cell_ptr] = cells[cell_ptr] + value
            
            if cells[cell_ptr] > 255:
                cells[cell_ptr] = cells[cell_ptr] - 256
        
        elif key == "-":
            cells[cell_ptr] = cells[cell_ptr] - value
            
            if cells[cell_ptr] < 0:
                cells[cell_ptr] = 256 + cells[cell_ptr]
        
        elif key == ">":
            cell_ptr += value
            
            if cell_ptr == len(cells):
                cells.append(0)
        
        elif key == "<":
            cell_ptr = cell_ptr - value if cell_ptr - value > 0 else 0
        
        elif key == ".":
            for i in range(value):
                print(chr(cells[cell_ptr]), end="")
        
        elif key == ":":
            for i in range(value):
                print(cells[cell_ptr], end="")
        
        elif key == "[":
            if cells[cell_ptr] == 0:
                code_ptr = loops[code_ptr]
                continue
        
        elif key == "]":
            if cells[cell_ptr] != 0:
                code_ptr = loops[code_ptr]
                continue

        code_ptr += 1

""" This function writes down the location of all the loops (both the start
    and the end) in the train-/brainfuck file. And then returns his notebook
    to the place that asked for it. This is a good boy. """
def prepare_loops (code):
    loop_starts = []
    loops = {}
    i = 0
    
    for key, value in code:
        if key == "[":
            loop_starts.append(i)
        
        elif key == "]":
            if loop_starts == []:
                print("Error at {}:'{}', no matching [.".format(i, key))
                exit(1)
            
            start = loop_starts.pop()
            loops[i] = start
            loops[start] = i
        
        i += 1
    
    return loops

""" Trainfuck is picky about its inputs. This function strips off all
    non-essential characters, and returns a list of tuples. """
def prepare_code (code_str):
    SYMBOLS = ["+", "-", ">", "<", ".", ":", "[", "]"]
    NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    prepared_code = []
    code = "".join([x for x in code_str if x in SYMBOLS + NUMBERS])
    
    i = 0
    
    while True:
        if i >= len(code):
            break
        
        value = ""
        j = i + 1
        
        if j >= len(code):
            prepared_code.append((code[i], 1))
            i += 1
            
            continue
        
        if code[j] in SYMBOLS:
            prepared_code.append((code[i], 1))
            i += 1
            
            continue
        
        while code[j] in NUMBERS:
            value += code[j]
            j += 1
            if j >= len(code):
                break
        
        if value != "":
            prepared_code.append((code[i], int(value)))
        
        i += j - i
        
    return prepared_code

""" This comment is here to visually separate the above function from 
    this thing. """
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage:", sys.argv[0], "<filename>")
        exit(1)
    
    try:
        with open(sys.argv[1]) as f:
            code = f.read()
    
    except IOError as e:
        print(e)
        exit(1)
    
    interpret(code)
