#include "food.h"
#include <iostream>
using namespace std;

Food::Food(double p, int cal, string n){
    price = p;
    calories = cal;
    name = n;
}
double Food::getPrice(){
    return price;
}
void Food::setCal(int cal){
    calories = cal;
}
int Food::getCal(){
    return calories;
}
string Food::getName(){
    return name;
}
