# task 1 slice

def isPalindrome(w):
    return w == w[::-1]
def isPalindrome(a):
    return a == a[::-1]

a = "windows"
ab = isPalindrome(a)

if ab:
  print("Yes")

else:
   print("No")

  
w = "malayalam"
ans = isPalindrome(w)

  
if ans:
    print("Yes")
else:
    print("No")