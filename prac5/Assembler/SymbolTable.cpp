#include "SymbolTable.h"

#include <string>

/**
 * Symbol Table constructor
 */
SymbolTable::SymbolTable() {
    std::unordered_map<std::string, uint16_t> table;
}

// /**
//  * Symbol Table destructor
//  */
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
    table.emplace(symbol, value);
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
    else {return iter->second;}
    
    return -1;
}