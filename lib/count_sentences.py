#!/usr/bin/env python3
import re  # Add this line

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string based on sentence-ending punctuation and count the segments
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s]
        return len(sentences)

# Example usage:
string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.is_sentence())  # Output: False
print(string.is_question())  # Output: False
print(string.is_exclamation())  # Output: True
print(string.count_sentences())  # Output: 3


