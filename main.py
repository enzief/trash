# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from BTree import BTree


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    t = BTree()
    t.insert(10)
    t.insert(20)
    t.insert(30)
    t.insert(40)
    t.insert(50)
    t.traverse()
    print("xxxx")
    t.insert(60)
    t.traverse()
    t.insert(70)
    t.insert(80)

    t.traverse()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
