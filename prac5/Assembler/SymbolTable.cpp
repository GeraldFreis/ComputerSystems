#include "SymbolTable.h"

#include <string>
#include <unordered_map>

/**
 * Symbol Table constructor
 */
SymbolTable::SymbolTable() {
    std::unordered_map<std::string, uint16_t> table;

    
    // other registers
    table.insert(std::pair<std::string, uint16_t>("R0", 0));
    table.insert(std::pair<std::string, uint16_t>("R1", 1));
    table.insert(std::pair<std::string, uint16_t>("R2", 2));
    table.insert(std::pair<std::string, uint16_t>("R3", 3));
    table.insert(std::pair<std::string, uint16_t>("R4", 4));
    table.insert(std::pair<std::string, uint16_t>("R5", 5));
    table.insert(std::pair<std::string, uint16_t>("R6", 6));
    table.insert(std::pair<std::string, uint16_t>("R7", 7));
    table.insert(std::pair<std::string, uint16_t>("R8", 8));
    table.insert(std::pair<std::string, uint16_t>("R9", 9));
    table.insert(std::pair<std::string, uint16_t>("R10", 10));
    table.insert(std::pair<std::string, uint16_t>("R11", 11));
    table.insert(std::pair<std::string, uint16_t>("R12", 12));
    table.insert(std::pair<std::string, uint16_t>("R13", 13));
    table.insert(std::pair<std::string, uint16_t>("R14", 14));
    table.insert(std::pair<std::string, uint16_t>("R15", 15));

    counter = 16;

    // predefined symbols
    table.insert(std::pair<std::string, uint16_t>("KBD", 24576));
    table.insert(std::pair<std::string, uint16_t>("SCREEN", 16384));
    table.insert(std::pair<std::string, uint16_t>("SP", 0));
    table.insert(std::pair<std::string, uint16_t>("LCL", 1));
    table.insert(std::pair<std::string, uint16_t>("ARG", 2));
    table.insert(std::pair<std::string, uint16_t>("THIS", 3));
    table.insert(std::pair<std::string, uint16_t>("THAT", 4));

}

/**
 * Symbol Table destructor
 */
// SymbolTable::~SymbolTable() {
//     // Your code here
// }

/**
 * Adds a symbol to the symbol table
 * @param symbol The name of the symbol
 * @param value The address for the symbol
 */
void SymbolTable::addSymbol(string symbol, uint16_t value) {
    if(table.count(symbol) > 0){return;}
    std::pair<std::string, uint16_t> thispair (symbol, value);
    table.insert(thispair);
}

/**
 * Gets a symbol from the symbol table
 * @param symbol The name of the symbol
 * @return The address for the symbol or -1 if the symbol isn't in the table
 */
int SymbolTable::getSymbol(string symbol) {
    // getting the iterator to the item
    std::unordered_map<std::string, uint16_t>::const_iterator iter = table.find(symbol);
    if(iter == table.end()){return -1;}
    else {return iter->second;} // returns the binary value from the symbol table
    
    return -1;
}