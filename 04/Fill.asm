// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.
	// RAM starts from 0, 16k for data
	// @KBD means keyboard address 24576
	// @SCREEN contains 8k, from 16384, it ends at @KBD
// Put your code here.

(LOOP)
	@KBD
	D=M
	
	@PUSHED
	D;JNE
	
	
	@SCREEN
	D=A
	@addr
	M=D	
(WHITEN)
	@KBD
	D=A
	@addr
	D=M-D
	@LOOP
	D;JGE //if i>=n go to LOOP
	
	@addr
	A=M
	M=0
	
	@1
	D=A
	@addr
	M=D+M
	
	
	@WHITEN
	0;JMP
	


	
(PUSHED)

	@SCREEN
	D=A
	@addr
	M=D
	

	
(BLACKEN)
	@KBD
	D=A
	@addr
	D=M-D
	@LOOP
	D;JGE //if i>=n go to LOOP
	
	@addr
	A=M
	M=-1
	
	@1
	D=A
	@addr
	M=D+M
	
	
	@BLACKEN
	0;JMP
