#include "salad.h"
#include "food.h"
#include <iostream>
using namespace std;

Salad::Salad(double p, int cal, string n, string d, bool c):Food(p,cal, n){
    dressing = d;
    croutons = c;
}
void Salad::printOrder(bool theBool){
    if(theBool == true){
        cout<<"You ordered the "<<this->getName()<<" with "<<dressing<<" dressing with croutons"<<endl;
        this->setCal(getCal()+130);
        cout<<this->getCal()<<" calories"<<endl;
    } else{
        cout<<"You ordered the "<<this->getName()<<" with "<<dressing<<" dressing without croutons"<<endl;
        cout<<this->getCal()<<" calories"<<endl;
    }
}
