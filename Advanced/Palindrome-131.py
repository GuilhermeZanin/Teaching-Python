def is_palindrome(s):
    """
    Helper function to check if a given string is a palindrome.
    """
    return s == s[::-1]

def partition_helper(s, start, path, result):
    """
    Helper function to recursively partition the string into palindromes.
    """
    if start == len(s):
        result.append(path[:])
        return
    
    for end in range(start, len(s)):
        substring = s[start:end + 1]
        if is_palindrome(substring):
            path.append(substring)
            partition_helper(s, end + 1, path, result)
            path.pop()  # backtrack

def partition(s):
    """
    Main function to return all possible palindrome partitioning of the string.
    """
    result = []
    partition_helper(s, 0, [], result)
    return result

# Example usage
s = "aab"
print(partition(s))  # Output: [["a","a","b"],["aa","b"]]
