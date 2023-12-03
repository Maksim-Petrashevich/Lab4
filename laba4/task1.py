class String:
    string ="NULL"

    def __init__(self, string):
        self.string = string

    def Size(self):
        return len(self.string)

    def WordCount(self, word):
        return self.string.count(word)

    def BigLetters(self):
        return self.string.upper()

    def LittleLetters(self):
        return self.string.lower()

    def OneSpace(self):
        string = ' '.join(self.string.split())
        self.string=string
        return string

if(__name__ == '__main__'):
    check=0
    while(True):
        try:
            print("\tМеню работы со строками")
            print("1. Ввести строку")
            print("2. Размер строки")
            print("3. Нахождение конкретного слова в подстроке")
            print("4. Выввод только с заглавной")
            print("5. Вывод только с маленькой")
            print("6. Вывод с одним пробелом между словами")
            print("7. Завершение")
            number = int(input("Ваш выбор: "))
            if( number<0):
                print("Неверный ввод")
            else:
                if number == 1:
                    check = 1
                    word = input("Введите строку: ")
                    s = String(word)
                elif number == 2:
                    if check == 1:
                        print(f"Размер строки: {s.Size()} ")
                    else:
                        print("Введите сперва строку")
                elif number == 3:
                    if check == 1:
                        while (True):
                            print(f"Введите слово которое хотите подсчитать в строке {s.string}")
                            word = input("Введите сдво: ")
                            if " " in word:
                                print("Слово дожно быть без пробела")
                            else:
                                number = s.WordCount(word)
                                if number == 0:
                                    print("Такого слова нет")
                                else:
                                    print(f"Слово {word} найдено в кол-ве {number} штук" )
                                break
                    else:
                        print("Введите сначала строку")
                elif number==4:
                    if check == 1:
                        print(s.BigLetters())
                    else:
                        print("Введите сначала строку")
                elif number==5:
                    if check == 1:
                        print(s.LittleLetters())
                    else:
                        print("Введите сначала строку")
                elif number==6:
                    if check == 1:
                        print(s.OneSpace())
                    else:
                        print("Введите сначала строку")
                elif number == 7:
                    exit(1)
        except ValueError:
            print("Неккоректный ввод")
