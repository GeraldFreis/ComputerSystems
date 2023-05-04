// Multiplies R1 and R2 and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// iterate R2 times over an addition of R1 to R1

@R0
M=0
// check if r1 or r2 is zero
@R1
D=M
@END
D;JEQ

@val1
M=D

@R2
D=M
@END
D;JEQ

@val2
M=D

// checking if R2 is negative
@R2
D=M
@NEGR2 // if not we move on
D;JLT

(WHILELOOP)
    @val1
	D=M
	@R0
	M=M+D
	@val2
	M=M-1
	D=M
	
	@WHILELOOP
	D;JGT

(END)
    @END
    0;JMP

(NEGR2)
    // if R1 is also negative we just make both positive. IF R1 is positive we make it negative and R2 positive
    @R1
    D=M
    @POSR1 // jumping if it is positive
    D;JGT

    // if R1 is negative and R2 is negative
    @0
    D=A
    @val1
    M=D-M
    @val2
    M=D-M

    @WHILELOOP
    0;JMP

(POSR1) // if R1 is positive and R2 is negative
    @0 // making R1 negative and R2 positive
    D=A
    @val1
    M=D-M

    @val2
    M=D-M
    @WHILELOOP
    0;JMP
