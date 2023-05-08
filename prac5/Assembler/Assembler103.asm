// A simple example assembler test case
(LOOP)
@newsymbol
MD=-M
@LOOP
D;JGT
@newsymbol
0;JMP
@newsymbol
M=0
D=M-1
@newsymbol
D=A-D
M=D
@END
D;JLE
(END)
0;JMP

@newnewsymbol
M=0
D=M+1
A=M
A=D
