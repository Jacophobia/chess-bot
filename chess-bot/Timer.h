#pragma once

#include <chrono>
#include <string>
#include <iostream>

class Timer
{
private:
	long get_time_ms();

	bool is_paused = true;
	long time_left;
	long time_1 = 0;
	long time_2 = 0;
public:
	Timer(long time);
	void start_timer();
	void pause_timer();
	long check_timer();
	void update_timer();
	void increase_timer(long time);
	void increase_timer();
};

