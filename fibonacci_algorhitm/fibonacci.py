array = range(100)
element_1 = 0
element_2 = 1
fibonacci = []
for element in array :
    next_element = element_1 + element_2
    fibonacci.append(element_1)
    element_1 = element_2
    element_2 = next_element
print(fibonacci[:100])