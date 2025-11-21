s = input("Enter a number or string: ")

flag = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        flag = False
        print("Not a Palindrome")
        break

if flag:
    print("Palindrome")
