def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

# Load data from p2.txt, skipping empty lines
data = []
with open("p2.txt", 'r') as fin:
    for line in fin:
        stripped_line = line.strip()
        if stripped_line:  # only process non-empty lines
            data.append(int(stripped_line))

print("Unsorted Array")
print(len(data), "items")

# Sort data in descending order using quicksort
quickSort(data, 0, len(data) - 1)

print("Sorted Array in Descending Order")
print(data)

# Count duplicates by comparing each element with the next one
duplicate_count = 0
for i in range(len(data) - 1):
    if data[i] == data[i + 1]:
        duplicate_count += 1

print("Found", duplicate_count, "duplicates")
