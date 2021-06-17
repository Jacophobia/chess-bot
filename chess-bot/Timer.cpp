#include "Timer.h"

long Timer::get_time_ms()
{
    std::chrono::milliseconds ms = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now().time_since_epoch()
        );
    return ms.count();
}

Timer::Timer(long time) :
    time_left{ time } {}

void Timer::start_timer()
{
    is_paused = false;
    time_1 = get_time_ms();
}

void Timer::pause_timer()
{
    update_timer();
    is_paused = true;
}

long Timer::check_timer()
{
    update_timer();
    return time_left;
}

void Timer::update_timer()
{
    if (!is_paused){
        time_2 = get_time_ms();
        long dif_time = time_2 - time_1;
        time_1 = get_time_ms();
        time_left -= dif_time;
    }
}

void Timer::increase_timer(long time)
{
    if (time_left >= 0) {
        time_left += time;
    }
}

void Timer::increase_timer()
{
    increase_timer(15000);
}
