#include <iostream>
#include <string>
#include <vector>

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

    void setDate(string d) { date = d; }
    void setAmount(double a) { amount = a; }
    void setDescription(string desc) { description = desc; }

    virtual void print() const {
        cout << "Дата: " << date << ", Сумма: " << amount << ", Описание: " << description;
    }
};

// Класс-наследник 1: Доходы
class Income : public Payment {
private:
    string source;

public:
    Income(string d, double a, string desc, string src) : Payment(d, a, desc), source(src) {}
    void print() const override {
        Payment::print();
        cout << ", Источник: " << source << endl;
    }
};

// Класс-наследник 2: Расходы
class Expense : public Payment {
private:
    string category;

public:
    Expense(string d, double a, string desc, string cat) : Payment(d, a, desc), category(cat) {}
    void print() const override {
        Payment::print();
        cout << ", Категория: " << category << endl;
    }
};

// Класс-контейнер
class Container {
private:
    vector<Payment*> payments;

public:
    ~Container() {
        for (auto payment : payments) {
            delete payment;
        }
    }

    void addPayment(Payment* p) {
        payments.push_back(p);
    }

    void removePayment(size_t index) {
        if (index < payments.size()) {
            delete payments[index]; 
            payments.erase(payments.begin() + index);
        }
    }

    void modifyPayment(size_t index, string date, double amount, string description) {
        if (index < payments.size()) {
            payments[index]->setDate(date);
            payments[index]->setAmount(amount);
            payments[index]->setDescription(description);
        }
    }

    void printAllPayments() const {
        for (const auto& payment : payments) {
            payment->print();
        }
    }
};

int main() {
    setlocale(LC_ALL, "Russian");
    Container container;

    // Добавляем платежи в контейнер (создаем через new)
    container.addPayment(new Income("01.06.2023", 50000.0, "Зарплата", "Работа"));
    container.addPayment(new Expense("02.06.2023", 15000.0, "Аренда", "Жилье"));

    // Просмотр контейнера
    cout << "Список платежей:\n";
    container.printAllPayments();

    // Изменяем один из платежей
    container.modifyPayment(0, "01.07.2023", 55000.0, "Обновленная зарплата");

    // Удаляем второй платеж
    container.removePayment(1);

    // Смотрим обновленный список
    cout << "\nОбновленный список платежей:\n";
    container.printAllPayments();

    return 0;
}