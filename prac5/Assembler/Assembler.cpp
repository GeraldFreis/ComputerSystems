#include "Assembler.h"
#include "SymbolTable.h"
#include <iostream>

#include <string>

std::string binaryCLIenT(int a){
    int value = a;
    std::string binary = "";
    while(value > 0){
        int remainder = value % 2;
        if(remainder != 0){binary += "1";}
        else {binary += "0";}
        value /= 2;
        std::cout << value << "\n";
    }
    // binary += "1";

    std::string reversed = "";
    for(int i = 0; i < binary.size();i++){
        reversed += binary.at(binary.size() - 1 - i);
    }
    for(int i = reversed.size(); i < 16; i++){
        reversed = "0" + reversed; // preprending 0's on
    }
    return reversed;

}

using namespace std;

/**
 * Assembler constructor
 */
Assembler::Assembler() {
    // Your code here
}

/**
 * Assembler destructor
 */
Assembler::~Assembler() {
    // Your code here
}

/**
 * Assembler first pass; populates symbol table with label locations.
 * @param instructions An array of the assembly language instructions.
 * @param symbolTable The symbol table to populate.
 */
void Assembler::buildSymbolTable(SymbolTable* symbolTable, string instructions[], int numOfInst) {
    // Your code here
    uint16_t counter = 0;
    for(int i = 0; i < numOfInst; i++){
        if(parseInstructionType(instructions[i]) == A_INSTRUCTION){
            symbolTable->addSymbol(Assembler::parseSymbol(instructions[i]), counter);
            counter++;
        }
    }
}

/**
 * Assembler second pass; Translates a set of instructions to machine code.
 * @param instructions An array of the assembly language instructions to be converted to machine code.
 * @param symbolTable The symbol table to reference/update.
 * @return A string containing the generated machine code as lines of 16-bit binary instructions.
 */
string Assembler::generateMachineCode(SymbolTable* symbolTable, string instructions[], int numOfInst) {
    std::string lines; int counter = 0;
    int instruction_counter = 0;

    for(int i = 0; i < numOfInst; i++){
        Assembler::InstructionType type=parseInstructionType(instructions[i]);
        if(type==A_INSTRUCTION){
            // returning the address if it is a number
            std::string actual_instruction = instructions[i].substr(1, instructions[i].size());
            if(actual_instruction.at(0) >= 'a' && actual_instruction.at(0)<= 'z'){
                symbolTable->addSymbol(actual_instruction, instruction_counter);
                if(counter != 0){
                    lines = lines + " " + translateSymbol(actual_instruction, symbolTable); }
                else {lines = translateSymbol(actual_instruction, symbolTable); counter++;}
            }
            else if(actual_instruction.at(0) >= 'A' && actual_instruction.at(0)<= 'Z'){
                symbolTable->addSymbol(actual_instruction, i+1);
                if(counter != 0){
                  lines = lines + " " + translateSymbol(actual_instruction, symbolTable);  
                }
                else {lines = translateSymbol(actual_instruction, symbolTable); counter++;}}
            else{
                if(counter != 0) {lines = lines + " " + binaryCLIenT(std::stoi(actual_instruction));}
                else {lines = binaryCLIenT(std::stoi(actual_instruction)); counter++;}}


        } else if(type==C_INSTRUCTION){
            Assembler::InstructionDest destination = parseInstructionDest(instructions[i]);
            // std::cout << destination << "\n\n";
            std::string dest = translateDest(destination);

            Assembler::InstructionComp computation = parseInstructionComp(instructions[i]);
            std::string comp = translateComp(computation);
            std::string returnval = "111" + comp + dest;
            // std::cout << dest << "\n";
            Assembler::InstructionJump jump = parseInstructionJump(instructions[i]);
            returnval += translateJump(jump);
            if(counter != 0){
                lines = lines + " " + returnval; 
            } else {lines = returnval;counter++;}

        } else {continue;}
    }
    return lines;
}

/**
 * Parses the type of the provided instruction
 * @param instruction The assembly language representation of an instruction.
 * @return The type of the instruction (A_INSTRUCTION, C_INSTRUCTION, L_INSTRUCTION, NULL)
 */
Assembler::InstructionType Assembler::parseInstructionType(string instruction) {
    // Your code here:
    if(instruction.at(0) == '@'){return A_INSTRUCTION;}
    else{return C_INSTRUCTION;}

    return NULL_INSTRUCTION;
}

