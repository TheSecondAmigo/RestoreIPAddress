#!/usr/bin/env python3

"""
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

"""

class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def getipaddr(fulllist, thislist, substr):

            # if len(thislist) == 4 and len(substr) == 0:
            #     fulllist.append(thislist)
            #     return

            if len(thislist) == 0:
                if len(substr) >= 2 and len(substr[1:]) <= 9:
                    myl = list()
                    myl.append(substr[0])
                    getipaddr(fulllist, myl, substr[1:])
                if not substr.startswith('0') and len(substr) >= 3 and len(substr[2:]) <= 9:
                    myl = list()
                    myl.append(substr[0:2])
                    getipaddr(fulllist, myl, substr[2:])
                if not substr.startswith('0') and len(substr) >= 3 and int(substr[0:3]) <= 255 and len(substr[3:]) <= 9:
                    myl = list()
                    myl.append(substr[0:3])
                    getipaddr(fulllist, myl, substr[3:])

            if len(thislist) == 1:
                if len(substr) >= 2 and len(substr[1:]) <= 6:
                    myl = list(thislist)
                    myl.append(substr[0])
                    getipaddr(fulllist, myl, substr[1:])
                if not substr.startswith('0') and len(substr) >= 3 and len(substr[2:]) <= 6:
                    myl = list(thislist)
                    myl.append(substr[0:2])
                    getipaddr(fulllist, myl, substr[2:])
                if not substr.startswith('0') and len(substr) >= 3 and int(substr[0:3]) <= 255 and len(substr[3:]) <= 6:
                    myl = list(thislist)
                    myl.append(substr[0:3])
                    getipaddr(fulllist, myl, substr[3:])

            if len(thislist) == 2:
                if len(substr) >= 2 and len(substr[1:]) <= 3:
                    myl = list(thislist)
                    myl.append(substr[0])
                    getipaddr(fulllist, myl, substr[1:])
                if not substr.startswith('0') and len(substr) >= 3 and len(substr[2:]) <= 3:
                    myl = list(thislist)
                    myl.append(substr[0:2])
                    getipaddr(fulllist, myl, substr[2:])
                if not substr.startswith('0') and len(substr) >= 3 and int(substr[0:3]) <= 255 and len(substr[3:]) <= 3:
                    myl = list(thislist)
                    myl.append(substr[0:3])
                    getipaddr(fulllist, myl, substr[3:])

            if len(thislist) == 3:
                if len(substr) >= 1 and int(substr) <= 255:
                    if not (substr.startswith('0') and len(substr) > 1):
                        thislist.append(substr)
                        fulllist.append(".".join(thislist))


        fulllist = list()
        myl = list()
        getipaddr(fulllist, myl, s)

        # print(fulllist)
        return fulllist


if __name__ == "__main__":


    s1 = "25525511135"
    exp1 = ["255.255.11.135", "255.255.111.35"]

    s2 = "010010"
    exp2 = ["0.10.0.10","0.100.1.0"]

    tests = [(s1, exp1), (s2, exp2)]

    soln = Solution()

    for s, exp in tests:
        print(f"S = {s}")
        rc = soln.restoreIpAddresses(s)
        print("exp = {}".format(exp))
        print("rc  = {}".format(rc))
        print("{}".format(exp == rc))

