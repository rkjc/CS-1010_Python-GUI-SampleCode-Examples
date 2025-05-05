
'''
 SeeThruComputer_cl_4-8bit_v0.1.2.py
 Richard Cross - 2023-03-12 11:20:52
 
 
 Change log:
 2023-03-15 21:53:00 
 adding activity output display and sub-steps indicator 
'''

# ---- imports ----
from time import sleep 

# ---- variables ----
clockSpd = 0 #int - default 0 for manual stepping
progCntr = 0 #int - using an integer for this because it makes array addressing easier
nextPC = 0
accum = "00000000" # default starting contents for the Accumulator register
status = 2 # status states: 0 = stopped; 1 = running; 2 = setup and user input write to memory
statStr = ["stop =", "run ==", "write "]
opcode = "0000"
operand = "0000"
currentOp = ""
currentInst = ""
terminal = ['','','','','','','','']

# to run one of the pre-written programs, copy a memory list initialization code
# sample from the Sample-Programs_cl_4-8bit.txt file and paste into this
# program file replacing everything between the START and END comments
# surrounding the existing default all zeros memory content pre-load

# ================ memory contents pre-load command  - START ============

# count to 2B with output
memory = ["10001111", # 0000 LOAD 1111 
          "10101110", # 0001 ADD 1110
          "10011111", # 0010 STOR 1111
          "00101111", # 0011 PRINT from 1111
          "01101101", # 0100 XOR 1101
          "11010111", # 0101 IFZERO 0111
          "11000000", # 0110 GOTO 0000
          "11110000", # 0111 STOP
          "00000000", # 1000 
          "00000000", # 1001  
          "00000000", # 1010 
          "00000000", # 1011 
          "00000000", # 1100 
          "00101011", # 1101 xor comparison value
          "00000001", # 1110 increment value
          "00000000"] # 1111 save copy accum

# ============== memory contents pre-load command - END ==================

# ------------- functions ----------------
'''
 Logical NOT
 takes a binary value of any length in string format
 returns the 'not' or inverted binary string of same length
'''
def not_binStr(inBinStr):
    tempBinStr = ""
    for c in inBinStr:
        if c == "1":
            tempBinStr += "0"
        else:
            tempBinStr += "1"
    return tempBinStr

'''
 Twos Complement
 takes a binary value in string form
 returns a same number of bits twos complement binary string
 '''
def twosComp(inBinStr):
    inverted_InBinStr = not_binStr(inBinStr)
    binCompStr = ("0" * (len(inBinStr) - 1)) + "1"
    binCompStr = adder_binStr(inverted_InBinStr, binCompStr)
    return binCompStr

'''
ADD two binary numbers
takes two binary values in string format, inputs must be same length
uses boolean expressions to produce a binary sum
Because of collection indexing numbers the colum index
variable 'i' starts at numBits - 1 for the right most LSB digit
The left most MSB digit is column index i = 0
'''
def adder_binStr(val1, val2):
    #-----------------------------------
    # sum = A’B’C + A’BC’ + ABC + AB’C’
    # carry-out = AB + BC + AC
    #-----------------------------------
    numBits = len(val1)
    tempSum = ""
    # carry value is an array of chars instead of a binary as string
    # but it is only used in the method and not returned
    carry = ['0'] * numBits  # makes an array of '0's to match the length of the input values

    # for these binary numbers as strings, the LSB column index is numBits-1
    # using range statement attributes that gives i = numBits - 1 down to 0
    for i in range(numBits-1, -1, -1):
        # determine the sum diget for the current column i
        trm1 = val1[i] == "0" and val2[i] == "0" and  carry[i] == "1" # A’B’C
        trm2 = val1[i] == "0" and val2[i] == "1" and  carry[i] == "0" # A’BC’
        trm3 = val1[i] == "1" and val2[i] == "1" and  carry[i] == "1" # ABC
        trm4 = val1[i] == "1" and val2[i] == "0" and  carry[i] == "0" # AB’C’
        if (trm1 or trm2 or trm3 or trm4):
            sumDiget = "1"
        else:
            sumDiget = "0"

        # determine and update the carry diget for the column i-1
        # Carry is not calculated for column 0 as it will be discarded as overflow
        if i > 0:
            tcry1 = val1[i] == "1" and val2[i] == "1"   # AB
            tcry2 = val2[i] == "1" and  carry[i] == "1" # BC
            tcry3 = val1[i] == "1" and  carry[i] == "1" # AC
            if (tcry1 or tcry2 or tcry3):
                carryDiget = "1"
            else:
                carryDiget = "0"

            # update the carry bit value
            # using i-1 because the carry result is always saved in # the next column to the left of the sum value
            carry[i - 1] = carryDiget

        # update the sum after column bit values have been calculated
        tempSum = sumDiget + tempSum
        # when column 0 only gets a sum value, carry is discarded
    return tempSum

