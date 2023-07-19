string_=input("Enter the string : ")
def palindrome(string_):
    if string_[::-1]==string_:
        return True
    else:
        return False
n = len(string_)
l=""
for i in range(n):
    for j in range(i+1,n):
        if palindrome(string_[i:j+1]):
            if len(l)<len(string_[i:j+1]):
                l=string_[i:j+1]
print(l)
