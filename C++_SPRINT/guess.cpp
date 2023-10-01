#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <algorithm>
#include <iomanip>
using namespace std;

struct HighScore {
    string name;
    int score;
};

bool compareHighScores(const HighScore& a, const HighScore& b) {
    return a.score > b.score;
}

int main() {
    srand(static_cast<unsigned int>(time(nullptr)));

    int level = 1;
    int maxNumber = 100;
    int maxAttempts = 7;
    int score = 0;

    vector<HighScore> leaderboard;
    const int leaderboardSize = 5;

    while (true) {
        int secretNumber = rand() % maxNumber + 1;
        int guess;
        int attempts = 0;

        cout << "Welcome to BYU-Idaho Guessing Game - Level " << level << "!" << endl;
        cout << "🎉 Get ready for an exciting challenge! 🎉" << endl;
        cout << "I have selected a number between 1 and " << maxNumber << ". Can you guess it in " << maxAttempts << " attempts?" << endl;

        clock_t startTime = clock();

        while (attempts < maxAttempts) {
            cout << "Attempts left: " << maxAttempts - attempts << endl;
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
                clock_t endTime = clock();
                double duration = static_cast<double>(endTime - startTime) / CLOCKS_PER_SEC;

                cout << "Congratulations! 🎉 You've guessed the number (" << secretNumber << ") in " << attempts << " attempts and " << fixed << setprecision(2) << duration << " seconds." << endl;
                score += maxAttempts - attempts + 1;

                leaderboard.push_back({ "Player", score });
                sort(leaderboard.begin(), leaderboard.end(), compareHighScores);

                if (leaderboard.size() > leaderboardSize) {
                    leaderboard.pop_back();
                }

                cout << "Your current score: " << score << endl;
                break;
            }
        }

        if (attempts == maxAttempts) {
            cout << "Sorry, you've reached the maximum number of attempts. The secret number was " << secretNumber << "." << endl;
        }

        cout << "Do you want to continue to the next level? (y/n): ";
        char playAgain;
        cin >> playAgain;

        if (playAgain != 'y' && playAgain != 'Y') {
            cout << "Thanks for playing! Your final score is: " << score << ". See you next time." << endl;

            if (!leaderboard.empty()) {
                cout << "Leaderboard:" << endl;
                for (int i = 0; i < leaderboard.size(); ++i) {
                    cout << i + 1 << ". " << leaderboard[i].name << ": " << leaderboard[i].score << endl;
                }
            }

            cout << "Do you want to restart the game? (y/n): ";
            char restart;
            cin >> restart;

            if (restart != 'y' && restart != 'Y') {
                break;
            } else {
                level = 1;
                maxNumber = 100;
                maxAttempts = 7;
                score = 0;
                leaderboard.clear();
            }
        } else {
            level++;
            maxNumber += 10;
            maxAttempts++;
        }
    }

    return 0;
}

