def task1():
    s = input()
    sub1, sub2 = s.split(',')
    print(len(sub1) > len(sub2))
    print(sub1 == sub2)
    print(sub2 in sub1)

def task2():
    s = input()
    print(s.strip())
    print(len(s))
    print(s.count('a'))
    print(s.replace('a', '@'))
    print(s.istitle())

def task3():
    s = input()
    print(s[1:-1])
    print(s[::2])
    print(s.lower()[::-1])

def task4():
    numbers = list(map(int, input().split()))
    sorted_numbers = sorted(numbers)
    print(sorted_numbers)
    print(sum(numbers))
    print(min(numbers), max(numbers))

def task5():
    s = input()
    result = (s.lower() == s.lower()[::-1]) and (' ' not in s)
    print(result)

def task6():
    n = int(input())
    hex_str = hex(n)[2:]
    print(hex_str)
    print(len(hex_str))
    print('a' in hex_str)

def task7():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    n = int(input())
    print(months[n-1])

if __name__ == "__main__":
    pass

