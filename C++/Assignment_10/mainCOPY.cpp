#include <iostream>

using namespace std;

class Food{
private:
    double price; //each entree has a price
    int calories;
    string name; //the name of the dish
public:
    Food(double p, int cal, string n){
        price = p;
        calories = cal;
        name = n;
    }
    double getPrice(){
        return price;
    }
    void setCal(int cal){
        calories = cal;
    }
    int getCal(){
        return calories;
    }
    string getName(){
        return name;
    }
};

class Steak:public Food{
private:
    string temp; //temperature they'd like their steak cooked
    bool A1;
public:
    Steak(double p, int cal, string n, string cook, bool a1):Food(p,cal, n){
        temp = cook;
        A1 = a1;
    }
    void printOrder(bool theBool){
        if(theBool == true){
            cout<<"You ordered the "<<this->getName()<<" cooked "<<temp<<" with A1 steak sauce"<<endl;
            this->setCal(getCal()+110);
            cout<<this->getCal()<<" calories"<<endl;
        } else{
            cout<<"You ordered the "<<this->getName()<<" cooked "<<temp<<" without A1 steak sauce"<<endl;
            cout<<this->getCal()<<" calories"<<endl;
        }
    }
};

class Fish:public Food{
private:
    string sauce; //They can choose WHATEVER SAUCE they want
    bool filet;
public:
    Fish(double p, int cal, string n, string s, bool f):Food(p,cal, n){
        sauce = s;
        filet = f;
    }
    void printOrder(bool theBool){
        if(theBool == true){
            cout<<"You ordered the "<<this->getName()<<" filleted, with "<<sauce<<" sauce"<<endl;
            cout<<this->getCal()<<" calories"<<endl;
        } else{
            cout<<"You ordered the "<<this->getName()<<" no fillet, with "<<sauce<<" sauce"<<endl;
            cout<<this->getCal()<<" calories"<<endl;
        }
    }
};

class Salad:public Food{
private:
    string dressing;
    bool croutons;
public:
    Salad(double p, int cal, string n, string d, bool c):Food(p,cal, n){
        dressing = d;
        croutons = c;
    }
    void printOrder(bool theBool){
        if(theBool == true){
            cout<<"You ordered the "<<this->getName()<<" with "<<dressing<<" dressing with croutons"<<endl;
            this->setCal(getCal()+130);
            cout<<this->getCal()<<" calories"<<endl;
        } else{
            cout<<"You ordered the "<<this->getName()<<" with "<<dressing<<" dressing without croutons"<<endl;
            cout<<this->getCal()<<" calories"<<endl;
        }
    }
};

bool getBool(string userInput){
    bool theBool;
    if(userInput == "y" or userInput == "Y"){
        theBool = true;
    } else{
        theBool = false;
    }
    return theBool;
}

int main()
{
    cout<<"Welcome to Austin's Computationally Fine Dining Restaurant! Here you enter your orders without hassling with waiting around for a waiter."<<endl; //Intro
    cout<<"Here's tonight's menu: "<<endl; //The Menu
    cout<<"Fire-grilled 13 oz. Angus Steak - $17.25 (steak)"<<endl;
    cout<<"Gourmet scrumptious House Salad - $8.75 (salad)"<<endl;
    cout<<"Fire-grilled Colorado river-run Salmon - $13.50 (salmon)"<<endl;
    cout<<" "<<endl;

    int numPeople; // number of orders that will be taken
    cout<<"How many people will be dining?: ";
    cin>>numPeople;

    double tab = 0; //This will be the party's total tab at the end
    int calCount = 0; //Total calorie count to remind people at the end how many calories they're eating
    int personCounter = 1;

    while(numPeople>0){
        string diningChoice; //This is where each user inputs their
        cout<<"What would person "<<personCounter<<" like? ";
        cin>>diningChoice;

        string attribute1 = "nothing";
        bool theBool = false;
        string yesOrNo = "n";

        if(diningChoice == "steak"){
            cout<<"How would you like your steak cooked? (no spaces) "<<endl;
            cout<<"rare, medium-rare, medium, medium-well, well-done: ";
            cin>>attribute1;

            cout<<"Would you like A1 sauce? (y/n): ";
            cin>>yesOrNo;
            theBool = getBool(yesOrNo);

            Steak order(17.25, 1025, "Angus Steak", attribute1, theBool);
            order.printOrder(theBool);

            tab += order.getPrice();
            calCount += order.getCal();

        }else if(diningChoice == "salmon"){
            cout<<"What sauce would your like with your salmon? (no spaces) "<<endl;
            cout<<"herb-butter, creamy-dill, mustard-wine, no: ";
            cin>>attribute1;

            cout<<"Would you like your salmon filleted? (y/n): ";
            cin>>yesOrNo;

            theBool = getBool(yesOrNo);

            Fish order(13.50, 769, "Grilled Salmon", attribute1, theBool);
            order.printOrder(theBool);

            tab += order.getPrice();
            calCount += order.getCal();

        } else if (diningChoice == "salad"){
            cout<<"What salad dressing would you like? (no spaces) "<<endl;
            cout<<"Ranch, Caesar, Italian, Vinaigrette, no: ";
            cin>>attribute1;

            cout<<"Would you like croutons? (y/n): ";
            cin>>yesOrNo;

            theBool = getBool(yesOrNo);

            Salad order(8.75, 525, "House Salad", attribute1, theBool);
            order.printOrder(theBool);

            tab += order.getPrice();
            calCount += order.getCal();
        }else{
            cout<<"The input you gave isn't on the menu, please try again"<<endl;
            ++numPeople;
            --personCounter;
        }
        cout<<" "<<endl;
        ++personCounter;
        --numPeople;
    }
    cout<<" "<<endl;
    cout<<"Your food will be out shortly! Your bill is : $"<<tab*1.08<<endl;
    cout<<"Total calorie consumption is: "<<calCount<<" calories, congrats!"<<endl;

    string anotherOrder;
    cout<<"Place another order? (y/n): ";
    cin>>anotherOrder;
    while(anotherOrder == "y"){
        cout<<" "<<endl;
        main();
    }

    return 0;
}
