A = {'x1': 0.2, 'x2': 0.4, 'x3': 0.6}
B = {'x1': 0.3, 'x2': 0.5, 'x3': 0.7}

def union(set1, set2):
    return {k: max(set1[k], set2[k]) for k in set1}

def intersection(set1, set2):
    return {k: min(set1[k], set2[k]) for k in set1}

def complement(set1):
    return {k: 1 - set1[k] for k in set1}

union_result = union(A, B)
complement_A = complement(A)
complement_B = complement(B)
intersection_result = intersection(complement_A, complement_B)
complement_union = complement(union_result)

print("Set A:", A)
print("Set B:", B)
print("Union of A and B:", union_result)
print("Complement of A:", complement_A)
print("Complement of B:", complement_B)
print("Intersection of Complement A and Complement B:", intersection_result)
print("Complement of Union of A and B:", complement_union)

print("De morgan law holds:", intersection_result == complement_union)