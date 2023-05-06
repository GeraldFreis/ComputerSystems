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
	@OUTOFRANGE // if (the firstIndex is > the length (R2): D will be < 0 and thus we will jump to OUTOFRANGE)
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
	// checking if either one is negative
	@jval
	D=M
	@JNEG // if jval is negative
	D;JLT

	// checking if I is negative
	@ival
	D=M
	@SECONDLOOP
	D;JLT


	@jval
	D=M
	@ival
	D=D-M // if the ival is > jval then D register will be negative 
	@ISGREATER
	D;JLE
	
	@SECONDLOOP
	0;JMP

(JNEG) // if both are negative
	// checking if ival is positive
	@ival
	D=M
	@INEG // jumps if i is negative
	D;JLT

	// if only Jval is negative we know that ival is greater 
	@ISGREATER
	0;JMP
	

(INEG) // we are here if both are neg
	// we can check if ival is greater by taking them away from each other
	@ival
	D=M
	@jval
	D=D-M // this will be positive if I is greater
	@ISGREATER
	D;JLT

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