def send_to_output(binary_val):
    MSB = binary_val[:4]  # grab the first 4 bits
    LSB = binary_val[4:] # grab the last 4 bits
    terminal.append(hex_lookup(MSB) + hex_lookup(LSB))
    terminal.pop(0)


def hex_lookup(binary_4_bit): 
    if binary_4_bit == "0000":
        return "0"
    elif binary_4_bit == "0001":
        return "1"
    elif binary_4_bit == "0010":
        return "2"
    elif binary_4_bit == "0011":
        return "3"
    elif binary_4_bit == "0100":
        return "4"
    elif binary_4_bit == "0101":
        return "5"
    elif binary_4_bit == "0110":
        return "6"
    elif binary_4_bit == "0111":
        return "7"
    elif binary_4_bit == "1000":
        return "8"
    elif binary_4_bit == "1001":
        return "9"
    elif binary_4_bit == "1010":
        return "A" 
    elif binary_4_bit == "1011":
        return "B"
    elif binary_4_bit == "1100":
        return "C"
    elif binary_4_bit == "1101":
        return "D"
    elif binary_4_bit == "1110":
        return "E"
    elif binary_4_bit == "1111":
        return "F"   


# ----- RUN --- changes the status to run and startes the execution of the program in memory ---
def runProg():
    global progCntr, nextPC
    global status
    global opcode, currentInst
    global operand, currentOp
    
    progCntr = 0
    status = 1

    while(status == 1):
        
        currentOp = "load Instruction Register"
        instructionRegister = memory[progCntr]
        opcode = instructionRegister[:4]  # grab the first 4 bits
        operand = instructionRegister[4:] # grab the last 4 bits
        showStatus() # Display status snapshot of current instruction in the Sim interface
        stepPause()
        
        
        currentOp = "execute instruction"
        doInstruction() # execute the instruction
        showStatus() # Display status snapshot of current instruction in the Sim interface
        stepPause()
        if status == 0: # STOPPED
            break
        currentInst = ""
        

        currentOp = "update Program Counter"
        progCntr = nextPC # Update Program Counter for next fetch cycle
        showStatus() # Display status snapshot of current instruction in the Sim interface
        stepPause()
        
        # check for memory out of range condition and stop execution
        if progCntr > 15:
            progCntr = 15
            status = 0 
            
def stepPause():
        # Simulator system clock - run from timer or manual user input
    if clockSpd == 0:
        input("push enter for next step")
    else:
        sleep(clockSpd/1000.0) # convert user micro-second input to fractional seconds


#-------- CPU OPCODE instruction interpreter --------
def doInstruction():
    global progCntr, nextPC
    global status
    global accum
    global opcode, currentInst
    global operand, currentOp

    xopcode = opcode
    xoperand = operand
    
    # increment Program Counter for default next instruction
    nextPC = progCntr + 1
    #concession to using arrays - convert operand value to integer to get memory location contents
    memLocAsInteger = int(xoperand,2)
    memLocContentsBinStr = memory[memLocAsInteger]
    
    # ---------- OPCODE interpreter ------------
    if xopcode == '0000':  # NOP
        currentInst = "NOP"
        # does nothing
        pass
      
    elif xopcode == '0001': # SHIFT R ACCUMULATOR
        currentInst = "SHIFT R ACCUMULATOR"
        accum = "0" + accum[:len(accum)-1]
        
