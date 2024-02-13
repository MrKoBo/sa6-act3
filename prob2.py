words = ["Acedd","Add","Abew", "Aatr"]
sorted_words = sorted(words)

longest_words = sorted(sorted_words, key=lambda x: len(x))
print(longest_words)