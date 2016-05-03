//Austin Metzner
//Assignment 9
//Melissa Bica
#include <iostream>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>
#include <cstdlib>
#include <fstream>
#include <string>

using namespace std;

class Cipher{
private:
    string file;
    int key;
    string message;
public:
   Cipher(){ //constructor
       cout<<"Calling cipher constructor"<<endl;
   }

    //Sets and gets cipher key offset
    void setKey(int num){
        key = num;
    }
    int getKey(){
        return key;
    }
     //Sets and gets treasure key offset
    void setFileName(string name){
        file = name;
    }
    string getFileName(){
        return file;
    }
     void setMessage(string msg){
        message = msg;
    }
    string getMessage(){
        return message;
    }

    void cipherDoc(string fileToOpen, int offSetNum){ //encrypts document
        ifstream inFile; //stream to input from a file
        string msgLine;
        char c; //for purpose of converting each character
        string theMsg;
        inFile.open(fileToOpen); //opens/reads file

        if(inFile.fail()){ //checks if file opens
        cout<<"File didn't open"<<endl;
        } else{
            while(getline(inFile, msgLine)){
                for(int x = 0; x < msgLine.length(); x++){ //goes through each character and encrypts by shifting by offset amount
                    c = msgLine[x];
                    if(((int)c + offSetNum) > 126){
                        c = (31 + (((int)c + offSetNum)-126));//This wraps the addition
                    } else{
                        c += offSetNum;
                    }
                    theMsg += c;
                }
            }
        }
        this->setMessage(theMsg);
    }
    void decipherDoc(string fileToOpen, int offSetNum){ //decrypts document
        ifstream inFile; //stream to input from a file
        string msgLine;
        char c; //for purpose of converting each character
        string theMsg;
        inFile.open(fileToOpen); //opens/reads file

        if(inFile.fail()){ //checks if file opens
        cout<<"File didn't open"<<endl;
        } else{
            while(getline(inFile, msgLine)){
                for(int x = 0; x < msgLine.length(); x++){ //goes through each character and encrypts by shifting by offset amount
                    c = msgLine[x];
                    if(((int)c - offSetNum) < 32){
                        c = (127 - (32 - ((int)c - offSetNum)));//This wraps the addition
                    } else{
                        c -= offSetNum;
                    }
                    theMsg += c;
                }
                //cout<<theMsg<<endl;
            }
        }
        this->setMessage(theMsg);
    }
    void printMsg(){
        cout<<this->getMessage()<<endl;
    }
};

int main(int argc, char *argv[])
{
    Cipher code; //creating object
    int c;

    c = getopt(argc, argv,"ed:");
    if(c == 'e'){//encrypt message

        code.setKey(atoi(optarg));
        int offSet = code.getKey();

        c = getopt(argc, argv,"f:");
        if(c == 'f'){
            code.setFileName(optarg);
            string fileOpen = code.getFileName();
            code.cipherDoc(fileOpen, offSet);
            code.printMsg();
        } else {
            cout<<"Did not provide a file"<<endl;
        }

    }
    if(c == 'd'){//decrypt message

        code.setKey(atoi(optarg));
        int offSet = code.getKey();

        c = getopt(argc, argv,"f:");
        if(c == 'f'){
            code.setFileName(optarg);
            string fileOpen = code.getFileName();
            code.decipherDoc(fileOpen, offSet);
            code.printMsg();
        } else {
            cout<<"Did not provide a file"<<endl;
        }
    }
    /* while((c = getopt(argc, argv,"f:")) != 'n'){ //Just in case other doesn't work
            if(c == 'f'){
                string fileOpen = Cipher.setFileName(optarg);
            } else {
                string z = optarg;
                z = 'n';
            }
        }*/
    return 0;
}
