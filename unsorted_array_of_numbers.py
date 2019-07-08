# https://www.glassdoor.com/Interview/Yelp-Software-Engineer-Intern-Interview-Questions-EI_IE43314.0,4_KO5,29.htm

a = [1, 2, 3, 4, 6, 7, 8]
result = []
size = len(a)
x = 10
for i in range(0, size):
    for j in range(i + 1, size):
        if a[i] + a[j] == x:
            res = (a[i], a[j])
            result.append(res)
print result
