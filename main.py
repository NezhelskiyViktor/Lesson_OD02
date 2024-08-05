# Определяем класс Stack (стек) в котором последний помещённый элемент будет первым в очереди
class Stack:
    # Конструктор класса, инициализирующий пустой стек
    def __init__(self):
        self.items = []  # Список для хранения элементов стека

    # Метод для проверки, пуст ли стек
    def is_empty(self):
        return self.items == []  # Возвращает True, если стек пуст

    # Метод для добавления элемента в стек
    def push(self, item):
        self.items.append(item)  # Добавляет элемент в конец списка (в стек)

    # Метод для удаления и возврата верхнего элемента стека
    def pop(self):
        return self.items.pop()  # Удаляет и возвращает последний элемент списка

    # Метод для получения верхнего элемента стека без его удаления
    def peek(self):
        return self.items[-1]  # Возвращает последний элемент списка (верх стека)


# Определяем класс Queue (очередь) в котором первый помещённый элемент будет первым в очереди
class Queue:
    # Конструктор класса, инициализирующий пустую очередь
    def __init__(self):
        self.items = []  # Список для хранения элементов очереди

    # Метод для проверки, пуста ли очередь
    def is_empty(self):
        return self.items == []  # Возвращает True, если очередь пуста

    # Метод для добавления элемента в конец очереди
    def push(self, item):
        self.items.insert(0, item)  # Вставляет элемент в начало списка (в очередь)

    # Метод для удаления и возврата первого элемента очереди
    def pop(self):
        return self.items.pop()  # Удаляет и возвращает последний элемент списка (первый в очереди)

    # Метод для получения размера очереди
    def size(self):
        return len(self.items)  # Возвращает количество элементов в очереди


# Определяем класс BinaryTree (двоичное дерево)
class BinaryTree:
    class Node:  # Определяем класс Node (узел)
        # Конструктор класса, инициализирующий узел с заданным значением
        def __init__(self, key):
            self.left = None  # Левый потомок (изначально None)
            self.right = None  # Правый потомок (изначально None)
            self.value = key  # Значение узла

    # Конструктор класса, инициализирующий пустое дерево
    def __init__(self):
        self.root = None  # Корень дерева (изначально None)

    # Метод для вставки нового узла с заданным значением
    def insert(self, key):
        if self.root is None:  # Если дерево пустое
            self.root = self.Node(key)  # Создаем корень дерева
        else:
            self._recursively(self.root, key)  # Вставляем узел рекурсивно

    # Вспомогательный метод для рекурсивной вставки узла
    def _recursively(self, current_node, key):
        if key < current_node.value:  # Если значение меньше текущего узла
            if current_node.left is None:  # Если левый потомок отсутствует
                current_node.left = self.Node(key)  # Создаем новый узел в качестве левого потомка
            else:
                self._recursively(current_node.left, key)  # Рекурсивно продолжаем вставку в левое поддерево
        else:  # Если значение больше или равно текущему узлу
            if current_node.right is None:  # Если правый потомок отсутствует
                current_node.right = self.Node(key)  # Создаем новый узел в качестве правого потомка
            else:
                self._recursively(current_node.right, key)  # Рекурсивно продолжаем вставку в правое поддерево

    # Метод для обхода дерева в симметричном порядке
    def traversal(self):
        return self.traversal_recursively(self.root)  # Начинаем с корня дерева

    # Вспомогательный метод для рекурсивного симметричного обхода
    def traversal_recursively(self, node):
        result = []
        # Обходим левое поддерево
        if node.left:
            result.extend(self.traversal_recursively(node.left))
        # Добавляем значение текущего узла
        result.append(node.value)
        # Обходим правое поддерево
        if node.right:
            result.extend(self.traversal_recursively(node.right))
        return result


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        """Добавляет ребро между вершинами u и v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        """Удаляет ребро между вершинами u и v."""
        if u in self.graph and v in self.graph[u]:
            self.graph[u].remove(v)
        if v in self.graph and u in self.graph[v]:
            self.graph[v].remove(u)

    def display(self):
        """Отображает граф в виде списка смежности."""
        for vertex in self.graph:
            print(f"Узел {vertex} связан с узлами: {', '.join(map(str, self.graph[vertex]))}")


if __name__ == "__main__":
    print("Демонстрация использования стека")
    stack = Stack()  # Создаем экземпляр стека
    numbers = [11, 22, 33, 44]  # Список чисел для вставки
    # Вставляем все числа в стек
    for number in numbers:
        stack.push(number)
    # Выводим симметричный обход стека
    print(f"Исходные данные для стека: {numbers}")
    print("Вывод данных из стека:")
    while not stack.is_empty():
        print(stack.pop())

    print("\nДемонстрация использования очереди")
    queue = Queue()  # Создаем экземпляр стека
    numbers = [11, 22, 33, 44]  # Список чисел для вставки
    # Вставляем все числа в стек
    for number in numbers:
        queue.push(number)
    # Выводим симметричный обход стека
    print(f"Исходные данные для очереди: {numbers}")
    print("Вывод данных из очереди:")
    while not queue.is_empty():
        print(queue.pop())

    print("\nДемонстрация использования двоичного дерева")
    tree = BinaryTree()  # Создаем экземпляр двоичного дерева
    numbers = [7, 4, 9, 1, 6, 8, 10]  # Список чисел для вставки
    # Вставляем все числа в дерево
    for number in numbers:
        tree.insert(number)
    # Выводим симметричный обход двоичного дерева
    print(f"Исходные данные для дерева: {numbers}")
    print("Упорядоченный обход бинарного дерева:", tree.traversal())

    print("\nДемонстрация использования графа")
    g = Graph()
    edges = [(1, 2), (1, 3), (2, 3), (3, 4), (5, 2), (5, 3), (6, 3), (6, 4)]
    print(f"Исходные данные для графа: {edges}")
    # Добавляем ребра
    for u, v in edges:
        g.add_edge(u, v)
    # Отображаем граф
    print("Список смежности графа:")
    g.display()
    # Удаляем ребро
    g.remove_edge(1, 3)
    # Отображаем граф после удаления ребра
    print("\nСписок смежности графа после удаления ребра методом remove_edge(1, 3):")
    g.display()
