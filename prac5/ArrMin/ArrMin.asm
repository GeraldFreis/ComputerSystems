// Finds the smallest element in the array of length R2 whose first element is at RAM[R1] and stores the result in R0.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@index // keeping track of how many times we have iterated
M=0
//storing first value in min
@R1
A=M
D=M
@min
M=D

// we store the minimum value at R0
(LOOP)
	//checking if we are in bounds
	@R2
	D=M
	@index
	D=D-M // if INDEX > R2 (we skip to the end)
	@END
	D;JLE // (IF INDEX-R2 < 0: goto END)
	//ELSE
	
	//checking if the current value at R1 is < R0
	@min
	D=M
	@R1
	A=M
	D=D-M
	@ISMIN
	D;JGT
	
	@index
	M=M+1
	@R1
	M=M+1
	
	@LOOP
	0;JMP

(ISMIN)
	@R1
	A=M
	D=M
	@min
	M=D
	// updating all the values
	@index
	M=M+1
	@R1
	M=M+1
	
	@min
	D=M
	@R0
	M=D
	@LOOP
	0;JMP
	
(END)
	0;JMP
	
