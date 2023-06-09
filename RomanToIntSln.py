class Solution:

    def romanToInt(self, s: str) -> int:
        romanNumerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        result = 0

        for i in range(len(s)-1): # Iterate through the string given
            if romanNumerals[s[i]] < romanNumerals[s[i+1]]: # For cases such as 'IV', 'XL'...
                result = result - romanNumerals[s[i]]   # Subtract from value
            else: # For all else cases
                result = result + romanNumerals[s[i]] # Add to result

        return result + romanNumerals[s[-1]] # Return once string has been fully iterated