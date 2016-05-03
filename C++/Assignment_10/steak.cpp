#include "steak.h"
#include "food.h"
#include <iostream>
using namespace std;

Steak::Steak(double p, int cal, string n, string cook, bool a1):Food(p,cal, n){
    temp = cook;
    A1 = a1;
}
void Steak::printOrder(bool theBool){
    if(theBool == true){
        cout<<"You ordered the "<<this->getName()<<" cooked "<<temp<<" with A1 steak sauce"<<endl;
        this->setCal(getCal()+110);
        cout<<this->getCal()<<" calories"<<endl;
    } else{
        cout<<"You ordered the "<<this->getName()<<" cooked "<<temp<<" without A1 steak sauce"<<endl;
        cout<<this->getCal()<<" calories"<<endl;
    }
}
