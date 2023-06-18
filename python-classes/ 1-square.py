#!/usr/bin/python3
class Square:
    def __init__(self, size):
        self.__size = size
    
    def imprime(self):
        print(self.__size)
        
def main():
    a = Square(12)
    a.imprime()

if __name__ == '__main__':
    main()