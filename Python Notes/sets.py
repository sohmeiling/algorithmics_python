##### ------------------------------------------------------------- #####
# Sets are used to store multiple items in a single variable.
# Sets are unordered, unindexed.

thisset = {"apple", "banana", "cherry"}
print(thisset)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)



##### ------------------------------------------------------------- #####
# 1 - No duplicates. Sets cannot have two items with the same value.
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)



##### ------------------------------------------------------------- #####
# 2 - Length of Sets
print(len(thisset))