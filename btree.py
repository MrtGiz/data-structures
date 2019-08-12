"""
Реализация класса - двоичное дерево поиска
В узлах дерева хранятся только значения
"""


class BinaryTree:
    def __init__(self):
        self.tree = EmptyNode()

    def __repr__(self):
        return repr(self.tree)

    def lookup(self, value):
        return self.tree.lookup(value)

    def insert(self, value):
        self.tree = self.tree.insert(value)


class EmptyNode:
    """
    пустой узел
    существует в единственном экземпляре, на него ссылаются все пустые узлы в дереве
    """
    def __repr__(self):
        return '*'

    def lookup(self, value):
        return False                                        # достигнут конец снизу

    def insert(self, value):
        return BinaryNode(self, value, self)               # добавить новый узел снизу


class BinaryNode:
    def __init__(self, left, value, right):
        self.data = value
        self.left = left
        self.right = right

    def lookup(self, value):
        if self.data == value:
            return True
        elif self.data > value:
            return self.left.lookup(value)                  # ищем в левом поддереве
        elif self.data < value:
            return self.right.lookup(value)                 # ищем в правом поддереве

    def insert(self, value):
        if self.data > value:
            self.left = self.left.insert(value)             # всатвить слева
        elif self.data < value:
            self.right = self.right.insert(value)           # вставить справа
        return self

    def __repr__(self):
        return '( %s, %s, %s )' % (repr(self.left), repr(self.data), repr(self.right))


if __name__ == '__main__':
    x = BinaryTree()
    for i in [3, 1, 9, 2, 7]:
        x.insert(i)
        print(x)

    print()
    for i in range(8):
        print((i, x.lookup(i)), end=' ')

