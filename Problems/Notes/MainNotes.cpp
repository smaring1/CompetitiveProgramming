#include <iostream>
#include <bits/stdc++.h>
#include <string>
typedef long long ll;
#define for (n) for (int i = 0; i < n; i++)

using namespace std;

void funcionabajo(int [][10], int [], int);

void intro()
{
    //Para leer archivos
    freopen("input.txt", "r", stdin);

    //Para sacar archivos
    freopen("output.txt", "w", stdout);

    //Tipos de datos
    int x, y;
    long long asdf; // NO mezclar LL con int. hay que castear (long long) int
    string z;
    char a = 'a';
    double asds = 2.3;
    bool beruh = true;

    //Operaciones
    /*
    1 * 2
    1 + 2
    1 - 2
    1 / 2
    1 % 2
    */

   //Ternary operator
   // expression ? statement : statement;
   //                True        False
    int nota = 10;
    nota <= 15 ? cout << "ganaste" : cout << "perdiste";  

    //Entrada y salida
    string variableString;
    cin >> x >> y; // Holas como estas --> Holas
    getline(cin, variableString); // hola como estas
    cout << x << " hola xd " << y << " x + y: " << x + y;

    //Strings
    string test = "Hola";
    test[0];       //Caracter 0 = H
    test[0] = 'L'; //Ahora dira Lola en vez de Hola

    //Entrada y salida de datos indefinidos
    int var;
    while (cin >> var)
    {
        cout << var << "\n";
    }

    //Recortar nomrbes de variuabkles
    typedef long long ll; //En vez de tenrer que escribir long long se puede escribir ll
    typedef vector<int> vi;
    ll numero = 123456789;
    vi vector_de_integers;

    // c++ "ll" == long long

    //Para dar una matriz como parametro minimo hay que dar uno de los tamaños°

    // ------ CONST ------
    const int pi = 3.1415; //La variable sera read-only, es decir, constante
}

void funcionabajo(int matriz[][10], int arreglo[], int variable){
    /*
    En c++ cuando creamos una funcion esta tiene que estar arriba de la funcion donde se llama
    sin embargo, hay una manera de redeclararla arriba de todo el codigo parar que no hayan problemas
    Mirar arriba para entender

    las varibles se copian sin nombre
    */
}

inline void hola(){
    // Cuando la palabra inline esta en una funcion y la llamas, lo que se hace es que se toma todo el
    // Codigo dentro de la funcion y se pega donse se llamo
    // Aumenta el tamañno del archivo y no es recomdable para funciones muy grnades
    // Hay veces que hasta el compilador decide no insertar el codigo
}

void morenotes(){
    
} 