word= "carambar"
letter= [i for i in word]
size=len(letter)
last_index = size -1


for i in range(last_index, -1, -1):
    print(letter[i])


# print([*word])      # ['c', 'a', 'r', 'a', 'm', 'b', 'a', 'r']