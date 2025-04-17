#include <fstream> 
#include <string>   
#include <iostream> 

int main(int argc, char* argv[]) {
    // Проверяем, есть ли аргументы командной строки
    if (argc < 2) return 1; 

    // Флаги
    bool count_lines = false;  // Кол-во строк
    bool count_words = false;  // Кол-во слов
    bool count_bytes = false;  // Кол-во байт
    bool count_chars = false;  // Кол-во символов

    // Определяем ключи
    for (int i = 1; i < argc; i++) {
        std::string arg = argv[i];

        if (arg == "-l" || arg == "--lines") count_lines = true;
        else if (arg == "-w" || arg == "--words") count_words = true;
        else if (arg == "-c" || arg == "--bytes") count_bytes = true;
        else if (arg == "-m" || arg == "--chars") count_chars = true;
    }

    if (!count_lines && !count_words && !count_bytes && !count_chars) {
        count_lines = count_words = count_bytes = true;
    }

    // Обработка файлов
    for (int i = 1; i < argc; i++) {
        std::string filename = argv[i];  // Получаем имя файла из аргумента

        // Пропускаем аргументы, которые являются ключами
        if (filename[0] == '-') continue;

        // Открываем файл для чтения
        std::ifstream file(filename);
        if (!file.is_open()) continue;

        int lines = 0;   // Кол-во строк
        int words = 0;   // Кол-во слов
        int bytes = 0;   // Кол-во байт
        int chars = 0;   // Кол-во символов
        std::string line;  // Буфер для чтения строк

        // Чтение файла
        while (getline(file, line)) {
            lines++;
            bytes += line.size() + 1;
            chars += line.size() + 1;

            // Подсчет слов в строке
            bool in_word = false;  
            for (char c : line) {  
                if (isspace(c)) {  
                    in_word = false;  
                }
                else if (!in_word) {  
                    words++;        
                    in_word = true; 
                }
            }
        }

        // Вывод результатов
        if (count_lines) std::cout << lines << " ";
        if (count_words) std::cout << words << " ";
        if (count_bytes) std::cout << bytes << " ";
        if (count_chars) std::cout << chars << " ";
        std::cout << filename << "\n";

        file.close();
    }

    return 0;
}