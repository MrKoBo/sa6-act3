words = ["Acedd","Add","Abew", "Aatr"]

longest_words = sorted(words, key=lambda x: (len(x), x))

print(longest_words)