#include "Director.h"

void Director::display_menu()
{
}

void Director::display_board()
{
}

int Director::get_input()
{
	return 0;
}

void Director::move_piece(char x, char y)
{
}

void Director::record_move()
{
}

Director::Director()
{
	std::cout << "Director :: No Arg Constructor Initiated" << std::endl;
}

Director::Director(std::string filename)
{
	std::cout << "Director :: File Constructor Initiated" << std::endl;
	std::cout << "Director :: Filename - " << filename << std::endl;
}

void Director::welcome_player()
{
	std::cout << "Welcome to Jacob's game of chess! Thank you for playing! :)" << std::endl;
}

void Director::enter_game_loop()
{
	p1_timer->start_timer();
	while (p1_timer->check_timer() > 0 && p2_timer->check_timer() > 0) {
	}
	std::cout << "Goodbye..." << std::endl;
}
