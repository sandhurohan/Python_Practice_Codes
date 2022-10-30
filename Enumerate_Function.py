list=["Item 0","Item 1","Item 2","Item 3","Item 4"]

# Enumerate function is used for shortcutbor faccilation

# Normal Way to Print Odd Items


# i=1
# for item in list:
#     if i%2!=0:
#         print(f"Odd Items Are {item}")
#     i+=1

# If We Use Enumerate Function

for index, item in enumerate(list):
    if index%2==0:
        print(f"Odd Items Are {item}")

# In enumeration Indexing start From index 1 rather than zero
