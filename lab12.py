# Lab 12 - Document Analysis System

LINE = "=" * 44


sentence = input("Enter a sentence: ")


vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

words = len(sentence.split())
total_letters = vowels + consonants
vowel_percentage = (vowels / total_letters * 100) if total_letters > 0 else 0.0


print(LINE)
print("DOCUMENT ANALYSIS REPORT")
print(LINE)
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

print("\n--- Character Breakdown ---")
print(f"{'Words:':<20}{words}")
print(f"{'Vowels:':<20}{vowels}")
print(f"{'Consonants:':<20}{consonants}")
print(f"{'Digits:':<20}{digits}")
print(f"{'Spaces:':<20}{spaces}")
print(f"{'Special characters:':<20}{special}")

print("\n--- Summary ---")
print(f"Total letters: {total_letters}")
print(f"Vowel percentage: {vowel_percentage:.1f}%")

print()
print(LINE)
print("Analysis Complete!")
print(LINE)