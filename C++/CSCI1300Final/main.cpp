//Austin Metzner section 104 Melissa Bica FINAL
#include <iostream>

using namespace std;

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

int main()
{

    return 0;
}
