#ifndef SYMBOL_TABLE_H
#define SYMBOL_TABLE_H

#include <cstdint>  // this contains uint16_t
#include <unordered_map>      // indexable dictionary
#include <string>   // process c++ string

using namespace std;

class SymbolTable {
    private:
        std::unordered_map<std::string, uint16_t> table;
   public:
    SymbolTable();
    //~SymbolTable();

    void addSymbol(string symbol, uint16_t value);
    int getSymbol(string symbol);
};

#endif /* SYMBOL_TABLE_H */