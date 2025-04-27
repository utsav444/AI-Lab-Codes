A = {'x1': 0.1, 'x2': 0.7, 'x3': 0.5}
B = {'x1': 0.3, 'x2': 0.4, 'x3': 0.6}

def union(set1, set2):
    return {k: max(set1[k], set2[k]) for k in set1}

def intersection(set1, set2):
    return {k: min(set1[k], set2[k]) for k in set1}

def complement(set1):
    return {k: 1 - set1[k] for k in set1}

union_result = union(A, B)
intersection_result = intersection(A, B)
complement_A = complement(A)
complement_B = complement(B)
intersection_complement = complement(intersection_result)
union_complement = union(complement_A, complement_B)

print("Set A:", A)
print("Set B:", B)
print("Union complement of A and B:", union_complement)
print("Intersection complement of A and B:", intersection_complement)

print("De morgan law holds:", intersection_complement == union_complement)
