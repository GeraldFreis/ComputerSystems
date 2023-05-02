#include "Assembler.h"
#include "SymbolTable.h"

#include <string>

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
}

/**
 * Assembler second pass; Translates a set of instructions to machine code.
 * @param instructions An array of the assembly language instructions to be converted to machine code.
 * @param symbolTable The symbol table to reference/update.
 * @return A string containing the generated machine code as lines of 16-bit binary instructions.
 */
string Assembler::generateMachineCode(SymbolTable* symbolTable, string instructions[], int numOfInst) {
    // Your code here
    return "";
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
    for(int i = 0; i < instruction.size(); i++){if(instruction.at(i) == '='){deststring = instruction.substr(0, i+1);}}
    
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
    return "";
}

/**
 * Generates the binary bits of the dest part of a C-instruction
 * @param dest The destination of the instruction
 * @return A string containing the 3 binary dest bits that correspond to the given dest value.
 */
string Assembler::translateDest(InstructionDest dest) {
    // Your code here:
    return "000";
}

/**
 * Generates the binary bits of the jump part of a C-instruction
 * @param jump The jump condition for the instruction
 * @return A string containing the 3 binary jump bits that correspond to the given jump value.
 */
string Assembler::translateJump(InstructionJump jump) {
    // Your code here:
    return "000";
}

/**
 * Generates the binary bits of the computation/op-code part of a C-instruction
 * @param comp The computation/op-code for the instruction
 * @return A string containing the 7 binary computation/op-code bits that correspond to the given comp value.
 */
string Assembler::translateComp(InstructionComp comp) {
    // Your code here:
    return "0000000";
}

/**
 * Generates the binary bits for an A-instruction, parsing the value, or looking up the symbol name.
 * @param symbol A string containing either a label name, a variable name, or a constant integer value
 * @param symbolTable The symbol table for looking up label/variable names
 * @return A string containing the 15 binary bits that correspond to the given sybmol.
 */
string Assembler::translateSymbol(string symbol, SymbolTable* symbolTable) {
    // Your code here:
    return "0000000000000000";
}
