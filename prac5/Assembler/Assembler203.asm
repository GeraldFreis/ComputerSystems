// Calculates the absolute value of R1 and stores the result in R0.
// (R0, R1 refer to RAM[0], and RAM[1], respectively.)

// we need to calculate the absolute value (we will check if the value is less than zero)
@R1
D=M
@ELSE
D;JGT

@0
D=M-D
@R0
M=D
@END
0;JMP

(ELSE)
@R0
M=D
@END
0;JMP
