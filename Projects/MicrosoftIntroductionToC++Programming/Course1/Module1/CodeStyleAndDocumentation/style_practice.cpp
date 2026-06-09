#include<iostream>

using namespace std;

class Calc{
    // A class used to calculate values
    public:
        int value_x, value_y;
        void CalculateSum(){value_x=10; value_y=20; int result=value_x + value_y;
            /*
            This function calculates the sum of two values.
            It initializes value_x and value_y, computes their sum, and displays the result and if the result is higher or lower than 25.
            */
            cout<<"result is "<<result<<endl;

            if(result > 25){cout<<"big number"<<endl;}
            else{cout<<"small number"<<endl;}
        }
    };

int main(){
    Calc c;
    c.CalculateSum();
    return 0;
}
