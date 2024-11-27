st = input()

x = tuple(set(st.split()))
y = tuple(st.split())

lst = []

for i in x:
    count = 0
    for j in y:
        if(i == j):
            count += 1
    sent = f"Слово {i} встретилось в вашем тексте {str(count)} раз"
    lst.append(sent)

print(f"В вашем тексте {len(x)} различных слов")

for i in lst:
    print(i)

example = input()
user = input()

user_set = set(user.split())
example_set = set(example.split())

print(len(user_set & example_set))
print(round((len(user_set - example_set) / len(user_set)) * 100), "%", sep = "")

st = input()

st_split = st.split()

lst_numbers = ["ноль","один","два","три","четыре","пять","шесть","семь",
               "восемь","девять","десять","одиннадцать","двенадцать",
               "тринадцать","четырнадцать","пятнадцать","шестнадцать",
               "семнадцать","восемнадцать","девятнадцать","двадцать"]
lst_sings = ["минус", "плюс"]

if(st_split[1] == lst_sings[0]):
    if(lst_numbers.index(st_split[0]) >= lst_numbers.index(st_split[2])):
        result = lst_numbers.index(st_split[0]) - lst_numbers.index(st_split[2])
        print(lst_numbers[result])
    else:
        result = lst_numbers.index(st_split[2]) - lst_numbers.index(st_split[0])
        print(st_split[1], lst_numbers[result])
else:
    result = lst_numbers.index(st_split[0]) + lst_numbers.index(st_split[2])
    print(lst_numbers[result])

print("111111")
print("222222")