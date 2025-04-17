#pragma once
#include <cinttypes>
#include <iostream>


struct uint2022_t {
    uint32_t parts[64] = { 0 }; // Массив из 64 32-битных чисел
};

// Размер не должен превышать 300 байт
static_assert(sizeof(uint2022_t) <= 300, "Size of uint2022_t must be no higher than 300 bytes");

uint2022_t from_uint(uint32_t i); // Конвертация из числа

uint2022_t from_string(const char* buff); // Конвертация из строки

// Перегрузка арифметических операторов
uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs); 

uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs); 

uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs); 

uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs); 

// Перегрузка операторов сравнения
bool operator==(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator>(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs);

bool operator<=(const uint2022_t& lhs, const uint2022_t& rhs);

// Перегрузка оператора вывода
std::ostream& operator<<(std::ostream& stream, const uint2022_t& value);