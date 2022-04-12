class StringUtility(object):
  def __init__(self, string):
    self.string = string
  def __str__(self):
    return self.string

  def vowels(self):
    count = 0
    for i in self.string:
      if i in "aeiouAEIOU":
        count += 1
    if count < 5:
      return str(count)
    else:
      return str("many")

  def bothEnds(self):
    if len(self.string)>=2:
      return self.string[:2]+self.string[-2:]
    else:
      return ''

  def fixStart(self):
    if len(self.string)>=2:
      return self.string[0]+self.string[1:].replace(self.string[0], "*")
    else:
      return ''

  def asciiSum(self):
    sum = 0
    for i in self.string:
      sum+=ord(i)
    return sum

  def cipher(self):
    if not self.string:
      return ""

    encoded_string = ""
    size = len(self.string)

    for i in self.string:
      ascii_val = None
      if not self.condition_in_alphabet(i):
        encoded_string += i
      elif i.lower() == i:
        ascii_val = ((ord(i) - ord('a')) + size) % 26
        encoded_string += chr(ascii_val + ord('a'))
      elif i.upper() == i:
        ascii_val = ((ord(i) - ord('A')) + size) % 26
        encoded_string += chr(ascii_val + ord('A'))
    return encoded_string

  def condition_in_alphabet(self, i):
    return (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)