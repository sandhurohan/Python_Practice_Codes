import Dictonary

# Recomended Method

print(Dictonary.d1)

# Another Way (Avoided Because It Create Ambiguity)

from Dictonary import d1
print(d1)

# We Import File when we want to use functions/modules from another file.
# We dont prefer to write file name as module name because if we did that it wil firstly check local path
# while importing & local will not contain files So Error Will Genrated