#ifndef SALAD_H_INCLUDED
#define SALAD_H_INCLUDED
#include "food.h"
#include <iostream>
using namespace std;

class Salad:public Food{
private:
    string dressing;
    bool croutons;
public:
    Salad(double p, int cal, string n, string d, bool c);
    void printOrder(bool theBool);
};

#endif // SALAD_H_INCLUDED
