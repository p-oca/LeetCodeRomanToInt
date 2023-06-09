# Notes
Inspired by [AlgoEngine's solution](https://www.google.com/search?client=firefox-b-d&q=markdown+cheat+sheet).
## Pseudocode
```
class Solution:
    function romanToInt(s: string) -> integer:
        romanNumerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0

        for i from 0 to length(s) - 2:
            if romanNumerals[s[i]] is less than romanNumerals[s[i+1]]:
                result = result - romanNumerals[s[i]]
            else:
                result = result + romanNumerals[s[i]]

        return result + romanNumerals[last character of s]
```
## Explanation
- To account for the cases such as 'IV', 'XL' and 'CD' the statement within the if just subtracts from the continuing result.
