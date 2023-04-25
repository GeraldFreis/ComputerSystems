// Sorts the array of length R2 whose first element is at RAM[R1] in ascending order in place. Sets R0 to True (-1) when complete.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// We are going to do a bubble sort in this code (we place each element before and after things they are greater than

@firstIndex
M=0
@ival
M=0
@secondIndex
M=0
@jval
M=0

(FIRSTLOOP) // this is a loop that iterates over all array items
	// checking that we are in range
	@firstIndex
	D=M
	@R2
	D=D-M
	@OUTOFRANGE // if (the firstIndex is > the length (R2): D will be < 0 and thus we will jump to OUTOFRANGE
	D;JGT

	// going to the current element
	@firstIndex
	D=M
	@R1
	A=M+D // going to the address at R1 + index
	D=A
	@ival // setting the i val to the current element
	M=D
	(SECONDlOOP) // this is the second loop makes my life a lot easie koopa
		@secondIndex // going to the second index and checking range
		D=M
		@R2
		D=D-M
		@OUTOFRANGESECONDLOOP
		D;JGT

		// if we are fine

		// setting the second element
		@secondIndex
		D=M
		@R1
		A=M+D
		D=A
		@jval
		M=D

		// comparing the i and j vals
		@jval
		D=M
		@ival
		D=D-M // if the ival is > jval then D register will be negative 
		@ISGREATER





(OUTOFRANGE) // this is basically an end
	@R0 // setting R0 to true
	D=M
	D=D-1
	M=D
	0;JMP

(OUTOFRANGESECONDLOOP) // this is for when we have iterated across the array
	@firstIndex // incrementing the first index
	M=M+1
	D=M
	@secondIndex // resetting the second index to the first index's value
	M=D+1

	@FIRSTLOOP // jumping back to the first 
	0;JMP





