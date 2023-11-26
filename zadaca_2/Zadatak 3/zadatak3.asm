@0
D = M;
@IF_TRUE
D; JLE

@END
0;JMP

(IF_TRUE)
@0
D = D-M;
(END)

@10
M=D;
//--

@1
D = M;
@IF_TRUE1
D; JLE

@END1
0;JMP

(IF_TRUE1)
@1
D = D-M;
(END1)

@11
M=D;

//--

@2
D = M;
@IF_TRUE2
D; JLE

@END2
0;JMP

(IF_TRUE2)
@2
D = D-M;
(END2)

@12
M=D;

//--
@3
D = M;
@IF_TRUE3
D; JLE

@END3
0;JMP

(IF_TRUE3)
@3
D = D-M;
(END3)

@13
M=D;

//--

@4
D = M;
@IF_TRUE4
D; JLE

@END4
0;JMP

(IF_TRUE4)
@4
D = D-M;
(END4)

@14
M=D;

//--

@15
D = M;

@14
D = D + M;
@13
D = D + M;
@12
D = D + M;
@11
D = D + M;
@10
D = D + M;

@5
M = D;

(END100)
@END100
0;JMP
