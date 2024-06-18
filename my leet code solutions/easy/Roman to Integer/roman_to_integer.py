class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.upper()
        value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        value = 0
        values = [value_dict[i] for i in s]

        if len(values) == 1:
            return values[0]
        count = 0
        while count <  (len(values) -1):
            if values[count] >= values[count + 1]:
                value += values[count]
                count += 1
            else:
                value += (values[count+1] - values[count])
                count += 2
        if values[-2] >= values[-1]:
            value += values[-1]
        return value
        