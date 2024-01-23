#!/usr/bin/env python3
import re

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            print("The value must be a string.")
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s]
        return len(sentences)

