def wordsDeclension(self, amount, word, suffix, removeLast = False):
  if amount == 0 or amount > 1:
    res = word[0: -1] if removeLast else word
    res += suffix
    return res

  return word
