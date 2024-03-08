def hex_to_bin(hex):
    bin = ""
    for c in hex:
        bin += hex_bin[c]
    return bin

def bin_to_hex(bin):
    hex = ""
    for i in range(0, len(bin), 4):
        temp = bin[i:i+4]
        ch = bin_hex[temp]
        hex += ch
    return hex

def length2(s):
    if s not in valid_opcodes:
        print("Invalid Instruction - Invalid Opcode")
        return False
    return True

def length4(s):
    opcode = s[:2]
    opcode = bin_to_hex(hex_to_bin(opcode)[:6] + "00")
    print("opcode is ",opcode)
    if opcode not in valid_opcodes:
        print("Invalid Instruction - Invalid Opcode")
        return False
    valid_reg = {'0','1','2','3','4','5'}
    reg1 = s[2]
    reg2 = s[3]
    if reg1 not in valid_reg:
        print("Invalid Instruction - Register 1 is not valid")
        return False
    if reg2 not in valid_reg:
        print("Invalid Instruction - Register 2 is not valid")
        return False
    return True

def length6(s):
    binary_rep = hex_to_bin(s)
    opcode = binary_rep[:8]
    opcode = bin_to_hex(opcode[:6] + "00")
    print("opcode is ",opcode)
    if opcode not in valid_opcodes:
        print("Invalid instruction - Invalid Opcode")
        return False
    flags = binary_rep[6:12]
    n = int(flags[0])
    i = int(flags[1])
    x = int(flags[2])
    b = int(flags[3])
    p = int(flags[4])
    e = int(flags[5])

    if e==1:
        print("Invalid instruction: e bit cannot be 1 in format 3 instruction")
        return False

    if b==1 and p==1:
        print("Invalid Instruction - Instruction cannot be both PC relative and Base addressing mode")
        return False
    
    if opcode in index_opcodes and x==0:
        print("Invalid Instruction - Index register should be 1")
    
    if opcode not in index_opcodes and x==1:
        print("Invalid Instruction - Index register should not be 1")

    
    return True

def length8(s):
    binary_rep = hex_to_bin(s)
    opcode = binary_rep[:8]
    opcode = bin_to_hex(opcode[:6] + "00")
    print("opcode is ",opcode)
    if opcode not in valid_opcodes:
        print("Invalid instruction - Invalid Opcode")
        return False
    flags = binary_rep[6:12]
    n = int(flags[0])
    i = int(flags[1])
    x = int(flags[2])
    b = int(flags[3])
    p = int(flags[4])
    e = int(flags[5])

    if e==0:
        print("Invalid instruction: e bit cannot be 0 in format 4 instruction")
        return False

    if b==1 and p==1:
        print("Invalid Instruction - Instruction cannot be both PC relative and Base addressing mode")
        return False

    if n==0 and i==0:
        print("Invalid Instruction - Invalid addressing mode, Both n and i bits cannot be 0")
        return False

    if opcode in index_opcodes and x==0:
        print("Invalid Instruction - Index register should be 1")
    
    if opcode not in index_opcodes and x==1:
        print("Invalid Instruction - Index register should not be 1")
    
    return True
    

if __name__ == "__main__":

    hex_bin = {
        '0': "0000", '1': "0001", '2': "0010", '3': "0011",
        '4': "0100", '5': "0101", '6': "0110", '7': "0111",
        '8': "1000", '9': "1001", 'A': "1010", 'B': "1011",
        'C': "1100", 'D': "1101", 'E': "1110", 'F': "1111"
    }

    bin_hex = {v: k for k, v in hex_bin.items()}

    valid_opcodes = {
        "C4", "C0", "F4", "C8", "F0", "F8", "90", "B4", "A0", "9C", "98", "AC", "A4", "A8", "94", "B0", "B8", 
        "18", "58", "40", "28", "88", "24", "64", "3C", "30", "34", "38", "48",
        "00", "68", "50", "70", "08", "6C", "74", "04", "D0", "20", "60", "44",
        "D8", "4C", "EC", "0C", "78", "54", "80", "D4", "14", "7C", "E8", "84",
        "10", "1C", "5C", "E0", "2C", "DC"
    }

    index_opcodes = {"C4","04","10","2C","B8"}

    
    instruction = input()
    
    hex_length = len(instruction)
    if hex_length == 2:
        res = length2(instruction)
    elif hex_length == 4:
        res = length4(instruction)
    elif hex_length == 6:
        res = length6(instruction)
    elif hex_length == 8:
        res = length8(instruction)
    else:
        print("Invalid instruction - Invalid length")
    if res:
        print("Valid instruction")
