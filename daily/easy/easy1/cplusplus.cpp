#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

string convertInt(int number)
{
    stringstream ss;
    ss << number;
    return ss.str();
}

int main()
{
    string name, username, st = "";
    int age = 0;
    ofstream out_stream;

    out_stream.open("cplusplus_output.txt");

    cout << "What is your name? ";
    cin >> name;
    cout << "How old are you? ";
    cin >> age;
    cout << "What is your reddit username? ";
    cin >> username;

    st = "Your name is " + name + ", you are " + convertInt(age) + " years old, " +
        "and your username is " + username + "\n";

    cout << st;
    out_stream << st;

    out_stream.close();
    return 0;
}
