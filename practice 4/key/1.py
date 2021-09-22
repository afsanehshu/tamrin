String = input("Enter : ")

vowel = ["a", "e", "i", "o", "u"]


s = String.lower()
S = list(s)

print(set(S).intersection(set(vowel)))


