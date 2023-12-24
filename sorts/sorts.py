from random import shuffle

a = [i for i in range(50)]
shuffle(a)

def shaker(a):
    l = 0
    r = len(a) - 1
    while l < r:
        for i in range(l, r):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
        r -= 1
        
        for i in range(r, l, -1):
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
        l += 1
        
def insertWithBinarySearch(a):
    def binSearch(l, r, a, value):
        while l < r:
            m = l + (r - l) // 2
            if a[m] < value:
                l = m + 1
            elif a[m] > value:
                r = m
        return l
    for i in range(len(a)):
        key = a[i]
        index = binSearch(0, i, a, key)
        for j in range(i, index, -1):
            a[j] = a[j - 1]
        a[index] = key
    
        
def shell(a):
    # TODO
    step = len(a) // 2
    while step > 0:
        j = step
        while j < len(a):
            i = j - step
            while i >= 0:
                if a[i + step] < a[i]:
                    a[i + step], a[i] = a[i], a[i + step]
                else:
                    break
                i -= step
            j += 1
        step //= 2
           
           
def bubbleWithFlag(a):
    for i in range(len(a) - 1):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
           

def simpleInsert(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while a[j] > key and j >= 0:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        
        
def selectionSort(a):
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
        
        
def combSort(a):
    step = len(a)
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.24)
        flag, i = False, 0       
        while i + step < len(a):
            if a[i] > a[i + step]:
                a[i + step], a[i] = a[i], a[i + step]
                flag = True
            i += step
            
            
def gnomeSort(a):
    for i in range(1, len(a)):
        j = i - 1
        while a[j + 1] < a[j] and j >= 0:
            a[j], a[j + 1] = a[j + 1], a[j]
            j -= 1
            
        
print(a)
gnomeSort(a)
print(a)
print(a == sorted(a))