/**
 * Parses the destination of the provided C-instruction
 * @param instruction The assembly language representation of a C-instruction.
 * @return The destination of the instruction (A, D, M, AM, AD, MD, AMD, NULL)
 */
Assembler::InstructionDest Assembler::parseInstructionDest(string instruction) {
    std::string deststring;
    //getting the stuff before the equal sign
    for(int i = 0; i < instruction.size(); i++){if(instruction.at(i) == '='){deststring = instruction.substr(0, i); break;}}
    // std::cout << deststring << "\n";
    if(deststring == "A"){return A;}
    else if(deststring == "AM"){return AM;}
    else if(deststring == "AMD"){return AMD;}
    else if(deststring == "D"){return D;}
    else if(deststring == "AD"){return AD;}
    else if(deststring == "M"){return M;}
    else if(deststring == "MD"){return MD;}
    // if the destination was not any of the actual destinations
    // Your code here:
    return NULL_DEST;
}

/**
 * Parses the jump condition of the provided C-instruction
 * @param instruction The assembly language representation of a C-instruction.
 * @return The jump condition for the instruction (JLT, JGT, JEQ, JLE, JGE, JNE, JMP, NULL)
 */
Assembler::InstructionJump Assembler::parseInstructionJump(string instruction) {
    // Your code here:
    // for example if "JLT" appear at the comp field return enum label JLT
    if (instruction.find("JLT") != string::npos) {
        return JLT;
    } else if(instruction.find("JGT") != string::npos){return JGT;}
    else if(instruction.find("JGE") != string::npos){return JGE;}
    else if(instruction.find("JLE") != string::npos){return JLE;}
    else if(instruction.find("JEQ") != string::npos){return JEQ;}
    else if(instruction.find("JNE") != string::npos){return JNE;}
    else if(instruction.find("JMP") != string::npos){return JGT;}
    return NULL_JUMP;
}

/**
 * Parses the computation/op-code of the provided C-instruction
 * @param instruction The assembly language representation of a C-instruction.
 * @return The computation/op-code of the instruction (CONST_0, ... ,D_ADD_A , ... , NULL)
 */
Assembler::InstructionComp Assembler::parseInstructionComp(string instruction) {
    // Your code here:
    // for example if "0" appear at the comp field return CONST_0
    if (instruction.find("0") != string::npos) {
        return CONST_0;
    }  else if(instruction.find("D+1") != string::npos){
        return D_ADD_1;
    }  else if(instruction.find("D+A") != string::npos){
        return D_ADD_A;
    } else if(instruction.find("D+M") != string::npos){
        return D_ADD_M;
    } else if(instruction.find("D-1") != string::npos){
        return D_SUB_1;
    } else if(instruction.find("D-A") != string::npos){
        return D_SUB_A;
    }  else if(instruction.find("D-M") != string::npos){
        return D_SUB_M;
    }  else if(instruction.find("-D") != string::npos){
        return NEG_D;
    }  else if(instruction.find("-A") != string::npos){
        return NEG_A;
    } else if(instruction.find("-M") != string::npos){
        return NEG_M;
    } else if(instruction.find("A+1") != string::npos){
        return A_ADD_1;
    }   else if(instruction.find("A-1") != string::npos){
        return A_SUB_1;
    } else if(instruction.find("A-D") != string::npos){
        return A_SUB_D;
    } else if(instruction.find("M+1") != string::npos){
        return M_ADD_1;
    }  else if(instruction.find("M-1") != string::npos){
        return M_SUB_1;
    } else if(instruction.find("M-D") != string::npos){
        return M_SUB_D;
    }  else if(instruction.find("!M") != string::npos){
        return NOT_M;
    }  else if(instruction.find("!D") != string::npos){
        return NOT_D;
    }  else if(instruction.find("!A") != string::npos){
        return NOT_A;
    }  else if(instruction.find("D&A") != string::npos){
        return D_AND_A;
    } else if(instruction.find("D&M") != string::npos){
        return D_AND_M;
    }  else if(instruction.find("D|A") != string::npos){
        return D_OR_A;
    }  else if(instruction.find("D|M") != string::npos){
        return D_OR_M;
    } else if(instruction.find("1") != string::npos){
        return CONST_1;
    } else if(instruction.find("-1") != string::npos){
        return CONST_NEG_1;
    } else if(instruction.find("A") != string::npos){
        return VAL_A;
    } else if(instruction.find("D") != string::npos){
        return VAL_D;
    } else if (instruction.find("M") != string::npos){
        return VAL_M;
    }
    return NULL_COMP;
}

