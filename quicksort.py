def quicksort(tab):
    less = []
    equal = []
    greater = []

    if len(tab) > 1:
        pivot = tab[0]
        for x in tab:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)

    else:
        return tab

tab=[12,4,5,6,7,3,1,15,25,152,845,974,12,32,564,321]

print(quicksort(tab))