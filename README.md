# Стеки и очереди. Деревья и графы

## ЗАДАНИЕ
- Реализовать стек и очередь с помощью списка.
- Дополнительно реализовать другие рассмотренные 
на уроке структуры.

## [Решение задачи](main.py)
```
class Stack:
    def __init__(self):
        self.items = []  # Список для хранения элементов стека

    def is_empty(self):
        return self.items == []  # Возвращает True, если стек пуст

    def push(self, item):
        self.items.append(item)  # Добавляет элемент в конец списка (в стек)

    def pop(self):
        return self.items.pop()  # Удаляет и возвращает последний элемент списка

    def peek(self):
        return self.items[-1]  # Возвращает последний элемент списка (верх стека)
```
```
class Queue:
    def __init__(self):
        self.items = []  # Список для хранения элементов очереди

    def is_empty(self):
        return self.items == []  # Возвращает True, если очередь пуста

    def push(self, item):
        self.items.insert(0, item)  # Вставляет элемент в начало списка (в очередь)

    def pop(self):
        return self.items.pop()  # Удаляет и возвращает последний элемент списка (первый в очереди)

    def size(self):
        return len(self.items)  # Возвращает количество элементов в очереди
```
[Смотри так же main.py](main.py)