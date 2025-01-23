x = [7, 9, 5, 4, 2, 1]
y = [1, 2, 3, 4, 5, 8, 9, 7]

def shaker_sort_recursively(sequence: list[int], left: int = 0, right: int = -1):
    if right < 0:
        right = len(sequence)

    if left >= right:
      return sequence

    for i in range(left + 1, right):
        if sequence[i - 1] > sequence[i]:
            temp_element = sequence[i]
            sequence[i] = sequence[i - 1]
            sequence[i - 1] = temp_element
    right -= 1
    for i in range(right - 1, left, -1):
        if sequence[i - 1] > sequence[i]:
            temp_element = sequence[i]
            sequence[i] = sequence[i - 1]
            sequence[i - 1] = temp_element
    left += 1

    return shaker_sort_recursively(sequence, left, right)

print(shaker_sort_recursively(x))
print(shaker_sort_recursively(y))
