from collections import deque


"""Односвязный список"""
# Структура данных, где элементы хранят ссылки на следующий элемент.
# Big O:
# append() - O(1) / push_front() - O(1) / pop_back() - O(n) / pop_front() - O(1)
# insert() - O(n) / erase() - O(n) (Удаление промежуточного элемента) / get_elem() - O(n)


class LinkedList:
    """Класс односвязного списка"""
    head = None

    class Node:
        """Класс элемента односвязного списка"""
        elem = None
        next_node = None

        def __init__(self, elem, next_node=None):
            self.elem = elem
            self.next_node = next_node

    def append(self, elem):
        """Метод добавления элемента в список"""
        if not self.head:
            self.head = self.Node(elem)
            return elem
        node = self.head

        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(elem)

    def insert(self, elem, index):
        """Метод добавления элемента по индексу"""
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(elem, next_node=node)

        return elem

    def get_elem(self, index):
        """Метод получения элемента по индексу"""
        i = 0
        node = self.head

        while i < index:
            node = node.next_node
            i += 1

        return node.elem

    def out(self):
        """Метод вывода элементов списка"""
        node = self.head

        while node.next_node:
            print(node.elem)
            node = node.next_node
        else:
            print(node.elem)

    def get_length(self):
        """Метод получения длинны списка"""
        if not self.head:
            return 0

        i = 1
        node = self.head

        while node.next_node:
            i += 1
            node = node.next_node

        return i

    def __iter__(self):
        node = self.head

        while node:
            yield node.elem
            node = node.next_node


linked_list = LinkedList()

linked_list.append(10)
linked_list.append(12)
linked_list.append(14)
linked_list.insert(13, 3)

print([linked_list.get_elem(3)])

linked_list.out()
print(linked_list.get_length())

for elem in linked_list:
    print(elem)


"""Двусвязный список"""
# Структура данных, где элементы хранят ссылку не только на следующий элемент, но и на предыдущий.
# Big O:
# append() - O(1) / push_front() - O(1) / pop_back() - O(1) / pop_front() - O(1)
# insert() - O(n) / erase() - O(n) (Удаление промежуточного элемента) / get_elem() - O(n)


class DuoLinkedList:
    """Класс двусвязного списка"""
    head = None
    tail = None
    length = 0

    class Node:
        """Класс элемента списка"""
        prev_node = None
        next_node = None
        elem = None

        def __init__(self, elem, next_node=None, prev_node=None):
            self.elem = elem
            self.next_node = next_node
            self.prev_node = prev_node

    def append(self, elem):
        """Метод добавления элемента в список"""
        self.length += 1
        if not self.head:
            self.head = self.Node(elem)
            return elem
        elif not self.tail:
            self.tail = self.Node(elem, None, self.head)
            self.head.next_node = self.tail
            return elem
        else:
            self.tail = self.Node(elem, None, self.tail)
            self.tail.prev_node.next_node = self.tail
            return elem


"""Динамический массив"""
# В Python в качестве Динамического массива представлен list().
# Но почему? Динамический массив же должен хранить одинаковый тип данных.
# Все дело в том, что в python мы работаем не с самими объектами, а с сылками на них =>
# => в массиве будут храниться только ссылки, которые являются единым типом данных.
# В качестве использования: ситуация, когда известно необходимое количество занимаемой памяти,
# дабы минимизировать ее использование
# Big O:
# list.append = O(1)
# list.insert(index, value) = O(n)
# list[1] = O(1)
# list_1 + list_2 = O(n + m), где n - число элементов list_1, а m - число элементов list_2
# list_2 = list_1[1:6] = O(n) - Создается новый массив, куда копируются значения list_1


"""Очередь"""
# Очередь работает по принципу FIFO (First In - First Out)
# deque из библиотеки collections создана на базе двухсвязного списка.
# В качестве использования: последовательное извлечение значений. Например: корзины с заказами и тд.
# Big O:
# append() - O(1) / appendleft() - O(1) / pop() - O(1) / popleft() - O(1) / extend() - O(n) (добав. элементы справа)
# extendleft() - O(n) (добав. элементы слева) / insert() - O(n) / remove() - O(n) / clear() - O(1) / copy() - O(n)

common_deque = deque([1, 2, 3, 4, 5])
common_deque.append(4)
common_deque.appendleft(10)
print(common_deque)

empty_deque = deque()
try:
    value = empty_deque.popleft()
    print(value)
except IndexError as e:
    print(e)

"""Стек"""
# Стек работает по принципу LIFO (Last In - First out)
# В качестве использования: извлечение значений в обратном порядке. Например: ссылки пройденых страниц для backtracking
# top() - O(1) / push() - O(1) / pop() - O(1) / size() - O(1) (вовзращает число элементов в стеке) /
# empty() - O(1) (вовзращает True,если стек пустой)
# Пример реализации стека на задаче по ПСП:

s = input()
stack = []
is_good = True

for char in s:
    if char in '([{':
        stack.append(char)
    elif char in ')]}':
        if not stack:
            is_good = False
            break
        open_char = stack.pop()
        if open_char == '(' and char == ')':
            continue
        if open_char == '[' and char == ']':
            continue
        if open_char == '{' and char == '}':
            continue
        is_good = False
        break
if is_good and len(stack) == 0:
    print(is_good)
else:
    print(False)
