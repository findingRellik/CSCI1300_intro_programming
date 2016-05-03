#ifndef FISH_H_INCLUDED
#define FISH_H_INCLUDED
#include "food.h"
#include <iostream>
using namespace std;

class Fish:public Food{
private:
    string sauce; //They can choose WHATEVER SAUCE they want
    bool filet;
public:
    Fish(double p, int cal, string n, string s, bool f);
    void printOrder(bool theBool);
};

#endif // FISH_H_INCLUDED
