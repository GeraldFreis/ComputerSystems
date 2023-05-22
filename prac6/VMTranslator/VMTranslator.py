import random as r
class VMTranslator:
    def __init__(self): self.counter = 0;

    def vm_push(segment, offset):
        '''Generate Hack Assembly code for a VM push operation'''
        '''Push operations tend to look like
        '''
        if(segment == "pointer"): 
            return f"@R{str(3+offset)}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "this"):
            return f"@THIS\nD=M\n@{str(offset)}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "that"):
            return f"@THAT\nD=M\n@{str(offset)}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "local"):
            return f"@LCL\nD=M\n@{str(offset)}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "constant"):
            return f"@{str(offset)}\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "static"):
            return f"@{str(16+offset)}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "temp"):
            return f"@R{str(5+offset)}\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        elif(segment == "argument"):
            return f"@ARG\nD=M\n@{str(offset)}\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"


        return "" 

    def vm_pop(segment, offset): # moves something off the stack into the pointer pointed at by the segment and offset
        '''Generate Hack Assembly code for a VM pop operation'''
        if(segment == "constant"): return ""
        elif(segment == "temp"):
            return f"@{str(5+offset)}\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif(segment == "this"):
            return f"@THIS\nD=M\n@{str(offset)}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif(segment == "that"):
            return f"@THAT\nD=M\n@{str(offset)}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"

        elif(segment == "pointer"):
            return f"@{str(3+offset)}\nD=A\n@R15\nM=D\n@SP\nAM=M-1\nD=M\n@R15\nA=M\nM=D\n"

        elif(segment == "local"):
            return f"@LCL\nD=M\n@{str(offset)}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        elif(segment == "argument"):
            return f"@ARG\nD=M\n@{str(offset)}\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"

        elif(segment == "static"):
            return f"@{str(16+offset)}\nD=A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        return ""

    def vm_add():
        # takes two top values from the stack and stores them then performs addition and pushes that back into the place of the first one and then puts a zero 
        return str("@SP\nAM=M-1\nD=M\nA=A-1\nM=D+M\n")


    def vm_sub()->None:

        '''Generate Hack Assembly code for a VM sub operation'''
        return ""

    def vm_neg()->None:
        '''Generate Hack Assembly code for a VM neg operation'''
        return "@SP\nA=M-1\nM=-M\n"

    def vm_eq():
        return "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@ISEQ\nD;JEQ\n@SP\nA=M-1\nM=0\n@END\n0;JMP\n(ISEQ)\n@SP\nA=M-1\nM=-1\n(END)\n" 

    def vm_gt():
        print("@SP\nD=A\nD=M\nA=A-1\n")
        '''Generate Hack Assembly code for a VM gt operation'''
        return ""

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        return ""

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return str("@SP\nAM=M-1\nD=M\nA=A-1\nD=M&D\nM=D\n")

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return ""

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return ""

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        return str("("+ str(label) +")\n")

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        return str("@"+label+"\n0;JMP\n")

    def vm_if(label):
        return f"@SP\nAM=M-1\nD=M\n@ISFALSE\nD;JEQ\n@{label}\n0;JMP\n(ISFALSE)\n"

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        returnstring = str()
        returnstring += f"({function_name})\n"
        # setting all the locals to zero n shiz
        for i in range(0, int(n_vars)):
            returnstring += "@SP\nM=M+1\nA=M-1\nM=0\n"
        # returnstring += "D=A\n@LCL\nM=D\n"

        return returnstring

    def vm_call(function_name, n_args):

        '''Generate Hack Assembly code for a VM call operation'''
        # saving the stack address and resetting it to the return address
        random = r.randint(0,100);
        # return f"@SP\nD=M\n@R13\nM=D\n@RETURNSTACK{random}\nD=A\n@SP\nA=M\nM=D\n@SP\nD=M+1\nM=D\n@LCL\nD=M\n@SP\nA=M\nM=D\n@SP\nD=M+1\nM=D\n@ARG\nD=M\n@SP\nA=M\nM=D\n@SP\nD=M+1\nM=D\n@THIS\nD=M\n@SP\nA=M\nM=D\n@SP\nD=M+1\nM=D\n@THAT\nD=M\n@SP\nA=M\nM=D\n@SP\nD=M+1\nM=D\n@R13\nD=M\n@{str(n_args)}\nD=D-A\n@ARG\nM=D\n@SP\nD=M\n@LCL\nM=D\n@{function_name}\n0;JMP\n(RETURNSTACK{random})\n"
        returnstring = f"@RETURNSTACK.{str(random)}\nD=A\n@SP\nA=M\nM=D\nD=A+1\n" # setting the returnaddress into the stack
        returnstring += f"@LCL\nD=D+M\nA=D-M\nM=D-A\nD=A+1\n@ARG\nD=D+M\nA=D-M\nM=D-A\nD=A+1\n@THIS\nD=D+M\nA=D-M\nM=D-A\nD=A+1\n"
        returnstring += f"@THAT\nD=D+M\nA=D-M\nM=D-A\n" # resetting That to the original position
        returnstring += f"@SP\nD=M\n@{n_args}\nD=D-A\n@ARG\nM=D\n" # resetting arg
        returnstring += f"@5\nD=A\n@SP\nM=M+D\nD=M\n@LCL\nM=D\n@{function_name}\n0;JMP\n(@RETURNSTACK.{str(random)})\n"
        return returnstring

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        # god damn does this seem like a nasty little program ong no cap fr fr fr fr fr fr i hate this subject fr fr 
        # return f"@LCL\nD=M\n@5\nA=D-A\nD=M\n@R13\nM=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=A+1\n@SP\nM=D\n@LCL\nAM=M-1\nD=M\n@THAT\nM=D\n@LCL\nAM=M-1\nD=M\n@THIS\nM=D\n@LCL\nAM=M-1\nD=M\n@ARG\nM=D\n@LCL\nA=M-1\nD=M\n@LCL\nM=D\n@R13\nA=M\n0;JMP\n"
        return f"@LCL\nD=M\n@5\nA=D-A\nD=M\n@RETURNSTACK\nM=D\n@SP\nA=M-1\nD=M\n@ARG\nA=M\nM=D\n@ARG\nD=M+1\n@SP\nM=D\n@LCL\nAM=M-1\nD=M\n@THAT\nM=D\n@LCL\nAM=M-1\nD=M\n@THIS\nM=D\n@LCL\nAM=M-1\nD=M\n@RETURNSTACK\nA=M\n0;JMP\n"
