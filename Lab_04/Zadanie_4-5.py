def it_odwracanie(L, left, right):
    if left < 0:
        return 'left too small'
    if right >= len(L):
        return 'right too big'

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    
    return L

def rec_odwracanie(L, left, right):
    if left < 0:
        return 'left too small'
    if right >= len(L):
        return 'right too big'

    if left < right:
        L[left], L[right] = L[right], L[left]
        rec_odwracanie(L, left+1, right-1)
    
    return L

L=[1, 2, 3, 5, 7]
print(f"Lista przed odwroceniem: {L}")
print(f"Lista po wykonaniu it_odwracanie(L, 1, 4): {it_odwracanie(L, 1, 4)}")
print(f"Lista po rec_obracanie(L, 0, 3): {rec_odwracanie(L, 0, 3)}")
