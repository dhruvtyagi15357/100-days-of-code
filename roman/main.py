def value_lookup(s: str) -> int:
        dictt = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        return dictt.get(s)
    
def romanToInt(s: str) -> int:
    summ = 0
    i = 0
    while i < len(s):
        print('i', i)
        flag = 0
        if i == len(s) - 1:
            print("i == len(s)-1")
            return summ + value_lookup(s[i])
        j = i+1
        while j < len(s):
            print('j', j)
            if value_lookup(s[j]) > value_lookup(s[i]):
                print('value_lookup(s[j]) > value_lookup(s[i]) == True')
                flag = 1
                neg_ind = j
                print('neg_ind', neg_ind)
            j += 1
        
        if flag == 1:
            k = i
            while k < neg_ind:
                print('k', k)
                summ -= value_lookup(s[k])
                k += 1
        else:
            summ += value_lookup(s[i])
        i += 1


print(romanToInt('LVIII'))