//Austin Metzner     Assignment 8
//Melissa Bica
//Contributors: Anna, Brooke, Chris
#include <iostream>
#include <istream>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <time.h>
#include <math.h>
using namespace std;

//Introduce Game
//Ask user how big they want the grid under 20
//Grid is grid[userinput][Userinput]
//Ask user how many treasures they want
//Have loop that puts randomly generated numbers randomly in grid
//Ask user to enter two numbers first being row and second being the column
//Check if user inputs are within the bounds of the grid and that it's even a number
//If treasure found add number of points to score variable, and take treasure of the board
//Alert user that treasure was found and number of points they earned
//If treasure is not guessed subtract 10% from all treasures and point count
//Let user know all treasures decreased by 10%
//Once treasures is 0 congratulate user and exit game or if user exits game

class Treasure{
private:
    bool isTreasureActive; //determines whether treasure is active
    double treasurePoints; //used to assign points to treasures
    bool isCoordinateActive; //used to prevent repeat inputs
public:
   Treasure(){ //construct, called right after user decides how big game is to set the entire grid to these values
       isTreasureActive = false;//comes into play when randomly placing treasures
       treasurePoints = 0;//only the treasures get points
       isCoordinateActive = true; //determines whether or not user can guess this spot
   }

    //Sets and gets treasure points wherever it's called
    void setTreasurePoints(double points){
        treasurePoints = points;
    }
    double getTreasurePoints(){
        return treasurePoints;
    }

    //This sets and get whether or not treasure is active
    void setIsTreasureActive(bool active){
       isTreasureActive = active;
    }
    bool getIsTreasureActive(){
        return isTreasureActive;
    }

    //This is for sole purpose of determining whether or not the coordinate has already been used
    void setIsCoordinateActive(bool active){
       isCoordinateActive = active;
    }
    bool getIsCoordinateActive(){
        return isCoordinateActive;
    }
    ~Treasure(){ //This is my destructor
    }
};

int main()
{
    cout<<"Welcome to TREASURE HUNT!"<<endl;
    cout<<" "<<endl;

    //Setting up the grid
    int numRows; //sets dimensions of grid
    cout<<"How big is your treasure hunt? ";
    cin>>numRows;
    cout<<" "<<endl;
    int numColumns = numRows;
    Treasure grid[numRows][numColumns];//gives all the places in grid the value zero (see constructor) and a false activation

    //Setting number of treasures
    int numTreasures; //number of desired treasures
    cout<<"How many treasures do you want: ";
    cin>>numTreasures; //Entering anything other than a number will break the program
    cout<<" "<<endl;

    int terminator = numTreasures;//This is a counter I'll use to end game

     while(numTreasures > numRows*numColumns){ //Makes sure number of treasures is possible
        cout<<"Enter a number within dimensions of grid: ";
        cin>>numTreasures;
        cout<<" "<<endl;
    }

    srand(time(NULL));//initializing the random
    //Placing the treasures without repeats
    while(numTreasures > 0){
        int num1 = rand() % (numRows);
        int num2 = rand() % (numColumns);
        if (grid[num1][num2].getIsTreasureActive() == false){
            grid[num1][num2].setIsTreasureActive(true);
            grid[num1][num2].setTreasurePoints(rand() % 101);
            numTreasures--;
        }
    }

    //sets each grid space with boolean for sake of checking whether or not space is occupied
    /*for(int x = 0; x < numColumns; x++){
            for(int y = 0; y < numRows; y++){
                grid[x][y].setIsCoordinateActive(true);
            }
        }*/

    int counter = 0;//attempts counter
    double score = 0;//score counter

    while(counter < numRows*numColumns){//Main loop of the game. Loops until all possible guesses are made or all treasures are found

        int guessRow;
        int guessColumn;
        cout<<"Enter your guess (2 integers separated by space [row x column]): ";
        cin>>guessRow>>guessColumn; //user's guess
        cout<<" "<<endl;

        //Valid input checker
        while(guessRow > numRows-1 or guessColumn > numColumns-1){ //makes sure guess is within grid //minus 1 because dimensions
            cout<<"Enter a guess that's within the grid: ";
            cin>>guessRow>>guessColumn;
            cout<<" "<<endl;
        }
        while(grid[guessRow][guessColumn].getIsCoordinateActive() == false){ //checks to make sure guess hasn't already been made
            cout<<"This guess has already been made try another guess: ";
            cin>>guessRow>>guessColumn;
            cout<<" "<<endl;
        }

        cout<<"You guessed row "<<guessRow<<" and column "<<guessColumn<<endl;
        cout<<" "<<endl;

        //Checks if user's guess is a winner, if not, treasure points decrease by 10%
        if(grid[guessRow][guessColumn].getIsTreasureActive() == true){
            score += (grid[guessRow][guessColumn].getTreasurePoints());//If user guesses treasure right adds points to score
            cout<<"You found a treasure!"<<endl;
            cout<<"You earned "<<grid[guessRow][guessColumn].getTreasurePoints()<<" points, your current score is "<<score<<" points"<<endl;
            cout<<" "<<endl;
            grid[guessRow][guessColumn].setTreasurePoints(0); //clears the treasures points
            grid[guessRow][guessColumn].setIsTreasureActive(false); //Is no longer active
            terminator--;//subtracts amount of treasures active to determine when game is over
        }
        else{ //Takes each treasure score down by 10%
            cout<<"Sorry! You guessed wrong "<<endl;
            cout<<" "<<endl;
            for(int x = 0; x< numColumns; x++){
                for(int y = 0; y< numRows; y++){
                    if(grid[x][y].getIsTreasureActive() == true and grid[x][y].getTreasurePoints() != 0){
                        grid[x][y].setTreasurePoints(.9*grid[x][y].getTreasurePoints());
                        //cout<<"Treasure value decreased by 10%"<<endl;//used to see if program was decrementing treasures as it should be
                    }
                }
            }
        }

        //Prints board for programmers reference
        /*for(int x = 0; x< numColumns; x++){ //prints points
            for(int y = 0; y< numRows; y++){
                cout<<grid[x][y].getTreasurePoints()<<" ";
            }
        }*/

        grid[guessRow][guessColumn].setIsCoordinateActive(false);//sets guessed coordinates to false so same guess can't be made again
        counter++;

        //This if/else block determines if all the treasures have been found or not
        if(terminator == 0){
            cout<<"Congrats! You found all the treasures! Your final score is: "<<score<<"!!"<<endl;
            exit(EXIT_SUCCESS);//exits program
        }

        //Opt out function
        string qtoquit;
        cout<<"Press 'q' to quit: "<<endl;
        cin>>qtoquit;
        if(qtoquit == "q"){
            cout<<"The game is over! Your final score is: "<<score<<"!!"<<endl;
            exit(EXIT_SUCCESS);
        }
    }
    cout<<"The game is over! Your final score is: "<<score<<"!!"<<endl;//final statement

    return 0;
}
