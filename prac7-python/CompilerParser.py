from ParseTree import *

class CompilerParser :

    def __init__(self,tokens):
        """
        Constructor for the CompilerParser
        @param tokens A list of tokens to be parsed
        """
        self.iterator = 0
        self.token_array = tokens;
        self.keywords = ('class', 'constructor', 'function', 'method', 'field', 'static', 'var', 'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let', 'do', 'if', 'else', 'while', 'return')
        self.symbols = ('{', '}', '(', ')', '[', ']', ',', '.', ';', '+', '-', '*', r'/', '&', '|', '<', '>', '=', '~')
        self.sub_routines = ('function', 'method', 'constructor')
        self.var_declarations = ('field', 'static')
        return # don't want a pass statement here that would be fucking stupid
    

    def compileProgram(self): # main compile program
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        # checking if the first line is a class name or main (it needs to be)
        if(self.token_array[0].value != "class" and (self.token_array[1].value != "Main" ) or self.token_array[1].value != "main"): raise ParseException; return None; # return should be unreached but just in case

        parsed_tree = ParseTree("class", "")
        for token in self.token_array: # for each token we add it
            if (token.node_type == 'symbol' and token.value == '}'): break

            # otherwise we want to parse it all
            if(token.node_type == 'keyword' and token.value in self.sub_routines):
                parsed_tree.addChild(compileSubroutine())
            elif(token.node_type == 'keyword' and token.value in self.var_declarations):
                parsed_tree.addChild(compileClassVarDec())
            else:
                parsed_tree.addChild(token)

            self.iterator += 1;
        # checking that the first 
        return parsed_tree; 
    
    
    def compileClass(self):
        """
        Generates a parse tree for a single class
        @return a ParseTree that represents a class
        """
        return None 
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        # creating a new tree
        newparsed = ParseTree("classVariableDeclarations", "")
        newparsed.addChild(self.token_array[self.iterator+1])
        newparsed.addChild(self.token_array[self.iterator+2])
        newparsed.addChild(self.token_array[self.iterator+3])
        counter = 0
        for i in range(self.iterator+4, len(self.token_array)):
            if(self.token_array[i].value == ","):
                newparsed.addChild(self.token_array[i]); newparsed.addChild(self.token_array[i+1]);
                i += 1; counter = i;
            else:
                break;

        newparsed.addChild(self.token_array[self.counter]) # adding the last element
        self.iterator = counter
        return newparsed 
    

    def compileSubroutine(self):
        """
        Generates a parse tree for a method, function, or constructor
        @return a ParseTree that represents the method, function, or constructor
        """
        
        return None 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        return None 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        return None 
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        return None 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        return None 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        return None 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        return None 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        return None 


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        return None 


    def next(self):
        """
        Advance to the next token
        """
        return


    def current(self):
        """
        Return the current token
        @return the token
        """
        return None


    def have(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        @return True if a match, False otherwise
        """
        # where does this token live?
        return False


    def mustBe(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        If so, advance to the next token, returning the current token, otherwise throw/raise a ParseException.
        @return token that was current prior to advancing.
        """
        return None
    

if __name__ == "__main__":


    """ 
    Tokens for:
        class MyClass {
        
        }
    """
    tokens = []
    tokens.append(Token("keyword","class"))
    tokens.append(Token("identifier","MyClass"))
    tokens.append(Token("symbol","{"))
    tokens.append(Token("symbol","}"))

    parser = CompilerParser(tokens)
    try:
        result = parser.compileProgram()
        print(result)
    except ParseException:
        print("Error Parsing!")
