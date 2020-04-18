#include <string>
#include <iostream>

enum Month {
    JANURAY = 1,
    FEBRUARY,
    MARCH,
    APRIL,
    MAY,
    JUNE,
    JULY,
    AUGUST,
    SEPTEMBER,
    OCTOBER,
    NOVEMBER,
    DECEMBER
};

const std::string monthString[12] = {"JANURAY","FEBRUARY","MARCH","APRIL","MAY","JUNE",
    "JULY","AUGUST","SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER"};

std::string monthToString(Month month) {
    return monthString[month];
}

bool isLeapYear(int year) {
    if (year % 4 != 0) {
        return false;
    }
    else {
        return true;
    }
}

int daysInMonth(Month month, int year) {
    switch (month) {
        case APRIL:
        case JUNE:
        case SEPTEMBER:
        case NOVEMBER:
            return 30;
        case FEBRUARY:
            return (isLeapYear(year))?29:28;
        default:
            return 31;
    }
}