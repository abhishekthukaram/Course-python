class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        signs = ["-", "+"]
        output = ""
        for position, value in enumerate(str):
            if position == 0 and value in signs:
                continue

            if not value.isnumeric():
                break;

            output += value
        print output
        if not output:
            return 0
        output = -int(output) if str[0] == '-' else int(output)
        # except ValueError as e:
        # pass
        print int(output)
        min_value, max_value = -2 ** 31, 2 ** 31 - 1
        # output = int(output)
        if output < min_value:
            return min_value
        elif output > max_value:
            return max_value
        else:
            return int(output)