(SimpleFunction.test)
//push
@0
D=A
@SP
M=M+1
A=M-1
M=D
//push
@0
D=A
@SP
M=M+1
A=M-1
M=D
//push
@LCL
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
@LCL
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
//not
@SP
A=M-1
M=!M
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
//add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
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
//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
@LCL
D=M
@R14
M=D
@R14
D=M
@5
A=D-A
D=M
@R15
M=D
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
@ARG
D=M
@SP
M=D+1
@R14
D=M
@1
A=D-A
D=M
@THAT
M=D
@R14
D=M
@2
A=D-A
D=M
@THIS
M=D
@R14
D=M
@3
A=D-A
D=M
@ARG
M=D
@R14
D=M
@4
A=D-A
D=M
@LCL
M=D
//Goto
@R15
A=M
0;JMP
