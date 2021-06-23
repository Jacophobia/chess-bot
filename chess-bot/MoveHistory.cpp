#include "MoveHistory.h"

MoveHistory::MoveHistory()
{
}

MoveHistory::Move::Move(char player, char piece, int turn, char init_x, char init_y, char new_x, char new_y, bool captured)
{
	chess_piece = std::make_tuple(player, piece, turn);
	pos_initial = std::make_tuple(init_x, init_y);
	pos_displaced = std::make_tuple(new_x, new_y);
	was_capture = captured;
}

std::tuple<char, char> MoveHistory::Move::get_pos_initial()
{
	return pos_initial;
}

std::tuple<char, char> MoveHistory::Move::get_pos_displaced()
{
	return pos_displaced;
}

std::string MoveHistory::Move::to_string()
{
	std::string str_move = "";
	str_move.push_back(std::get<0>(chess_piece));
	str_move.push_back(std::get<1>(chess_piece));
	str_move.push_back(std::get<0>(pos_initial));
	str_move.push_back(std::get<1>(pos_initial));
	str_move.push_back(std::get<0>(pos_displaced));
	str_move.push_back(std::get<1>(pos_displaced));
	return str_move;
}
