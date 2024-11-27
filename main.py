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