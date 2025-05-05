
'''
 SeeThruComputer_cl_4-8bit_v0.1.1.py
 Richard Cross - 2023-03-12 11:20:52
 
 
 Change log:
 2023-03-15 21:53:00 - cosmetic changes to output 
'''

# ---- imports ----
from time import sleep 

# ---- variables ----
clockSpd = 500 #int - default 500 = 0.5 seconds per instruction
progCntr = 0 #int - using an integer for this because it makes array addressing easier
accum = "00000000" # default starting contents for the Accumulator register
status = 2 # status states: 0 = stopped, 1 = running, 2 = setup and user input write to memory
statStr = ["stop =", "run ==", "write "]
opcode = "0000"
operand = "0000"

# to run one of the pre-written programs, copy a memory list initialization code
# sample from the Sample-Programs_cl_4-8bit.txt file and paste into this
# program file replacing everything between the START and END comments
# surrounding the existing default all zeros memory content pre-load

# ================ memory contents pre-load command  - START ============

# default empty memory
memory = ["00000000", # 0000 
          "00000000", # 0001 
          "00000000", # 0010 
          "00000000", # 0011 
          "00000000", # 0100 
          "00000000", # 0101 
          "00000000", # 0110 
          "00000000", # 0111 
          "00000000", # 1000 
          "00000000", # 1001 
          "00000000", # 1010 
          "00000000", # 1011 
          "00000000", # 1100 
          "00000000", # 1101 
          "00000000", # 1110 
          "00000000"] # 1111

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
    # sum = A’B’C + A’BC’ + ABC + AB’C’
    # carry-out = AB + BC + AC
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


# ----- RUN --- changes the status to run and startes the execution of the program in memory ---
def runProg():
    global progCntr
    global status
    global opcode
    global operand
    
    progCntr = 0
    status = 1

    while(status == 1):
        instructionRegister = memory[progCntr]
        opcode = instructionRegister[:4]  # grab the first 4 bits
        operand = instructionRegister[4:] # grab the last 4 bits

        doInstruction() # execute the instruction

        # Simulator system clock - run from timer or manual user input
        if clockSpd == 0:
            input("push enter for next step")
        else:
            sleep(clockSpd/1000.0) # convert user micro-second input to fractional seconds

        # check for memory out of range condition and stop execution
        if progCntr > 15:
            progCntr = 15
            status = 0

#-------- CPU OPCODE instruction interpreter --------
def doInstruction():
    global progCntr
    global status
    global accum
    global opcode
    global operand

    xopcode = opcode
    xoperand = operand
    
    # increment Program Counter for default next instruction
    nextPC = progCntr + 1
    #concession to using arrays - convert operand value to integer to get memory location contents
    memLocAsInteger = int(xoperand,2)
    memLocContentsBinStr = memory[memLocAsInteger]
    
    # ---------- OPCODE interpreter ------------
    if xopcode == '0000':  # NOP
        # does nothing
        pass
      
    elif xopcode == '0001': # SHIFT R ACCUMULATOR
        accum = "0" + accum[:len(accum)-1]
        
    elif xopcode == '0010': # SHIFT L ACCUMULATOR
        accum = accum[1:] + "0"
        
    #----------- Logical -------------------
    elif xopcode == '0011': # NOT
        tempAccum = ""  
        for c in accum:
          if c == "1":
             tempAccum += "0"
          else:
             tempAccum += "1"
        accum = tempAccum
        
    elif xopcode == '0100': # AND
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
    elif xopcode == '1000': # LOAD DIRECT
        accum = memory[memLocAsInteger]

    elif xopcode == '0111': # LOAD INDIRECT
        indirectAddress = int(memory[memLocAsInteger], 2)
        accum = memory[indirectAddress]

    elif xopcode == '1110': # LOAD IMMEADIATE
        accum = "0000" + xoperand
        
    elif xopcode == '1001': # STORE
        memory[memLocAsInteger] = accum
        
    #---------- Algebraic -------------------
    elif xopcode == '1010': # ADD
          accum = adder_binStr(accum, memLocContentsBinStr)
        
    elif xopcode == '1011': # SUB
          twosCompMemBinStr = twosComp(memLocContentsBinStr)
          accum = adder_binStr(accum, twosCompMemBinStr)

    #---------- Branching and Control -------------------
    elif xopcode == '1100': # GOTO
        nextPC = memLocAsInteger

    elif xopcode == '1101':  # IFZERO jump
        if accum == "00000000":
            nextPC = memLocAsInteger

    elif xopcode == '1111': # STOP
        status = 0 # stop execution

    showStatus() # Display status snapshot of current instruction in the Sim interface

    #----- Update Program Counter for next fetch cycle ------
    progCntr = nextPC

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
    global opcode
    global operand
    global accum
    print("\n\n\n  -------------------------------------------------------------\n  ===================== status = " + statStr[status] + "========================")
    print('''  -------------------------------------------------------------
  |  program  ||  instruction register   ||    accumulator    |
  |  counter  ||  op code  |   operand   ||     contents      |
  |-----------||-------------------------||-------------------|''')
    PCbinStr = expandBinStr(int_to_bin_str(progCntr, 4))
    print("  |  " + PCbinStr + " ||  " + expandBinStr(opcode) + " |   " + expandBinStr(operand) + "  ||  " +  expandBinStr(accum) + " |")
    print('''  =============================================================
  | memory contents:               |
  | PC | address  |   stored data  |
  |                                |''')
      
    count = 0
    for count in range(16):
          lineLead = "  |       "
          if count == progCntr:
              lineLead = "  | PC>   "
          memStr = memory[count]
          PCstr = int_to_bin_str(count, 4)
          print(lineLead + PCstr + "  - - -  " + memStr + "    |")

    print("  ##########################################################")



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



