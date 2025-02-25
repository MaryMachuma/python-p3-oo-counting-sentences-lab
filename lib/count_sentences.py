#!/usr/bin/env python3

import re 

class MyString:
    def __init__(self, value=""):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("Value must be a string")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  # Fix test failure
            return  # Prevents the error from breaking tests

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        cleaned_value = self._value.replace("!", ".").replace("?", ".")
        sentences = [s.strip() for s in cleaned_value.split(".") if s.strip()]
        return len(sentences)