#    elif xopcode == '0010': # SHIFT L ACCUMULATOR
#        currentInst = "SHIFT L ACCUMULATOR"
#        accum = accum[1:] + "0"

    elif xopcode == '0010': # PRINT DIRECT
        currentInst = "PRINT DIRECT"
        send_to_output(memory[memLocAsInteger])
        
    #----------- Logical -------------------
    elif xopcode == '0011': # NOT
        currentInst = "NOT"
        tempAccum = ""  
        for c in accum:
          if c == "1":
             tempAccum += "0"
          else:
             tempAccum += "1"
        accum = tempAccum
        
    elif xopcode == '0100': # AND
        currentInst = "AND"
        cnt = 0
        tempAccum = ""
        tempMem = memLocContentsBinStr
        while cnt < len(accum):
          if accum[cnt] == "1" and tempMem[cnt] == "1":
             tempAccum += "1"
          else:
             tempAccum += "0"
          cnt += 1   
        accum = tempAccum
        
    elif xopcode == '0101': # OR
        currentInst = "OR"
        cnt = 0
        tempAccum = ""
        tempMem = memLocContentsBinStr
        while cnt < len(accum):
           if accum[cnt] == "0" and tempMem[cnt] == "0":
              tempAccum += "0"
           else:
              tempAccum += "1"
           cnt += 1   
        accum = tempAccum
        
    elif xopcode == '0110': # XOR
        currentInst = "XOR"
        cnt = 0
        tempAccum = "" # temporary empty string
        tempMem = memLocContentsBinStr
        while cnt < len(accum):
           if accum[cnt] == tempMem[cnt]:
              tempAccum += "0"
           else:
              tempAccum += "1"
           cnt += 1   
        accum = tempAccum

    #---------- Memory -------------------

    elif xopcode == '0111': # LOAD INDIRECT
        currentInst = "LOAD INDIRECT"
        indirectAddress = int(memory[memLocAsInteger], 2)
        accum = memory[indirectAddress]
        
    elif xopcode == '1000': # LOAD DIRECT
        currentInst = "LOAD DIRECT"
        accum = memory[memLocAsInteger]

    elif xopcode == '1110': # LOAD IMMEADIATE
        currentInst = "LOAD IMMEADIATE"
        accum = "0000" + xoperand
        
    elif xopcode == '1001': # STORE
        currentInst = "STORE"
        memory[memLocAsInteger] = accum
        
    #---------- Algebraic -------------------
    elif xopcode == '1010': # ADD
        currentInst = "ADD"
        accum = adder_binStr(accum, memLocContentsBinStr)
        
    elif xopcode == '1011': # SUB
        currentInst = "SUB"
        twosCompMemBinStr = twosComp(memLocContentsBinStr)
        accum = adder_binStr(accum, twosCompMemBinStr)

    #---------- Branching and Control -------------------
    elif xopcode == '1100': # GOTO
        currentInst = "GOTO"
        nextPC = memLocAsInteger

    elif xopcode == '1101':  # IFZERO jump
        currentInst = "IF ZERO JUMP"
        if accum == "00000000":
            nextPC = memLocAsInteger

    elif xopcode == '1111': # STOP
        currentInst = "STOP"
        status = 0 # stop execution

    # don't really need this here, but it helps to indicate the end of this long function
    return

#-----------------------------------------------------------------------
#---- helper utilities for the Simulator terminal display interface ----

'''
 converts a positive integer value into a string of 1' and 0'
 unsigned binary representation, includes leading 0s
 mainly used to display the PC location in binary form
'''
def int_to_bin_str(intIn, numBits=8):
      tempStr = ((bin(intIn))[2:])
      tempStr = ((numBits - len(tempStr))*"0") + tempStr
      return tempStr

