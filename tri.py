from random import randint

def is_sorted(l: list) -> bool:
    for i in range(1, len(l)):
        if l[i - 1] > l[i]:
            return False
    return True

def insertion(liste: list, i: int) -> bool:
    i_ = i
    while i >= 1 and liste[i - 1] > liste[i]:
        temp = liste[i]
        liste[i] = liste[i - 1]
        liste[i - 1] = temp
        i -= 1
    
    if i_ == i:
        return True
    else:
        return False

def tri_insertion(liste: list):
    i = 1
    l = len(liste)
    while i < l:
        if insertion(liste, i):
            i += 1


def selection_min(liste: list, i: int) -> int:
    min = i
    for j in range(i + 1, len(liste)):
        if liste[j] < liste[min]:
            min = j
    return min

def tri_selection(liste: list):
    for i in range(len(liste) - 1):
        min = selection_min(liste, i)
        temp = liste[i]
        liste[i] = liste[min]
        liste[min] = temp


test_list = [randint(0, 250) for _ in range(100)]
print(is_sorted(test_list))
print(test_list)

print()
test_insertion = test_list.copy()
tri_insertion(test_insertion)
print(is_sorted(test_insertion))
print(test_insertion)

print()
test_selection = test_list.copy()
tri_selection(test_selection)
print(is_sorted(test_selection))
print(test_selection)