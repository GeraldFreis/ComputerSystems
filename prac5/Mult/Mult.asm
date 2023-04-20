// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// iterate R2 times over an addition of R1 to R1

@R0
M=0

(WHILELOOP)
@R1
D=M
@R0
M=M+D
@R2
M=M-1
D=M
@WHILELOOP
D;JGT

(END)
@END
0;JMP
