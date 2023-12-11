def _parse_macros(self):
    self._iter_lines(self._parse_macro)

# Macro je zadan $MV(A,B)
def _parse_macro(self, line, p, o):
    if line[0] == "$":
        macrostring = line[1:] 
        macro = macrostring.split("(") 
        #treba se splitati kod "(" i dobijemo listu: [MV, A,B)]
        command= macro[0]

        argumentstring = []
        arguments=[]

        if len(macro) >1:
            argumentstring = macro[1]
            argumentstring =argumentstring.split(")")
            arguments=argumentstring[0].split(",")

        
            #MV izgleda ovako:
            # @a
            # D=M
            # @b
            # M=D 
            if command == "MV":
                blok = "@" + str(arguments[0])+"\n"+"D=M"+"\n"+"@" + str(arguments[1])+"\n"+"M=D"
                #blok = ["@" + str(arguments[0]), "D=M", "@" + str(arguments[1]), "M=D"]
                return blok


        
            #SWAP izgleda ovako:
            #@temp
            #M=0
            #@a
            #D=M
            #@temp
            #M=D
            #@b
            #D=M
            #@a
            #M=D
            #@temp
            #D=M
            #@b
            #M=D
            elif command == "SWP":
                #blok = ["@temp", "M=0", "@" + str(arguments[0]), "D=M", "@temp", "M=D", "@" + str(arguments[1]), "D=M", "@" + str(arguments[0]), "M=D", "@temp", "D=M", "@" + str(arguments[1]),"M=D"]
                blok = "\n@temp"+ "\nM=0"+ "\n@" + str(arguments[0])+ "\nD=M"+ "\n@temp"+ "\nM=D"+ "\n@" + str(arguments[1])+ "\nD=M"+ "\n@" + str(arguments[0])+ "\nM=D"+ "\n@temp"+ "\nD=M" + "\n@" + str(arguments[1])+"\nM=D"
                return blok

            #SUM izgleda ovako:
            #@a
            #D=M
            #@b
            #D=D+M
            #@d
            #M=D
            elif command == "SUM":
                #blok = ["@" + str(arguments[0]), "D=M", "@" + str(arguments[1]), "D=D+M", "@" + str(arguments[2]), "M=D"]
                blok = "@" + str(arguments[0])+ "\nD=M"+ "\n@" + str(arguments[1])+ "\nD=D+M"+ "\n@" + str(arguments[2])+ "\nM=D"
                return blok


            #WHILE izgleda ovako:
            #(WHILE i)
            #@argument
            #D=M
            #@END i
            #D;JEQ
            elif command == "WHILE":
                self._nested += 1
                #blok = ["(WHILE" + str(self._nested) + ")", "@" + str(arguments[0]), "D=M", "@END" + str(self._nested), "D;JEQ"]
                blok = "(WHILE" + str(self._nested) + ")"+ "\n@" + str(arguments[0])+ "\nD=M"+ "\n@END" + str(self._nested)+ "\nD;JEQ"
                return blok
        
            elif command == "END":
                #blok = ["@WHILE" + str(self._nested), "0;JMP", "(END" + str(self._nested) + ")"]
                blok = "@WHILE" + str(self._nested) + "\n0;JMP" +"\n(END" + str(self._nested) + ")"
                self._nested -=1
                return blok
        
            else:
                self._flag = False
                self._line =  o 
                self._errm = "Invalid command: " + command
                return ""
    else:
        return line