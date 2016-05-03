#ifndef FOOD_H_INCLUDED
#define FOOD_H_INCLUDED
#include <iostream>
using namespace std;

class Food{
private:
    double price; //each entree has a price
    int calories;
    string name; //the name of the dish
public:
    Food(double p, int cal, string n);
    double getPrice();
    void setCal(int cal);
    int getCal();
    string getName();
};


#endif // FOOD_H_INCLUDED
