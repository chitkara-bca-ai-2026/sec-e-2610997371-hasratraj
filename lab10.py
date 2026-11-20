# Lab 10 - Text Processing Tool

W = 30   

print("=" * 40)
print("         TEXT PROCESSING TOOL")
print("=" * 40)


sentence = input("Enter a sentence: ")

print("\n--- Processing Results ---")


try:
    pos = int(input("Enter position for indexing: "))
    print(f"Character at position {pos}  : '{sentence[pos]}'")
except ValueError:
    print("[ERROR] Position must be a whole number.")
except IndexError:
    print(f"[ERROR] Position {pos} is out of range (valid: 0 to {len(sentence) - 1}).")


try:
    start = int(input("Enter start index for slicing : "))
    end = int(input("Enter end index for slicing   : "))
    print(f"Sliced string [{start}:{end}]       : '{sentence[start:end]}'")
except ValueError:
    print("[ERROR] Slice indexes must be whole numbers.")


print(f"{'Uppercase':<{W}}: {sentence.upper()}")
print(f"{'Lowercase':<{W}}: {sentence.lower()}")


old_word = input(f"{'Enter word to replace':<{W}}: ")
new_word = input(f"{'Enter replacement word':<{W}}: ")
print(f"{'After replace':<{W}}: {sentence.replace(old_word, new_word)}")


print(f"{'Length of sentence':<{W}}: {len(sentence)}")


print("\n" + "=" * 40)
print("Analysis Complete!")
print("=" * 40)