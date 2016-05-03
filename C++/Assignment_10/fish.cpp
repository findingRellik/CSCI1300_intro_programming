#include "fish.h"
#include "food.h"
#include <iostream>
using namespace std;

Fish::Fish(double p, int cal, string n, string s, bool f):Food(p,cal, n){
    sauce = s;
    filet = f;
}
void Fish::printOrder(bool theBool){
    if(theBool == true){
        cout<<"You ordered the "<<getName()<<" filleted, with "<<sauce<<" sauce"<<endl;
        cout<<this->getCal()<<" calories"<<endl;
    } else{
        cout<<"You ordered the "<<getName()<<" no fillet, with "<<sauce<<" sauce"<<endl;
        cout<<this->getCal()<<" calories"<<endl;
    }
}

