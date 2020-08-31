#include <iostream>
#include <string>
using namespace std;

int main() {
    cout << "Input message to encrpyt: ";
    string message;
    getline(cin, message);
    string encodedMessage = "";

    for(int i = 0; i < message.length(); i++) {
        int letter = (int)((char) message[i]);
        string strLetter = "";
        if(letter < 100) {
            strLetter = "0" + to_string(letter);
        } else {
            strLetter = to_string(letter);
        }
        encodedMessage = strLetter + encodedMessage;
    }

    cout << encodedMessage << endl;

    return 0;
}

