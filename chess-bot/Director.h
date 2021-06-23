#pragma once

#include "MoveHistory.h"
#include "Timer.h"

#include <string>
#include <memory>
#include <iostream>

class Director
{
private:
	int player_one_score = 0;
	int player_two_score = 0;
	int player_one_time = 300000;
	int player_two_time = 300000;
	std::unique_ptr<MoveHistory> gameLog = std::make_unique<MoveHistory>();
	std::shared_ptr<Timer> p1_timer = std::make_shared<Timer>(player_one_time);
	std::shared_ptr<Timer> p2_timer = std::make_shared<Timer>(player_two_time);

	void display_menu();
	void display_board();
	int get_input();
	void move_piece(char x, char y);
	void record_move();
public:
	Director();
	Director(std::string filename);
	void welcome_player();
	void enter_game_loop();
};

