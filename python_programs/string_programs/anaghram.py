# function to check if two strings are
# anagram or not
def check(s1, s2):
    """
    You can check if two strings are anagrams by comparing the frequency of each character in both strings.
    Two strings are anagrams if they contain the same characters with the same frequencies,
    regardless of the order of the characters."""
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")


s1 = "listen"
s2 = "silent"
check(s1, s2)
