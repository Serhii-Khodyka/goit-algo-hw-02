import queue
import random
import time

# створюємо чергу заявок
request_queue = queue.Queue()

# генеруємо заявки
def generate_request():
    unique_id = random.randint(1, 1000000)  # створюємо унікальний номер заявки
    request = {"id": unique_id, "timestamp": time.time()}  # додаємо для унікальності заявки час створення
    request_queue.put(request)  # додаємо до черги
    print(f"Нова заявка: {unique_id}")

# обробка заявки
def process_request():
    if not request_queue.empty():  # перевіряємо чи черга не пуста
        request = request_queue.get()  # видаляємо заявку з черги
        print(f"Заявка : {request['id']} оброблена")
    else:
        print("Черга пуста")

if __name__ == "__main__":
    while True:
        action = input("Введіть 'new' для генерації заявки, 'serv' для обробки, чи 'exit' для виходу: ")
        if action == 'new':
            generate_request()
        elif action == 'serv':
            process_request()
        elif action == 'exit':
            print("Програму завершено")
            break
        else:
            print("Помилкова команда")
