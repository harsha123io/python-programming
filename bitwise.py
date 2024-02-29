def rangeBitwiseAnd(left: int, right: int) -> int:
    shift = 0
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    return left << shift
left = 5
right = 7
print(rangeBitwiseAnd(left, right)) 
