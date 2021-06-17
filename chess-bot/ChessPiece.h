#pragma once
#include <memory>

#include "GameBoard.h"

class ChessPiece
{
private:
	int point_value = 1;
	char x_position;
	char y_position;
	std::unique_ptr<GameBoard> board = std::make_unique<GameBoard>();
public:

};

