le= "meegha"
a=le[::-1]


def charandfrequency(a):
  count={}
  for i in a :
    if i in count:
      count[i] += 1
    else:
      count[i] = 1
  max_count = 0
  max_char = ''
  for i in count:
    if count[i] > max_count:
      max_count = count[i]
      max_char = i
  return max_char

result = most_repeated(a)
print("Most repeated element is:", result)