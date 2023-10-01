#include <iostream>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
    // Seed the random number generator
    srand(static_cast<unsigned int>(time(nullptr)));

    int level = 1; // Starting level
    int maxNumber = 100;

    while (true) {
        // Generate a random number for the current level
        int secretNumber = rand() % maxNumber + 1;
        int guess;
        int attempts = 0;

        cout << "Welcome to BYU-Idaho Guessing Game - Level " << level << "!" << endl;
        cout << "🎉 Get ready for an exciting challenge! 🎉" << endl;
        cout << "I have selected a number between 1 and " << maxNumber << ". Can you guess it?" << endl;

        while (true) {
            cout << "Enter your guess: ";
            cin >> guess;
            attempts++;

            if (guess < 1 || guess > maxNumber) {
                cout << "Please enter a number between 1 and " << maxNumber << "." << endl;
                continue;
            }

            if (guess < secretNumber) {
                cout << "Oh no! Your guess is too low. Try again." << endl;
            } else if (guess > secretNumber) {
                cout << "Oops! Your guess is too high. Try again." << endl;
            } else {
                cout << "Congratulations! 🎉 You've guessed the number (" << secretNumber << ") in " << attempts << " attempts." << endl;
                break;
            }
        }

        // Move to the next level
        level++;
        maxNumber += 10; // Increase the range for the next level

        cout << "Do you want to continue to the next level? (y/n): ";
        char playAgain;
        cin >> playAgain;

        if (playAgain != 'y' && playAgain != 'Y') {
            cout << "Thanks for playing! See you next time." << endl;
            break;
        }
    }

    return 0;
}
