#include <QCoreApplication>
#include <iostream>
using namespace std;

//review question 1
double gradeCalculator(double hwAvg, double prjAvg, double recAvg, double examAvg){
    double finalGrade = 0.0;
    finalGrade = (hwAvg * 0.30) + (prjAvg * 0.10) + (recAvg * 0.10) + (examAvg * 0.50);
    return finalGrade;
}
//review question 2
void gradeCalculatorWPointers(double *finalGrade, double hwAvg, double prjAvg, double recAvg, double examAvg){
    *finalGrade = (hwAvg * 0.30) + (prjAvg * 0.10) + (recAvg * 0.10) + (examAvg * 0.50);
}
//review question 3
void gradeCalculatorWArrays(double *finalGrade, double vars[]){
    //vars is hw, prj, rec, exam
    *finalGrade = (vars[0] * 0.30) + (vars[1] * 0.10) + (vars[2] * 0.10) + (vars[3] * 0.50);

}
//review question 5
void swap(double *n1, double *n2){
    int temp;
    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
}
//review question 6
class Time{
private:
    int hours;
    int minutes;
    int seconds;
public:
    Time(int h, int m, int s){
        hours = h;
        minutes = m;
        seconds = s;
    }
    Time(int totalSeconds){
        //Divide by 3600 to get the number of hours
        hours = totalSeconds / 3600;

        //Use the mod operator on seconds to get what is left
        totalSeconds = totalSeconds % 3600;

        //Divide the remaining seconds by 60 to get the number of minutes
        minutes = totalSeconds / 60;

        //Use the mod operator on seconds to get what is left
        seconds = totalSeconds % 60;

    //Cast everything back to an int to display whole numbers
    //hours = int(hours)
    //minutes = int(minutes)
    }
    void displayTime(){
        cout<<"hours: "<<hours<<endl;
        cout<<"minutes: "<<minutes<<endl;
        cout<<"seconds: "<<seconds<<endl;

    }

};
//review question 7
class Food{
private:
    string foodType;
    string foodCategory;
public:
    Food(string ft, string fc){
        foodType = ft;
        foodCategory = fc;

    }
    Food(){} //needed for array
    void setFoodType(string ft){
        foodType = ft;
    }
    void setFoodCategory(string fc){
        foodCategory = fc;
    }
    string getFoodType(){
        return foodType;
    }
    string getFoodCategory(){
        return foodCategory;
    }
};
//review question 8
struct Birthdate{
    int month;
    int day;
    int year;
};
//review question 9
struct WeatherPoint{
    int temperature;
    int windSpeed;
    int humidity;

};

int main(int argc, char *argv[])
{
    //review question 1
    double finalGrade = gradeCalculator(90, 80, 85, 95);
    cout<<finalGrade<<endl;

    //review question 2
    double *ptrFinalGrade = &finalGrade;
    gradeCalculatorWPointers(ptrFinalGrade, 90, 80, 85, 90);
    cout<<*ptrFinalGrade<<endl;

    //review question 3
    double gradeVariables[4];
    gradeVariables[0] = 90;
    gradeVariables[1] = 100;
    gradeVariables[2] = 80;
    gradeVariables[3] = 94;
    gradeCalculatorWArrays(ptrFinalGrade, gradeVariables);
    cout<<*ptrFinalGrade<<endl;

    //review question 4
    int miles[] = {15, 22, 16, 18, 27, 23, 20};
    int milesCopy[7];
    for(int i = 0; i < 7; i++){
        milesCopy[i] = miles[i];
        cout<<milesCopy[i]<<endl;
    }

    //review question 5
    int number1 = 6;
    int number2 = 60;
    int *ptrNumber1 = &number1;
    int *ptrNumber2 = &number2;

    swap(ptrNumber1, ptrNumber2);
    cout<<"number 1="<<*ptrNumber1<<" and number 2="<<*ptrNumber2<<endl;

    //review question 6
    Time myTime(70000);
    myTime.displayTime();
    Time myTime2(5, 50, 6);
    myTime2.displayTime();

    //review question 7
    Food myFood[10]; //uses no arguments constructor
    string tempFoodType;
    string tempFoodCat;
    for(int i = 0; i < 10; i++){
        cout<<"enter a food type: ";
        getline(cin, tempFoodType);
        myFood[i].setFoodType(tempFoodType);

        cout<<"enter a food category: ";
        getline(cin, tempFoodCat);
        myFood[i].setFoodCategory(tempFoodCat);

    }
    //print food information
    for(int i = 0; i < 10; i++){
        cout<<myFood[i].getFoodType()<<endl;
        cout<<myFood[i].getFoodCategory()<<endl;
    }
    //review question 8
    Birthdate myBirthdate;
    myBirthdate.day = 4;
    myBirthdate.month = 1;
    myBirthdate.year = 2000;
    cout<<"the birthdate is day: "<<myBirthdate.day<<" month: "<<myBirthdate.month<<" year: "<<myBirthdate.year<<endl;

    //review question 9
    WeatherPoint weather[100];
    for(int i = 0; i < 100; i++){
        weather[i].windSpeed = i/10;
        weather[i].humidity = 25;
        weather[i].temperature = i;
    }
    //calculate average
    double avgTemp = 0.0;
    double avgHumidity = 0.0;
    double avgWind = 0.0;
    for(int i = 0; i < 100; i++){
        avgWind += weather[i].windSpeed;
        avgTemp += weather[i].temperature;
        avgHumidity += weather[i].humidity;
    }
    avgWind /= 100;
    avgTemp /= 100;
    avgHumidity /= 100;
    cout<<"average wind: "<<avgWind<<endl;
    cout<<"average temp: "<<avgTemp<<endl;
    cout<<"avg humiditiy: "<<avgHumidity<<endl;

    return 0;
}
