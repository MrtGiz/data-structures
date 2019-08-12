"""
Реализация класса - двоичное дерево поиска
В узлах дерева хранятся ключи и значения
"""


class KeyedBinaryTree:
    def __init__(self):
        self.tree = EmptyNode()

    def __repr__(self):
        return repr(self.tree)

    def lookup(self, value):
        return self.tree.lookup(value)

    def insert(self, key, value):
        self.tree = self.tree.insert(key, value)


class EmptyNode:
    """
    пустой узел
    существует в единственном экземпляре, на него ссылаются все пустые узлы в дереве
    """
    def __repr__(self):
        return '*'

    def lookup(self, key):
        return None                                       # достигнут конец снизу

    def insert(self, key, value):
        return BinaryNode(self, key, value, self)         # добавить новый узел снизу


class BinaryNode:
    def __init__(self, left, key, value, right):
        self.key, self.value = key, value
        self.left, self.right = left, right

    def lookup(self, key):
        if self.key == key:
            return self.value
        elif self.key > key:
            return self.left.lookup(key)                  # ищем в левом поддереве
        else:
            return self.right.lookup(key)                 # ищем в правом поддереве

    def insert(self, key, value):
        if self.key == key:
            self.value = value
        elif self.key > key:
            self.left = self.left.insert(key, value)      # всатвить слева
        elif self.key < key:
            self.right = self.right.insert(key, value)    # вставить справа
        return self

    def __repr__(self):
        return '( %s, %s=%s, %s )' % (repr(self.left), repr(self.key), repr(self.value), repr(self.right))


if __name__ == '__main__':
    t = KeyedBinaryTree()
    for (key, val) in [('bbb', 1), ('aaa', 2), ('ccc', 3)]:
        t.insert(key, val)
    print(t)
    print(t.lookup('aaa'), t.lookup('ccc'))
    t.insert('ddd', 4)
    t.insert('aaa', 5)                                    # изменить значение ключа
    print(t)