# A quick-and-dirty parser when run as a standalone script.
if __name__ == "__main__":
    import sys
    if(len(sys.argv) > 1):
        with open(sys.argv[1], "r") as a_file:
            for line in a_file:
                tokens = line.strip().lower().split()
                if(len(tokens)==1):
                    if(tokens[0]=='add'):
                        print(VMTranslator.vm_add())
                    elif(tokens[0]=='sub'):
                        print(VMTranslator.vm_sub())
                    elif(tokens[0]=='neg'):
                        print(VMTranslator.vm_neg())
                    elif(tokens[0]=='eq'):
                        print(VMTranslator.vm_eq())
                    elif(tokens[0]=='gt'):
                        print(VMTranslator.vm_gt())
                    elif(tokens[0]=='lt'):
                        print(VMTranslator.vm_lt())
                    elif(tokens[0]=='and'):
                        print(VMTranslator.vm_and())
                    elif(tokens[0]=='or'):
                        print(VMTranslator.vm_or())
                    elif(tokens[0]=='not'):
                        print(VMTranslator.vm_not())
                    elif(tokens[0]=='return'):
                        print(VMTranslator.vm_return())
                elif(len(tokens)==2):
                    if(tokens[0]=='label'):
                        print(VMTranslator.vm_label(tokens[1]))
                    elif(tokens[0]=='goto'):
                        print(VMTranslator.vm_goto(tokens[1]))
                    elif(tokens[0]=='if-goto'):
                        print(VMTranslator.vm_if(tokens[1]))
                elif(len(tokens)==3):
                    if(tokens[0]=='push'): # pushing segments and then  which one to push (inbound checking?)
                        print(VMTranslator.vm_push(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='pop'):
                        print(VMTranslator.vm_pop(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='function'):
                        print(VMTranslator.vm_function(tokens[1],int(tokens[2])))
                    elif(tokens[0]=='call'):
                        print(VMTranslator.vm_call(tokens[1],int(tokens[2])))

        