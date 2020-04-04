<title>我是标题</ title>

# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    # True
print(pattern2 in string)    # False

import re

# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(pattern2, string))  # None