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


@R1
D=M
@200
M=D
@201
M=D

(FIRSTLOOP) // this is a loop that iterates over all array items
	// checking that we are in range
	@firstIndex
	D=M
	@R2
	D=M-D
	@OUTOFRANGE // if (the firstIndex is > the length (R2): D will be < 0 and thus we will jump to OUTOFRANGE
	D;JLE
	
	
	// setting the current addresses
	@firstIndex
	D=M
	@R1
	A=M
	D=A+D
	@200
	M=D
	@201
	M=D+1
	//@R1
	//M=M+1
	
	// setting the current element
	@200
	D=M
	A=D
	D=M
	@ival
	M=D
	
	//@SECONDLOOP
	//0;JMP
	
(SECONDlOOP) // this is the second loop makes my life a lot easie koopa
	@secondIndex // going to the second index and checking range
	D=M
	@R2
	D=M-D
	@OUTOFRANGESECONDLOOP
	D;JLE

	// if we are fine

	// setting the second element
	@201
	D=M
	A=D
	D=M
	@jval
	M=D
	
	// setting the second address
	//@secondIndex
	@201
	M=M+1
	@secondIndex
	M=M+1
	// comparing the i and j vals
	@jval
	D=M
	@ival
	D=D-M // if the ival is > jval then D register will be negative 
	@ISGREATER
	D;JLE
	
	@SECONDLOOP
	0;JMP
		

(ISGREATER)
	// going to the firstIndex 
	@jval
	D=M
	@200
	A=M
	M=D
	
	@ival
	D=M
	@201
	A=M-1
	M=D
	
	// changing the addresse
	 
	@SECONDLOOP
	0;JMP


(OUTOFRANGE) // this is basically an end
	@R0 // setting R0 to true
	M=M-1
	@END
	0;JMP
(END)
	@END
	0;JMP

(OUTOFRANGESECONDLOOP) // this is for when we have iterated across the array
	@R1
	M=M+1
	@firstIndex // incrementing the first index
	M=M+1
	D=M
	@secondIndex // resetting the second index to the first index's value
	M=D+1
	
	@FIRSTLOOP // jumping back to the first 
	0;JMP

