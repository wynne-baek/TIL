import sys
sys.stdin = open('input.txt')

TC = int(input())
for _ in range(1, TC+1):
    str1 = input()
    str2 = input()
    char_dict = {}
    for char in str1:
        char_dict[char] = 0
    #print(char_dict)
    for char in str2:
        for key in char_dict.keys():
            if char == key:
                char_dict[key] += 1
    print(f'#{_} {max(char_dict.values())}')