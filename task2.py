from collections import deque

def is_palindrome(input_str):
    # видаляємо пробіли і переводимо в нижній регістр
    input_str = input_str.lower().replace(" ", "")
    
    # створюємо двосторонню чергу
    queue = deque()
    for char in input_str:
        queue.append(char)
    
    # порівнюємо символи з обох сторін черги
    while len(queue) > 1:
        if queue.pop() != queue.popleft():
            return False
    return True

if __name__ == "__main__":
    input_str = input("Введіть слово/речення для перевірки поліндрома: ")
    print(is_palindrome(input_str)) 
