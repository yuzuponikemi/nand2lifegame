//push
@ARG
D=M
@1
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//pop
@4
D=A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//push
@0
D=A
@SP
M=M+1
A=M-1
M=D
//pop
@THAT
D=M
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//push
@1
D=A
@SP
M=M+1
A=M-1
M=D
//pop
@THAT
D=M
@1
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//push
@ARG
D=M
@0
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//push
@2
D=A
@SP
M=M+1
A=M-1
M=D
//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//pop
@ARG
D=M
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
(MAIN_LOOP_START)
//push
@ARG
D=M
@0
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//if-Goto
@SP
AM=M-1
D=M
@COMPUTE_ELEMENT
D;JNE
//Goto
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
//push
@THAT
D=M
@0
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//push
@THAT
D=M
@1
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//pop
@THAT
D=M
@2
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//push
@4
D=A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//push
@1
D=A
@SP
M=M+1
A=M-1
M=D
//add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
//pop
@4
D=A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//push
@ARG
D=M
@0
D=D+A
@13
M=D
@13
A=M
D=M
@SP
M=M+1
A=M-1
M=D
//push
@1
D=A
@SP
M=M+1
A=M-1
M=D
//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//pop
@ARG
D=M
@0
D=D+A
@13
M=D
@SP
M=M-1
A=M
D=M
@13
A=M
M=D
//Goto
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
