//push
@111
D=A
@SP
M=M+1
A=M-1
M=D
//push
@333
D=A
@SP
M=M+1
A=M-1
M=D
//push
@888
D=A
@SP
M=M+1
A=M-1
M=D
//pop
@StaticTest.vm8
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
//pop
@StaticTest.vm3
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
//pop
@StaticTest.vm1
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
@StaticTest.vm3
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
@StaticTest.vm1
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
//sub
@SP
A=M-1
D=M
A=A-1
M=M-D
@SP
M=M-1
//push
@StaticTest.vm8
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
//add
@SP
A=M-1
D=M
A=A-1
M=D+M
@SP
M=M-1
