#include <fstream> 
#include <string>   
#include <iostream> 

int main(int argc, char* argv[]) {
    // ���������, ���� �� ��������� ��������� ������
    if (argc < 2) return 1; 

    // �����
    bool count_lines = false;  // ���-�� �����
    bool count_words = false;  // ���-�� ����
    bool count_bytes = false;  // ���-�� ����
    bool count_chars = false;  // ���-�� ��������

    // ���������� �����
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

    // ��������� ������
    for (int i = 1; i < argc; i++) {
        std::string filename = argv[i];  // �������� ��� ����� �� ���������

        // ���������� ���������, ������� �������� �������
        if (filename[0] == '-') continue;

        // ��������� ���� ��� ������
        std::ifstream file(filename);
        if (!file.is_open()) continue;

        int lines = 0;   // ���-�� �����
        int words = 0;   // ���-�� ����
        int bytes = 0;   // ���-�� ����
        int chars = 0;   // ���-�� ��������
        std::string line;  // ����� ��� ������ �����

        // ������ �����
        while (getline(file, line)) {
            lines++;
            bytes += line.size() + 1;
            chars += line.size() + 1;

            // ������� ���� � ������
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

        // ����� �����������
        if (count_lines) std::cout << lines << " ";
        if (count_words) std::cout << words << " ";
        if (count_bytes) std::cout << bytes << " ";
        if (count_chars) std::cout << chars << " ";
        std::cout << filename << "\n";

        file.close();
    }

    return 0;
}