#pragma once

#include <tuple>
#include <string>
#include <stack>
#include <memory>

#include "Timer.h"

class MoveHistory
{
private:
	class Move {
	private:
		std::tuple<char, char, int> chess_piece; // player (W or B), piece (K, Q, B, R, N, P), turn
		std::tuple<char, char> pos_initial; // x, y
		std::tuple<char, char> pos_displaced; // x, y
		bool was_capture;
	public:
		Move(char player, char piece, int turn, char init_x, char init_y, char new_x, char new_y, bool captured);
		std::tuple<char, char> get_pos_initial();
		std::tuple<char, char> get_pos_displaced();
		char get_player();
		std::string to_string();
	};
	std::stack<Move> Moves;
	int turn;
	void remove_piece(char player, char init_x, char init_y);
public:
	MoveHistory(std::shared_ptr<Timer> p1_timer, std::shared_ptr<Timer> p2_timer);
	void add_move(char player, char init_x, char init_y, char new_x, char new_y);
	void undo_move();
	
};

