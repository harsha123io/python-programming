from itertools import permutations
def unique_permutations(num):
    perms = permutations(str(num))
    unique_perms = set()
    for perm in perms:
        perm_str = ''.join(perm)
        unique_perms.add(perm_str)
    for perm in unique_perms:
        print(perm)
num = int(input("Enter a number: "))
print("Unique permutations of", num, "are:")
unique_permutations(num)
