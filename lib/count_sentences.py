#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    if isinstance(value, str):
      self.value = value
    print("The value must be a string.")
    
  def is_sentence(self):
    return self.value.endswith(".")

  def is_question(self):
    return self.value.endswith("?")

  def is_exclamation(self):
    return self.value.endswith("!")

  def count_sentences(self):
    temp_value = self.value.replace("!", ".").replace("?", ".")
    sentences = temp_value.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]
    return len(sentences)