#include <string>
#include <iostream>

class Cat {
    private:
        int height, length;
    public:
        static std::string kind_name;
        Cat(int height, int length) : height(height), length(length) {}
    static void scream_once();
};

std::string Cat::kind_name = "cat";

void Cat::scream_once() {
    std::cout << "miao" << std::endl;
}

int main() {
    std::cout << Cat::kind_name << std::endl;
    Cat::scream_once();
    Cat cat(25, 60);
    std::cout << cat.kind_name << std::endl;
    cat.scream_once();
}
