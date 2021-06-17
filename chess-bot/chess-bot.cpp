// chess-bot.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <memory>
#include <string>

#include "Director.h"

int main()
{
    int choice = -1;
    while (choice != 1 && choice != 2) {
        std::cout << "Would you like to start a new game or load a previous game?" << std::endl;
        std::cout << "1 - Start a new game" << std::endl;
        std::cout << "2 - Load a game from a file" << std::endl;
        std::cin >> choice;
    }
    std::unique_ptr<Director> game;
    if (choice == 1) {
        game = std::make_unique<Director>();
    }
    else {
        std::string filename = "PreviousGames.txt";
        game = std::make_unique<Director>(filename);
    }
    game->welcome_player();
    game->enter_game_loop();
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
