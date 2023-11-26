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

@100
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

@101
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

@102
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

@103
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

@104
M=D;

//--

@105
D = M;

@104
D = D + M;
@103
D = D + M;
@102
D = D + M;
@101
D = D + M;
@100
D = D + M;

@5
M = D;

@104
M = 0;
@103
M = 0;
@102
M = 0;
@101
M = 0;
@100
M = 0;

(END100)
@END100
0;JMP
