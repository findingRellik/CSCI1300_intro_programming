#ifndef STEAK_H_INCLUDED
#define STEAK_H_INCLUDED
#include "food.h"
#include <iostream>
using namespace std;

class Steak:public Food{
private:
    string temp; //temperature they'd like their steak cooked
    bool A1;
public:
    Steak(double p, int cal, string n, string cook, bool a1);
    void printOrder(bool theBool);
};

#endif // STEAK_H_INCLUDED
