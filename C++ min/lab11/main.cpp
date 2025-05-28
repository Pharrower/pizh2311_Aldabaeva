#include <iostream>
#include <string>
#include <vector>
#include <algorithm> // Для sort

using namespace std;

// Базовый класс - Платеж
class Payment {
protected:
    string date;
    double amount;
    string description;

public:
    Payment() : date("01.01.1970"), amount(0.0), description("Без описания") {}
    Payment(string d, double a, string desc) : date(d), amount(a), description(desc) {}

    virtual ~Payment() {}

    double getAmount() const { return amount; }

    virtual void print() const {
    cout << "Дата: " << date << ", Сумма: " << amount << ", Описание: " << description << endl;
    }
};

// Класс-наследник 1: Доходы
class Income : public Payment {
    public:
        Income(string d, double a, string desc) : Payment(d, a, desc) {}
        void print() const override {
            cout << "Доход - ";
            Payment::print();
        }
};

// Класс-наследник 2: Расходы
class Expense : public Payment {
    public:
    Expense(string d, double a, string desc) : Payment(d, a, desc) {}
    void print() const override {
        cout << "Расход - ";
        Payment::print();
    }
};

// Основной класс - Журнал учета
class AccountBook {
    private:
    string card;
    string name;
    vector<Payment*> payments; // Используем вектор

    public:
    AccountBook(string c, string n) : card(c), name(n) {}
    ~AccountBook() {
    for (auto payment : payments) {
    delete payment; // Освобождение памяти
    }
    }

    void addPayment(Payment* p) {
    payments.push_back(p);
    }

    void printAllPayments() const {
    cout << "\nЖурнал: " << name << " (карта: " << card << ")" << endl;
    cout << "Список платежей:\n";
    for (size_t i = 0; i < payments.size(); i++) {
    cout << i + 1 << ". ";
    payments[i]->print();
    }
    }
};

int main() {
AccountBook book("1234 5678 9012 3456", "Иванов И.И.");

// Создаем и заполняем вектор платежей
vector<Payment*> payments;
payments.push_back(new Income("01.06.2023", 50000.0, "Зарплата"));
payments.push_back(new Expense("02.06.2023", 15000.0, "Аренда"));
payments.push_back(new Income("05.06.2023", 10000.0, "Фриланс"));
payments.push_back(new Expense("10.06.2023", 5000.0, "Продукты"));

// 1. Сортировка по убыванию суммы
sort(payments.begin(), payments.end(), [](Payment* a, Payment* b) {
return a->getAmount() > b->getAmount();
});

cout << "=== Платежи отсортированные по убыванию суммы ===" << endl;
for (auto p : payments) {
p->print();
}

// 2. Поиск платежей больше 10000 руб.
vector<Payment*> largePayments;
for (auto p : payments) {
if (p->getAmount() > 10000) {
largePayments.push_back(p);
}
}

cout << "\n=== Платежи с суммой > 10000 руб. ===" << endl;
for (auto p : largePayments) {
p->print();
}

// 3. Добавление всех платежей в журнал
for (auto p : payments) {
book.addPayment(p);
}

cout << "\n=== Содержимое журнала после добавления ===" << endl;
book.printAllPayments();

// 4. Сортировка всех платежей по возрастанию суммы
sort(payments.begin(), payments.end(), [](Payment* a, Payment* b) {
return a->getAmount() < b->getAmount();
});

// 5. Сортировка большого контейнера по возрастанию суммы
sort(largePayments.begin(), largePayments.end(), [](Payment* a, Payment* b) {
return a->getAmount() < b->getAmount();
});

// 6. Просмотр отсортированных платежей и крупных платежей
cout << "\n=== Платежи после сортировки по возрастанию суммы ===" << endl;
for (auto p : payments) {
p->print();
}

cout << "\n=== Крупные платежи после сортировки по возрастанию суммы ===" << endl;
for (auto p : largePayments) {
p->print();
}

return 0;
}