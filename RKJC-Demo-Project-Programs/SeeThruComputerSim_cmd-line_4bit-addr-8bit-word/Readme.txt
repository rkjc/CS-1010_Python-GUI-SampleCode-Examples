SeeThruComputer


--------------------
src/SeeThruComputerSim_cmd-line_4bit-addr-8bit-word/SeeThruComputer_cl_4-8bit versions 

This version has a 4-bit address space and 8-bit word length
It is an all in one file, non-OOP Python3 program for simplicity and readability by Python beginers.
The only requirement is having python installed on the users system and running it from a command line.
It should require no additional library installations - pure default Python3 installation. 



operation:
----
to run the program in the memory enter the charachter
 a
at the prompt and hit enter
the Program counter will be set to 0000
and it will run the instruction at memory location 0000

----
to enter data into the memory location indicated by the Program Counter
enter the letter b followed by 8 1s or 0s, with no spaces

example:
b10010101
then hit enter
will store the binary value 10010101

---
move the program counter

c1010
will move it to the memory address 1010
---
change the clock speed in milliseconds
d500
will set it to run an instruction every 0.5 seconds

d0
will set it to run manually, press the enter key to run the net instruction.

------------------------------------------------------------------------------
# - instruction set -

#    opcode	Name	Description

#    0000	NOP 	No operation; safely ignored.

# -- logic --
# shift
#    0001	SHIFTR 	Bit shift the accumulator to the right by 1 position.

# Shift left command replaced by print command (0010	SHIFTL 	Bit shift the accumulator to the left by 1 position.)
#    0010   PRINT DIRECT - outputs contents of memory location to the 'terminal'

# boolean
#    0011	NOT 	Binary NOT the accumulator. The value 10101111 becomes 01010000.
#    0100	AND 	Binary AND the accumulator with the value stored at an address.
#    0101	OR 	    Binary OR the accumulator with the value stored at an address.
#    0110	XOR 	Binary XOR the accumulator with the value stored at an address.

# -- I/O  data transfer --
#    1000	LOAD 	Load the accumulator with the value stored at an address.
#    1001	STORE 	Copy the accumulator into an address.

# -- arithmetic --
#    1010	ADD 	Add the value stored at an address to the accumulator.
#    1011	SUB 	Subtract the value stored at an address from the accumulator.

# -- control --
# branch
#    1100	GOTO 	Jump to a program address.
#    1101	IFZERO 	If the accumulator is zero, jump to a program address.

#    1111	STOP 	Stop program execution.

# -----
# unused opcodes in this example
#    0111    (maybe implement a SKIP instruction?)
#    1110
--------------------------------------------------


