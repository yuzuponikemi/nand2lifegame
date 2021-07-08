// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
	@SUM
	M=0
	@i
	M=0
	@R2
	M=0

	@R0
	D=M
	@R1
	D=M-D
	
	@POSITIVE
	D;JGT
	
	//NEGATIVE R0>=R1
	@R0
	D=M
	@LG
	M=D
	@R1
	D=M
	@SM
	M=D
	
	@MULT
	0;JMP
	
(POSITIVE)
	//POSITIVE R0<R1
	@R1
	D=M
	@LG
	M=D
	@R0
	D=M
	@SM
	M=D
	
(MULT)   // sum=sum+LG for SM times
	@i
	D=M
	@SM
	D=D-M
	@OUT
	D;JGE //if i>=SM go to END
	
	@i
	M=M+1
	@LG
	D=M
	@SUM
	M=M+D
	
	
	@MULT
	0;JMP
	
(OUT)
	@SUM
	D=M
	@R2
	M=D
(END)
	@END
	0;JMP
	