# adds spaces between each charachter to make it more readable on the screen
# improves viewability of binary numbers in the display
def expandBinStr(inBinStr, spaceNum=1):
      outStr = ""
      for c in inBinStr:
          outStr = outStr + c + (" " * spaceNum)
      return outStr


#----------- terminal interface -----------------------------------
def showStatus():
    global opcode, currentOp, currentInst
    global operand, accum 
    
    print("\n\n\n  -------------------------------------------------------------------\n  ========================= status = " + statStr[status] + "==========================")
    print('''  -------------------------------------------------------------------
  |  Program  |   |  Instruction Register   |   |    Accumulator    |
  |  Counter  |   |  op code  |   operand   |   |     contents      |
  |-----------|   |-------------------------|   |-------------------|''')
    PCbinStr = expandBinStr(int_to_bin_str(progCntr, 4))
    print("  |  " + PCbinStr + " |   |  " + expandBinStr(opcode) + " |   " + expandBinStr(operand) + "  |   |  " +  expandBinStr(accum) + " |")
    print('''  ===================================================================
  | memory contents:               |
  | PC | address  |   stored data  |
  |                                |      -------------------------------''')
      
    count = 0
    for count in range(16):
        lineTail = ""
        lineLead = "  |       "
        if count == progCntr:
            lineLead = "  | PC>   "
            
            
        #currentOp = str(opcode)

        if count == 0:
            lineTail = "     |    currentOperation:          |"
        if count == 1:
            lineTail = "     |   " + currentOp + (" " * (28 - len(currentOp))) + "|"    
        if count == 2:
            lineTail = "     |    " + currentInst + (" " * (27 - len(currentInst))) + "|"
        if count == 3:
            lineTail = "      -------------------------------"
            
        if count == 5:
            lineTail = "      -------------------------------"
        if count == 6:
            lineTail = "     |" + terminal[0]+ (" " * (31 - len(terminal[0]))) + "|"
        if count == 7:
            lineTail = "     |" + terminal[1]+ (" " * (31 - len(terminal[1]))) + "|"
        if count == 8:
            lineTail = "     |" + terminal[2]+ (" " * (31 - len(terminal[2]))) + "|"
        if count == 9:
            lineTail = "     |" + terminal[3]+ (" " * (31 - len(terminal[3]))) + "|"
        if count == 10:
            lineTail = "     |" + terminal[4]+ (" " * (31 - len(terminal[4]))) + "|"
        if count == 11:
            lineTail = "     |" + terminal[5]+ (" " * (31 - len(terminal[5]))) + "|"
        if count == 12:
            lineTail = "     |" + terminal[6]+ (" " * (31 - len(terminal[6]))) + "|"
        if count == 13:
            lineTail = "     |" + terminal[7]+ (" " * (31 - len(terminal[7]))) + "|"      
        if count == 14:
            lineTail = "      -------------------------------" 

        PCstr = int_to_bin_str(count, 4)
        memStr = memory[count]
        print(lineLead + PCstr + "  - - -  " + memStr + "    |" + lineTail)

    print("  ##################################################################")



# ---- main program - user interaction setup and run loop ----
while(True):
    showStatus()
    print('''
    select operation:
    (a)run program
    (b)store binary data in current memory address
    (c)change current Program Counter pointer
    (d)set clock speed in milliseconds (enter an integer value)
    ''', end="")
    
    inStr = input("enter-> ")
    if len(inStr) == 0:
        inStr = 'a'

    command = inStr[0].lower()
    inTrimStr = inStr[1:9] # for 8-bit inputs
    
    if command == 'a':
        runProg()
        break
    elif command =='b':
        memory[progCntr] = inTrimStr
        if progCntr < 15:
           progCntr += 1
    elif command == 'c':
        inInt = int(inTrimStr, 2)
        progCntr = inInt
    elif command == 'd':
        inTimeStr = inStr[1:]
        inTimeInt = int(inTimeStr)
        clockSpd = inTimeInt 



