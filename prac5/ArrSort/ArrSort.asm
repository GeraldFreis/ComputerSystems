@i // index of first loop
M=0
@j // index of second loop
M=0
// setting the first address
@R1
D=M
@201 // random point in memory holding the first address
M=D
@202 // random point in memory holding the second address
M=D
@temp // temporary value to store
M=0

(FIRSTLOOP)
	// checking that we are still in bounds
	@i
	D=M
	@R2
	D=M-D // if this is <= 0 we go to end
	@END
	D;JLE

	// setting up the address values
	@201
	D=M
	@202 // next value
	M=D+1

	(SECONDLOOP)
		// checking that we are in bounds
		@j
		D=M
		@R2
		D=M-D
		@OUTOFBOUNDSINNER
		D;JLE

		@202
		A=M
		D=M
		@COMPARENEGATIVES // if the value at the second address is < 0
		D;JLT
		// if we are still herer the second address is positive
		@COMPAREPOSITIVES // we jump unconditionally to the negatives
		0;JMP

(GENERICSWAP)
	@202 // storing second value in a temp spot
	A=M
	D=M

	@temp
	M=D
	@201 // putting the first value into the second value spot
	A=M
	D=M
	@202
	A=M
	M=D
	
	@temp
	D=M
	@201
	A=M
	M=D


(INCREMENT)
	@202 // incrementing the second address
	M=M+1
	@j
	M=M+1
	@SECONDLOOP
	0;JMP



(COMPARENEGATIVES)
	// checking if the first value is negative too
	@201
	A=M
	D=M
	// if it is we can jump to the swap negatives
	@SWAPNEGATIVES
	D;JLT
	// otherwise we know that second value is negative and first is positive so we just swap them
	@GENERICSWAP
	0;JMP

(SWAPNEGATIVES)
	// checking if the first value is > the second value
	@201
	A=M
	D=M
	@202
	A=M
	D=D-M // this will be positive if the first value is > than second
	// if it is < 0 we can just skip
	@INCREMENT
	D;JLE
	// otherwise if the val is positive first value is > than second
	@GENERICSWAP
	0;JMP

(COMPAREPOSITIVES)
	//checking if the first value is < 0 then we can just skip
	@201
	A=M
	D=M
	@INCREMENT
	D;JLE
	// we are here if first value is > 0
	// now we check which one is greater than the other
	@201
	A=M
	D=M
	@202
	A=M
	D=M-D // this will be negative if the first value is > than the second
	@GENERICSWAP
	D;JLT
	// otherwise we just increment
	@INCREMENT
	0;JMP

(OUTOFBOUNDSINNER)
	@201
	M=M+1
	@i
	M=M+1
	D=M
	@j
	M=D+1
	@FIRSTLOOP
	0;JMP

(END)
	@0
	D=A
	@R0
	M=D-1
	@END
	0;JMP
