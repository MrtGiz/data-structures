"""
В этом модуле будет представлена реализация связных списков
"""

import copy
import random


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'LinkedList [ ' + str(current.value)
            while current.next != None:
                current = current.next
                out += ", " + str(current.value)
            return out + ' ]'
        return 'LinkedList []'

    def clear(self):
        """
        Очистка списка
        :return:
        """
        self.__init__()

    def Len(self):
        """
        Опеределение длины списка
        :return:
        """
        self.length = 0
        if self.first != None:
            self.length += 1
            current = self.first
            while current.next != None:
                current = current.next
                self.length += 1
        return self.length

    def Push(self, x):
        """
        Добавление элемента в начало списка
        :param x:
        :return:
        """
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        else:
            self.first = Node(x, self.first)

    def add(self, x):
        """
        Добавление элемента в конец списка
        :param x:
        :return:
        """
        if self.first == None:
            self.first = Node(x, None)
            self.last = self.first
        elif self.last == self.first:
            self.last = Node(x, None)
            self.first.next = self.last
        else:
            current = Node(x, None)
            self.last.next = current
            self.last = current

    def InsertNth(self, i, x):
        """
        Вставка элемента на определенную позицию в списке
        :param i: позиция в списке
        :param x: значение для вставки
        :return:
        """
        if self.first == None:
            self.Push(x)
            return
        elif i == 0:
            self.Push(x)
            return
        curr = self.first
        count = 0
        while curr != None:
            if count == i - 1:
                curr.next = Node(x, curr.next)
                if curr.next.next == None:
                    self.last = curr.next
                break
            curr = curr.next
            count += 1

    def Pop(self):
        """
        Удаление головного элемента, возвращает значение удаленного элемента
        :return:
        """
        if self.first == None:
            return None
        elif self.first == self.last:
            self.clear()
        else:
            oldhead = self.first
            self.first = oldhead.next
            return oldhead.value

    def Del(self, i):
        """
        Удаление i-го элемента из списка
        если i больше количества элементов в списке, то ничего не происходит - нужно будет сделать исключение!!!
        :param i:
        :return:
        """
        if self.first == None:
            return
        old = curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == self.last:
                    old.next = self.last
                    break
                else:
                    old.next = curr.next
                    break
            old = curr
            curr = curr.next
            count += 1

    def sortedInsert(self, x):
        """
        Вставка элемента в отсортированный список - работает только для однотипных списков!!!
        :param x:
        :return:
        """
        if self.first == None:
            self.first = Node(x, self.last)
            return
        if self.first.value > x:
            self.first = Node(x, self.first)
            return
        old = curr = self.first
        while curr != None:
            if curr.value > x:
                curr = Node(x, curr)
                old.next = curr
                return
            old = curr
            curr = curr.next
        curr = Node(x, None)                                # вариант, когда х самый большой в списке
        old.next = curr                                     # становится в конец списка

    def RemoveDuplicates(self):
        """
        Удаление повторяющихся значений.
        Данная функция должна применяться к уже отсортированному списку.
        :return:
        """
        if self.first == None:
            return
        curr = self.first
        while curr.next != None:
            _del = 0
            if curr.value == curr.next.value:
                curr.next = curr.next.next
                _del = 1
            if _del == 0:
                curr = curr.next

    def Copy(self):
        """
        Функция для глубокого копирования списков
        :return:
        """
        return copy.deepcopy(self)


if __name__ == '__main__':
    li = LinkedList()
    for n in range(20):
        li.add(n)
    print(li)

    li.clear()
    print(li)

    for n in range(20):
        li.add(n)

    print('length:', li.Len())

    for n in range(5):
        li.Push('null')
    print(li)
    print('length:', li.Len())

    li.InsertNth(0, 'INS')
    print(li)

    li.Pop()
    li.Pop()
    li.Pop()
    li.Pop()
    li.Pop()
    li.Pop()
    print(li)

    print('length:', li.Len())
    li.Del(19)
    print(li)

    li.sortedInsert(666)
    li.sortedInsert(10)
    li.sortedInsert(-2)
    for n in range(5):
        li.InsertNth(22, 'null')
    print(li)
    li.RemoveDuplicates()
    print(li)

    new_list = li.Copy()
    print('new_list - \n', new_list)
    print('object id: li -', id(li), '| new_list -', id(new_list))
