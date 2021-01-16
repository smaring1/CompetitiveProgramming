#include <iostream>
#include <bits/stdc++.h>
#include <string>
typedef long long ll;
#define for (n) for (int i = 0; i < n; i++)

using namespace std;

void display(student s, student *e);

//Un struct es un grupo de Data elements agruádps bajo un mismo nombre
struct student{ //<-- Sin parentesis
    //Un struct ocntiene Data Members y Member Functions
    //Data Members
    int rollno;
    char sex;
    int age;

    //Data Functions
    void printDetails(){
        cout << "Roll = " << rollno << endl;
    }
} pepito; //<-- PUNTO Y COMA AL FINAL, lo que pongamos aca son varibles que declaramos

int main(){
    //Se declarar como si fuera un objeto
    student miguel, julian, marco = {11, 'M'};
    // Or
    marco.rollno = 11;
    marco.sex = 'M';

    //Podemos llamar a pepito por que lo declaramos al final del struct
    pepito.rollno = 110;

    // ---- Uso de pointers y arrow operator para acceder a structs ----
    student pedro;
    student *pedroptr;

    pedroptr = &pedro;
    
    pedro.rollno = 11;
    pedroptr -> rollno = 122;

    // -- Struct como parameter --
    display(pedro, &pedro); //Podemos pasar con pointer para modificar los valores

    // --- Nested Structs ---
    person lucas;
    lucas.age = 18;
    lucas.name = "lucas";
    lucas.house.house_no = 13; //Con cada "." (punto) accedemos a los miebros de cad struct intenro
    lucas.house.street_name = "Laureles";

    person *lucasptr; //tambien podemos usar y acceder con pointers
    lucasptr = &lucas;

    lucasptr -> age = 14;
    lucasptr -> name = "lukas";
    lucasptr -> house.house_no = 18; //Como address/house no es un pointer se accede con punto .
    lucasptr -> houseptr -> house_no = 22; //Como houseptr fue delcarado como pointer en el struct si se puede accerder con ->

    
    
    return 0;
}

//Podemos pasar un struct como parametro, tambien su pointer
void display(student s, student *e){
    cout << s.rollno << " " << s.sex << endl;
    cout << e -> rollno << " " << e -> sex << endl;
    s.rollno = 10; //No hay cambios
    e -> rollno = 10; //Si hay cambios
}

//Podemos crear nested structs
struct address{
    int house_no;
    string street_name;
};

struct person{
    string name;
    int age;
    address house; //Aqui estamos creando su nested struct
    address *houseptr;
};