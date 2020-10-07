"""
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging
from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits.
The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid
one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address
to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper
cases).
However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::)
to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
Besides, extra leading zeros in the IPv6 is also invalid. For example, the address
02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
"""


class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if IP.count(".") ==3:
            result = IP.split(".")
            if len(result) >4:
                return "Neither"
            for number in result:
                if not (number.isdigit()):
                    return "Neither"
                if int(number) > 255 or int(number) < 0:
                    return "Neither"
                if len(number) > 3 or len(number) < 0:
                    return "Neither"
            return "IPv4"
        elif IP.count(":") == 7:
            v6 = IP.split(":")
            print (v6)
            hexdigits = '0123456789abcdefABCDEF'
            for ch in v6:
                if len(ch) == 0 or len(ch) >4 or not(all(x in hexdigits for x in ch)):
                    print ("Mistake")
                    return "Neither"
            return "IPV6"
        else:
            return "Neither"




v4 = Solution()
print v4.validIPAddress("55.255.255")
print v4.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334")
print v4.validIPAddress("$AA.55.255.255")




