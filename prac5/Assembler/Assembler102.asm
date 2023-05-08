// A simple example assembler test case
@newsymbol
MD=-M
@0
D;JGT
@newsymbol
0;JMP
@newsymbol
M=0
D=M-1
@newsymbol
D=A-D
M=D
