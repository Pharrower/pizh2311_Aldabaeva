#include "number.h"

// Конвертация из uint32_t
uint2022_t from_uint(uint32_t i) {
    uint2022_t result;
    result.parts[0] = i;

    return result;
}

// Конвертация из строки
uint2022_t from_string(const char* buff) {
    uint2022_t result = from_uint(0);

    while (*buff) {
        if (isdigit(*buff)) {
            uint32_t digit = *buff - '0';
            result = result * from_uint(10) + from_uint(digit);
        }

        buff++;
    }

    return result;
}

// Оператор сложения
uint2022_t operator+(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint64_t carry = 0; // Перенос

    for (int i = 0; i < 64; i++) {
        uint64_t sum = (uint64_t)lhs.parts[i] + rhs.parts[i] + carry;
        result.parts[i] = static_cast<uint32_t>(sum);
        carry = sum >> 32;
    }

    result.parts[63] &= 0x3F;
    return result;
}

// Оператор вычитания
uint2022_t operator-(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;
    uint64_t borrow = 0; // Заём

    for (int i = 0; i < 64; i++) {
        uint64_t rhs_val = (uint64_t)rhs.parts[i] + borrow;

        if (lhs.parts[i] >= rhs_val) {
            result.parts[i] = lhs.parts[i] - rhs_val;
            borrow = 0;
        }
        else {
            result.parts[i] = (uint64_t)0x100000000 + lhs.parts[i] - rhs_val;
            borrow = 1;
        }
    }

    result.parts[63] &= 0x3F;
    return result;
}

// Оператор умножения
uint2022_t operator*(const uint2022_t& lhs, const uint2022_t& rhs) {
    uint2022_t result;

    for (int i = 0; i < 64; i++) {
        uint64_t carry = 0;

        for (int j = 0; j < 64 - i; j++) {
            uint64_t product = (uint64_t)lhs.parts[i] * rhs.parts[j] + result.parts[i + j] + carry;
            result.parts[i + j] = static_cast<uint32_t>(product);
            carry = product >> 32;
        }
    }

    result.parts[63] &= 0x3F;
    return result;
}

// Оператор деления
uint2022_t operator/(const uint2022_t& lhs, const uint2022_t& rhs) {
    if (rhs == from_uint(0)) return from_uint(0);
    uint2022_t dividend = lhs;
    uint2022_t divisor = rhs;
    uint2022_t quotient = from_uint(0);
    uint2022_t current = from_uint(0);

    for (int i = 2021; i >= 0; --i) {
        current = current * from_uint(2);

        int part = i / 32;
        int bit = i % 32;
        uint32_t bit_value = (dividend.parts[part] >> bit) & 1;
        if (bit_value) {
            current = current + from_uint(1);
        }

        if (current >= divisor) {
            current = current - divisor;
            quotient.parts[part] |= (1 << bit);
        }
    }

    quotient.parts[63] &= 0x3F;
    return quotient;
}

// Операторы сравнения

bool operator==(const uint2022_t& lhs, const uint2022_t& rhs) {
    for (int i = 0; i < 64; i++) {
        if (lhs.parts[i] != rhs.parts[i]) return false;
    }

    return true;
}

bool operator!=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return !(lhs == rhs);
}

// Вспомогательная функция для сравнения
int compare(const uint2022_t& a, const uint2022_t& b) {
    for (int i = 63; i >= 0; i--) {
        if (a.parts[i] < b.parts[i]) return -1;
        if (a.parts[i] > b.parts[i]) return 1;
    }

    return 0;
}

bool operator>(const uint2022_t& lhs, const uint2022_t& rhs) {
    return compare(lhs, rhs) > 0;
}

bool operator>=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return compare(lhs, rhs) >= 0;
}

bool operator<(const uint2022_t& lhs, const uint2022_t& rhs) {
    return compare(lhs, rhs) < 0;
}

bool operator<=(const uint2022_t& lhs, const uint2022_t& rhs) {
    return compare(lhs, rhs) <= 0;
}

// Вывод
std::ostream& operator<<(std::ostream& stream, const uint2022_t& value) {
    if (value == from_uint(0)) {
        stream << "0";

        return stream;
    }

    uint2022_t num = value;
    char buffer[610] = { 0 };
    int index = 0;

    while (num != from_uint(0)) {
        uint2022_t div = from_uint(10);
        uint2022_t quot = num / div;
        uint2022_t rem = num - quot * div;

        buffer[index++] = '0' + rem.parts[0];
        num = quot;
    }

    // Вывод в обратном порядке
    for (int i = index - 1; i >= 0; i--) {
        stream << buffer[i];
    }

    return stream;
}