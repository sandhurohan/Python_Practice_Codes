#FStrings = Fast Strings

import math
s1="My age is : "
s2=18
#a="My name is Rohan. %s %s"% (s1, s2)
#a="My name is Rohan {} {}"
# a="My name is Rohan {1} {0}"
# b=a.format(s1,s2)
a=f"My name is Rohan {s1}{s2}{math.tan(0)}"
print(a)
