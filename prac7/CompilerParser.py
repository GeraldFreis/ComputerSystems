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
        self.statements = ('let', 'do', 'if', 'while', 'return')
        return # don't want a pass statement here that would be fucking stupid
    

    def compileProgram(self): # main compile program
        """
        Generates a parse tree for a single program
        @return a ParseTree that represents the program
        """
        # checking if the first line is a class name or main (it needs to be)
        if(self.token_array[0].value != "class" and self.token_array[1].value != "Main"  and self.token_array[1].value != "main"): raise ParseException; return None; # return should be unreached but just in case

        parsed_tree = ParseTree("class", "")
        for token in self.token_array: # for each token we add it
            if     (token.node_type == 'symbol' and token.value == '}'): break

            # otherwise we want to parse it all
            if     (token.node_type == 'keyword' and token.value in self.sub_routines):
                parsed_tree.addChild(compileSubroutine())
            elif   (token.node_type == 'keyword' and token.value in self.var_declarations):
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
        parsed_tree = ParseTree("class", "")
        for token in self.token_array: # for each token we add it
            if     (token.node_type == 'symbol' and token.value == '}'): break

            # otherwise we want to parse it all
            if     (token.node_type == 'keyword' and token.value in self.sub_routines):
                parsed_tree.addChild(compileSubroutine())
            elif   (token.node_type == 'keyword' and token.value in self.var_declarations):
                parsed_tree.addChild(compileClassVarDec())
            else:
                parsed_tree.addChild(token)

            self.iterator += 1;
        # checking that the first 
        return parsed_tree; 
        # return None 
    

    def compileClassVarDec(self):
        """
        Generates a parse tree for a static variable declaration or field declaration
        @return a ParseTree that represents a static variable declaration or field declaration
        """
        # creating a new tree
        newparsed = ParseTree("classVarDec", "")
        newparsed.addChild(self.token_array[self.iterator+1])
        newparsed.addChild(self.token_array[self.iterator+2])
        newparsed.addChild(self.token_array[self.iterator+3])
        counter = 0
        for i in range(self.iterator+4, len(self.token_array)):
            if    (self.token_array[i].value == ","):
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
        newparsed = ParseTree("subroutine", "")
        newparsed.addChild(self.token_array[self.iterator])
        newparsed.addChild(self.token_array[self.iterator+1])
        newparsed.addChild(self.token_array[self.iterator+2])
        newparsed.addChild(self.token_array[self.iterator+3])
        newparsed.addChild(compileParameterList())
        newparsed.addChild(self.token_array[self.iterator])  # iterator should be updated
        newparsed.addChild(compileSubroutineBody())

        return newparsed 
    
    
    def compileParameterList(self):
        """
        Generates a parse tree for a subroutine's parameters
        @return a ParseTree that represents a subroutine's parameters
        """
        newparsed = ParseTree("parameterList", "")

        for i in range(self.iterator, len(self.token_array)):

            if     (token_array[i].value == ")"):
                newparsed.addChild(token_array[i]); self.iterator = i; break;
            else: 
                newparsed.addChild(token_array[i])

        return newparsed 
    
    
    def compileSubroutineBody(self):
        """
        Generates a parse tree for a subroutine's body
        @return a ParseTree that represents a subroutine's body
        """
        newparsed = ParseTree("subroutineBody", "")
        # checking if we have a variable, and if so we compile it, else we compile statements
        for i in range(self.iterator, len(self.token_array)):
            if(self.token_array[i].value != "}"): # if we are still in the subroutine
                if     (self.token_array[i].value != "var"): # if we do not have a variable declaration we know that we have a statement
                    newparsed.addChild(compileStatements())
                else:
                    newparsed.addChild(compileVarDec())
            else:
                self.iterator = i;
                break;
        
        return newparsed 
    
    
    def compileVarDec(self):
        """
        Generates a parse tree for a variable declaration
        @return a ParseTree that represents a var declaration
        """
        newparsed = ParseTree("varDec", "")
        newparsed.addChild(self.token_array[self.iterator+1])
        newparsed.addChild(self.token_array[self.iterator+2])
        newparsed.addChild(self.token_array[self.iterator+3])

        counter = 0
        for i in range(self.iterator+4, len(self.token_array)):
            if    (self.token_array[i].value == ","):
                newparsed.addChild(self.token_array[i]); newparsed.addChild(self.token_array[i+1]);
                i += 1; counter = i;
            else:
                break;

        newparsed.addChild(self.token_array[self.counter]) # adding the last element
        self.iterator = counter
        return newparsed 
    

    def compileStatements(self):
        """
        Generates a parse tree for a series of statements
        @return a ParseTree that represents the series of statements
        """
        newparsed = ParseTree("statements", "")
        
        for i in range(self.iterator, len(self.token_array)): # iterating until we do not have a token in the statements list
            
            if    (self.token_array[i] not in self.statements):
                self.iterator = i
                break;
            
            else:
                self.iterator = i # updating iterator to be the current token
                if      (self.token_array[i].value == "let"):
                    newparsed.addChild(compileLet())

                elif    (self.token_array[i].value == "do"):
                    newparsed.addChild(compileDo())

                elif    (self.token_array[i].value == "while"):
                    newparsed.addChild(compileWhile())

                elif    (self.token_array[i].value == "return"):
                    newparsed.addChild(compileReturn())

                elif    (self.token_array[i].value == "if"):
                    newparsed.addChild(compileIf())

                i = self.iterator # updating i to be the current token


        return newparsed 
    
    
    def compileLet(self):
        """
        Generates a parse tree for a let statement
        @return a ParseTree that represents the statement
        """
        newparsed = ParseTree("lets", "")
        newparsed.addChild(self.token_array[self.iterator])
        newparsed.addChild(self.token_array[self.iterator+1])

        if    (self.token_array[self.iterator+2].value == "["):
            newparsed.addChild("symbol", "[")
            self.iterator += 3
            newparsed.addChild(compileExpression())
            newparsed.addChild("symbol", "]")
        else:
            if    (self.token_array[self.iterator+2] != "[" and self.token_array[self.iterator+2] != "="):
                raise ParseException; return None; #just in case
        
        newparsed.addChild(self.token_array[self.iterator]) # iterator should be updated from the compile expression function
        self.iterator += 1
        
        newparsed.addChild(compileExpression())
        newparsed.addChild(self.token_array[self.iterator]) # iterator should be updated from the compile expression function


        return newparsed 


    def compileIf(self):
        """
        Generates a parse tree for an if statement
        @return a ParseTree that represents the statement
        """
        newparsed = ParseTree("ifs", "")

        newparsed.addChild(self.token_array[self.iterator])
        newparsed.addChild(self.token_array[self.iterator+1]); self.iterator += 1
        newparsed.addChild(compileExpression())
        newparsed.addChild(self.token_array[self.iterator])
        newparsed.addChild(self.token_array[self.iterator+1])

        self.iterator += 1
        for i in range(self.iterator, len(self.token_array)):
            if    (self.token_array[i].value == "}"): break;
            else: 
                if    (self.token_array[i].value not in self.statements):
                    raise ParseException
                else:
                    self.iterator = i # updating the iterator
                    newparsed.addChild(compileStatements())
                    
                    i = self.iterator
        newparsed.addChild(self.token_array[self.iterator])

        return newparsed 

    
    def compileWhile(self):
        """
        Generates a parse tree for a while statement
        @return a ParseTree that represents the statement
        """
        newparsed = ParseTree("whiles", "")
        return None 


    def compileDo(self):
        """
        Generates a parse tree for a do statement
        @return a ParseTree that represents the statement
        """
        newparsed = ParseTree("does", "")
        return None 


    def compileReturn(self):
        """
        Generates a parse tree for a return statement
        @return a ParseTree that represents the statement
        """
        newparsed = ParseTree("return", "")
        return None 


    def compileExpression(self):
        """
        Generates a parse tree for an expression
        @return a ParseTree that represents the expression
        """
        newparsed = ParseTree("expressions", "")
        return None 


    def compileTerm(self):
        """
        Generates a parse tree for an expression term
        @return a ParseTree that represents the expression term
        """
        newparsed = ParseTree("terms", "")
        return None 


    def compileExpressionList(self):
        """
        Generates a parse tree for an expression list
        @return a ParseTree that represents the expression list
        """
        newparsed = ParseTree("expression_lists", "")
        return None 


    def next(self):
        """
        Advance to the next token
        """
        newparsed = ParseTree("nexts", "")
        return


    def current(self):
        """
        Return the current token
        @return the token
        """
        newparsed = ParseTree("currents", "")
        return None


    def have(self,expectedType,expectedValue):
        """
        Check if the current token matches the expected type and value.
        @return True if a match, False otherwise
        """
        # where does this token live?
        return False


    def mustBe(self,expectedType,expectedValue): # idk what the point of this function and the prior one is, they are pretty useless lmaooooo
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
