A = {'x1': 0.2, 'x2': 0.5, 'x3': 0.7}
B = {'x1': 0.3, 'x2': 0.4, 'x3': 0.5}
C = {'x1': 0.1, 'x2': 0.3, 'x3': 0.9}

def union(set1, set2):
    return {k: max(set1[k], set2[k]) for k in set1}

def intersection(set1, set2):
    return {k: min(set1[k], set2[k]) for k in set1}

def complement(set1):
    return {k: 1 - set1[k] for k in set1}

union_result = union(A, B)
intersection_result = intersection(A, B)
complement_result = complement(A)

print("Set A:", A)
print("Set B:", B)
print("Union of A and B:", union_result)
print("Intersection of A and B:", intersection_result)
print("Complement of A:", complement_result)
