text=input("Enter a word")
rev=text[::-1]
vowels=0;
for char in text.lower():
    if char in "aeiou":
        vowels=vowels+1;
    if text.lower()==rev.lower():
        palindrome=True
    else:
        palindrome=False


    print("Reverse:",rev)
    print("vowels",vowels)
    print("palindrome:",palindrome)
