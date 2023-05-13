class VMTranslator:
    def __init__(self):
        self.sp = {0, 256} # stack pointer
        self.static = 16 # pointer to static base address [ranges to 255]
        self.temp = 5 # pointer to temp base address [ranges to 15]
        self.local = {1, 256} # the pointer is saved in this address
        self.argument = {2, 256} # the pointer is saved in this address
        self.this = {3, 256} # the pointer is saved in this address
        self.that = {4, 256} # the pointer is saved in this address 

    def vm_push(segment: str, offset: int)->str:
        '''Generate Hack Assembly code for a VM push operation'''
        '''Push operations tend to look like
        @offset
        D=A
        @segment+D
        D=M
        @SP
        M=D
        '''
        if(segment == 'argument'):
            print("Here")
        elif (segment == 'local'):
            print("NHere")
        elif (segment == 'temp'):
            print("NHere")
        elif (segment == 'temp'):
            print("NHere")
        elif (segment == 'temp'):
            print("NHere")
               
        return "" 

    def vm_pop(segment, offset):
        '''Generate Hack Assembly code for a VM pop operation'''
        return ""

    def vm_add():
        '''Generate Hack Assembly code for a VM add operation'''
        return ""

    def vm_sub():
        '''Generate Hack Assembly code for a VM sub operation'''
        return ""

    def vm_neg():
        '''Generate Hack Assembly code for a VM neg operation'''
        return ""

    def vm_eq():
        '''Generate Hack Assembly code for a VM eq operation'''
        return ""

    def vm_gt():
        '''Generate Hack Assembly code for a VM gt operation'''
        return ""

    def vm_lt():
        '''Generate Hack Assembly code for a VM lt operation'''
        return ""

    def vm_and():
        '''Generate Hack Assembly code for a VM and operation'''
        return ""

    def vm_or():
        '''Generate Hack Assembly code for a VM or operation'''
        return ""

    def vm_not():
        '''Generate Hack Assembly code for a VM not operation'''
        return ""

    def vm_label(label):
        '''Generate Hack Assembly code for a VM label operation'''
        return ""

    def vm_goto(label):
        '''Generate Hack Assembly code for a VM goto operation'''
        return ""

    def vm_if(label):
        '''Generate Hack Assembly code for a VM if-goto operation'''
        return ""

    def vm_function(function_name, n_vars):
        '''Generate Hack Assembly code for a VM function operation'''
        return ""

    def vm_call(function_name, n_args):
        '''Generate Hack Assembly code for a VM call operation'''
        return ""

    def vm_return():
        '''Generate Hack Assembly code for a VM return operation'''
        return ""



        