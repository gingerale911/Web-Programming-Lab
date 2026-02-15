class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        return ' '.join(words[::-1])

s = input()
reverser = StringReverser()
print(reverser.reverse_words(s))
