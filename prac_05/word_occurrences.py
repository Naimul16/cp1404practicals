"""
Count Word Frequency
Estimate: 20 minutes
Actual:   43 minutes
"""

user_input = input("Enter a sentence: ")
split_words = user_input.split()
frequency_dict = {}

for item in split_words:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

longest_word = max(len(entry) for entry in frequency_dict)

for entry in sorted(frequency_dict):
    print(f"{entry:{longest_word}} : {frequency_dict[entry]}")
