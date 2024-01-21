from queue import Queue
count = 0

# Створити чергу заявок
orders_queue = Queue()

class Order():
    def __init__(self, id_number):
        self.id_number = id_number


def generate_request():
    global count
# Створити нову заявку
    new_order = Order(count)
    count += 1
# Додати заявку до черги
    orders_queue.put(new_order)

def process_request():
    # Перевірка
    if not orders_queue.empty():
        # Видалити заявку з черги
        order = orders_queue.get()
        # Обробити заявку
        print(f'Your order {order.id_number} is in service now')
    else:
        #Вивести повідомлення, що черга пуста
        print("The queue is empty")

try:
    while True:
        generate_request()
        process_request()
# Ctrl+C
except KeyboardInterrupt:
    print("Program terminated by User")