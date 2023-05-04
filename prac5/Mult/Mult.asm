// This file is based on part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: Mult.asm

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

@R2
D=M
@END
D;JEQ

// checking if both are negative
@R1
D=M
@NEGATIVECHECK
D;JLT

@R2
D=M
@NEGATIVECHECK
D;JLT

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

(NEGATIVECHECK)
	// if we are here R1 was negative
	// now we check if R2 is negative
	@R2
	D=M
	@WHILELOOP // if R2 is > 0 we jump to the whileloop
	D;JGT	
	
	// we are here if R2 is < 0 (not equal to because we tested that above)
	@R0
	D=M
	@R2 // making R2 > 0
	M=D-M

	// if we are still here we make R1 > 0 too
	@R1
	D=M
	@WHILELOOP
	D;JGT

	@R0
	D=M
	@R1
	M=D-M 
	
(END)
	@END
	0;JMP
