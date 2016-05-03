//Austin Metzner
//CSCI 1300 Hoenigman
//Melissa Bica
#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <math.h>

using namespace std;


double PasserRating(double p,double a,double y,double t,double i){
    double C = ((p/a)-.3)*5;
    double Y = ((y/a)-3)*.25;
    double T = ((t/a)*20);
    double I = 2.375-((i/a)*25);
    /*
    cout<<"p "<<p<<endl;
    cout<<"a "<<a<<endl;
    cout<<"C "<<C<<endl;
    cout<<"Y "<<Y<<endl;
    cout<<"T "<<T<<endl;
    cout<<"I "<<I<<endl;
    */
    if(C < 0){
        cout<<"C is "<<C<<endl;
        C = 0;
        cout<<"Negative changed to 0"<<endl;
    }
    if(Y < 0){
        cout<<"Y is "<<Y<<endl;
        Y = 0;
        cout<<"Negative changed to 0"<<endl;
    }
     if(I < 0){
        cout<<"I is "<<I<<endl;
        I = 0;
        cout<<"Negative changed to 0"<<endl;
    }
     if(T < 0){
        cout<<"T is "<<T<<endl;
        T = 0;
        cout<<"Negative changed to 0"<<endl;
    }

    if(C > 2.375){
        C = 2.375;
        cout<<C<<"Changed to 2.375"<<endl;
    }
    if(Y > 2.375){
        Y = 2.375;
        cout<<C<<"Changed to 2.375"<<endl;
    }
   if(I > 2.375){
        I = 2.375;
        cout<<I<<"Changed to 2.375"<<endl;
    }
    if(T > 2.375){
        T = 2.375;
        cout<<C<<"Changed to 2.375"<<endl;
    }
    double passerRating = (((C+Y+T+I)/6)*100);
    return passerRating;
}

double CyclingEnergy(double m, double b, double v, double d){
    //mass is in kilograms
    //velocity is in m/s
    //d is in kilometers
    double g = 9.8; //gravitational coefficient
    double k = .18; // coefficient related to rider position
    double Cr = .001; // coefficient of resistance from road
    srand(time(NULL));
    double Cf = (rand() % 50 + 51.0)/100.0; //randrange[50,100]/100 equivalent
    cout<<"CF draft is "<<Cf<<endl;

    double pAir = k*Cf*(v*v*v); // Power to overcome air resistance
    double pRoll = Cr*g*(m+b)*v; //power to overcome rolling resistance
    double pSec = pAir + pRoll;
    cout<<"Power output is "<<pSec<<" watts"<<endl;

    double timeTravel = (d*1000)/v; // m*(s/m) = s
    cout<<"Travel time in seconds: "<<timeTravel<<endl;
    double totalEnergy = (pSec*timeTravel)/1000; //divided by 1000 to put into kJ
    cout<<"Total energy is "<<round(totalEnergy)<<" kJoules to travel "<<d<<" kilometers"<<endl;

    double sumEnergy = 0;
    for(int i = 0; i<timeTravel; i++){
        double Cf = (rand() % 50 + 51.0)/100.0;
        double pAir = k*Cf*(v*v*v);
        double secEnergy = pSec*1;//energy in each second (*1)
        sumEnergy += secEnergy;
        //cout<<"Energy so far "<<sumEnergy<<" joules"<<endl;
    }
    double avgEnergy = (sumEnergy/1000)/(timeTravel/60);//average kJoules per minute
    cout<<"The average energy is "<<avgEnergy<<" kJoules per minute"<<endl;
}

int main(int argc, char *argv[])
{
    int c;

    //defining football variables
    double p = 0; //completions
    double a = 0; //attempts
    double y = 0; //yards
    double t = 0; //touchdowns
    double i = 0; //interceptions
    //defining cycling variables (inputs)
    double m = 0; //mass of rider
    double b = 0; //mass of bike
    double v = 0; //velocity
    double d = 0; //distance

    c = getopt(argc, argv,"fc:");
    if(c == 'f'){
        //run football
        while((c = getopt(argc, argv,"p:a:y:t:i:")) != -1){
            if(c == 'p'){
                p = atoi(optarg);
            }else if(c == 'a'){
                a = atoi(optarg);
            }else if(c == 'y'){
                y = atoi(optarg);
            } else if(c == 't'){
                t = atoi(optarg);
            } else if(c == 'i'){
                i = atoi(optarg);
            } else{
                int z = atoi(optarg);
                z = -1;
            }
        }
        //atoi convert the argument to a number since it is read as a string
        int pr = PasserRating(p,a,y,t,i);
        cout<<"Passer rating is "<<pr<<endl;
        if(pr < 85){
            cout<<"This QB's rating is poor!"<<endl;
        } else if(85<= pr && pr<90){
            cout<<"This QB's rating is mediocre!"<<endl;
        } else if(90<= pr && pr<95){
            cout<<"This QB's rating is good!"<<endl;
        } else if(95<= pr){
            cout<<"This QB's rating is great!"<<endl;
        }
    }
    if(c == 'c'){
        //run cycling
        while((c = getopt(argc, argv,"m:b:v:d:")) != -1){
            if(c == 'm'){
                m = atoi(optarg);
            } else if(c == 'b'){
                b = atoi(optarg);
            } else if(c == 'v'){
                v = atoi(optarg);
            } else if(c == 'd'){
                d = atoi(optarg);
            } else{
                int z = atoi(optarg);
                z = -1;
            }
        } //end of while loop
        //Call Cycling function
        CyclingEnergy(m,b,v,d);
    }
    return 0;
}
