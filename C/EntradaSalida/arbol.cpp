#include <iostream>
using namespace std;
#define URL "https://misfragmentosdecodigo.eu"

int main ()
{
    int acd = 1, numLineas, x , n , i;
    cin >> numLineas;
    x = numLineas - 1;

    while (x != 0) {
        n = 0;
        i = 0;
        while (i != x) {
            cout << " ";
            i++;
        }

        while (n < acd) {
            if (n%2 == 0) {
                cout << "*";
            } else {
                cout << " ";
            }
            n++;
        }
        x--;
        acd += 2;
        cout << endl;
    }

    // Falta ajustar de acuerdo al tamaño del árbol
    cout << "    *" << endl;
    cout << "    *" << endl;
    cout << "  * * *" << endl;
    /*for (int x = numLineas-1; x != 0; x--){
        cout.width(x);
        for (int n = 0; n < acd; n++){
            if (n % 2 == 0) {
                 cout << "*";
            } else {
                cout << " ";
            }
        }
        acd += 2;
        cout << endl;
    }*/
    /*for (int x = ((acd - 2) / 2 - 3) / 2; x != 0; x--){
        cout.width((acd * 40) / 100);
        for (int n = 0; n < (acd * 20) / 100; n++){
            cout << "*";
        }
        cout << endl;
    }
    for (int x = 2; x != 0; x--){
        cout.width((acd * 30) / 100);
        for (int n = 0; n < (acd * 40) / 100; n++){
            cout << "*";
        }
        cout << endl;
    }
    cout << "\nFeliz navidad les desea " << endl;
    cout << URL << endl;*/
    return 0;
}