/**
 * Parses the symbol of the provided A/L-instruction
 * @param instruction The assembly language representation of a A/L-instruction.
 * @return A string containing either a label name (L-instruction),
 *         a variable name (A-instruction), or a constant integer value (A-instruction)
 */
string Assembler::parseSymbol(string instruction) {

    // adding the symbol to the table
    return "";
}

/**
 * Generates the binary bits of the dest part of a C-instruction
 * @param dest The destination of the instruction
 * @return A string containing the 3 binary dest bits that correspond to the given dest value.
 */
string Assembler::translateDest(InstructionDest dest) {
    if(dest == M){return "001";}
    else if(dest == D){return "010";}
    else if(dest == A){return "100";}
    else if(dest == MD){return "011";}
    else if(dest == AM){return "101";}
    else if(dest == AD){return "110";}
    else if(dest == AMD){return "111";}
    return "000";
}

/**
 * Generates the binary bits of the jump part of a C-instruction
 * @param jump The jump condition for the instruction
 * @return A string containing the 3 binary jump bits that correspond to the given jump value.
 */
string Assembler::translateJump(InstructionJump jump) {
    if(jump == JGT){return "001";}
    else if(jump == JEQ){return "010";}
    else if(jump == JGE){return "011";}
    else if(jump == JLT){return "100";}
    else if(jump == JNE){return "101";}
    else if(jump == JLE){return "110";}
    else if(jump == JMP){return "111";}
    return "000";
}

/**
 * Generates the binary bits of the computation/op-code part of a C-instruction
 * @param comp The computation/op-code for the instruction
 * @return A string containing the 7 binary computation/op-code bits that correspond to the given comp value.
 */
string Assembler::translateComp(InstructionComp comp) {
    if(comp == CONST_0){return "0101010";}
    else if(comp == CONST_1){return "0111111";}
    else if(comp == CONST_NEG_1){return "0111010";}
    else if(comp == VAL_D){return "0001100";}
    else if(comp == VAL_A){return "0110000";}
    else if(comp == NOT_D){return "0001101";}
    else if(comp == NOT_A){return "0110001";}
    else if(comp == NEG_D){return "0001111";}
    else if(comp == NEG_A){return "0110011";}
    else if(comp == D_ADD_1){return "0011111";}
    else if(comp == A_ADD_1){return "0110111";}
    else if(comp == D_SUB_1){return "0001110";}
    else if(comp == A_SUB_1){return "0110010";}
    else if(comp == D_ADD_A){return "0000010";}
    else if(comp == D_SUB_A){return "0010011";}
    else if(comp == A_SUB_D){return "0000111";}
    else if(comp == D_AND_A){return "0000000";}
    else if(comp == D_OR_A){return "0010101";}
    else if(comp == VAL_M){return "1110000";}
    else if(comp == NOT_M){return "1110001";}
    else if(comp == NEG_M){return "1110011";}
    else if(comp == M_ADD_1){return "1110111";}
    else if(comp == M_SUB_1){return "1110010";}
    else if(comp == D_ADD_M){return "1000010";}
    else if(comp == D_SUB_M){return "1100011";}
    else if(comp == M_SUB_D){return "1000111";}
    else if(comp == D_AND_M){return "1000000";}
    else if(comp == D_OR_M){return "1010101";}
    return "0000000";
}




/**
 * Generates the binary bits for an A-instruction, parsing the value, or looking up the symbol name.
 * @param symbol A string containing either a label name, a variable name, or a constant integer value
 * @param symbolTable The symbol table for looking up label/variable names
 * @return A string containing the 15 binary bits that correspond to the given sybmol.
 */
string Assembler::translateSymbol(string symbol, SymbolTable* symbolTable) {
    if(symbol.at(0) == 'R'){ // we point to a predefined address
        int val = std::stoi(symbol.substr(1, symbol.size())); // converting to my balls
        // now we can convert this number to binary
        return binaryCLIenT(val);
    }
    if(symbol.at(0) >= '1' && symbol.at(0) <= '9'){ // if the symbol is just an address we vibing
        // now I work some binary magic on my nuts
        return binaryCLIenT(std::stoi(symbol));
    } 
    int symbolval = symbolTable->getSymbol(symbol);
    if(symbolval != -1){return binaryCLIenT(symbolval);}


    return "0000000000000000";
}
