//Austin Metzner section 104 Melissa Bica FINAL
#include <iostream>

using namespace std;

class BugCollection{
private:
    int ants;
    int flies;
    int spiders;
public:
    BugCollection(int a, int f, int s){ //Sets initial values, constructor
        ants = a;
        flies = f;
        spiders = s;
    }

    void addBug(int bugType){ //increments number of bug by 1
        if(bugType == 1){
            ants += 1;
        } else if(bugType == 2){
            flies += 1;
        } else if(bugType == 3){
            spiders += 1;
        } else{
            cout<<"Invalid input"<<endl;
        }
    }

    void removeBug(int bugType){ //decrements the number of bugs by one
        if(bugType == 1){
            ants -=1;
        } else if(bugType == 2){
            flies -= 1;
        } else if(bugType == 3){
            spiders -= 1;
        } else{
            cout<<"Invalid input"<<endl;
        }
    }
    void printBugCollection(){ //prints the private variables
        cout<<"Number of ants is "<<ants<<endl;
        cout<<"Number of flies is "<<flies<<endl;
        cout<<"Number of spiders is "<<spiders<<endl;
    }
};

void findMinMax(int nums[], int *maxVal, int *minVal){
    for(int i = 0; i<10; i++){//for loop to go through and determine an set the max val (same with the next for loop but for min)
        if(nums[i]>*maxVal){
            *maxVal = nums[i];
        }
    }
    cout<<"Max value is "<<*maxVal<<endl;//displays max value after for loop runs//
    for(int i = 0; i<10; i++){
        if(nums[i]<*minVal){
            *minVal = nums[i];
        }
    }
    cout<<"Min value is "<<*minVal<<endl;
}

int main()
{
    //Calling bugCollection
    BugCollection billy(3,2,4);//3 ants, 2 flies, and 4 spiders, calling constructor
    billy.addBug(1);// adds one ant to his collection
    billy.printBugCollection();// prints current bug collection
    billy.removeBug(3); // removes one spider from his collection
    billy.printBugCollection();

    //calling void find Max
    int Max = -99999999;//Low number so numbers in array can be considered a maximum above it
    int Min = 99999999;// Likewise a high number so numbers in array can be considered a minimum
    int *maxVal = &Max;//pointers to go into the function
    int *minVal = &Min;
    int nums[10]={0,1,2,3,4,5,6,7,8,9};// the array of numbers to have to be checked for mins and maxs

    findMinMax(nums, maxVal, minVal);//will out put the minimum and maximum values, pointers point to Max and Min

    return 0;
}
