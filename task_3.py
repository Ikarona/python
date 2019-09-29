'''
using itertool
'''
import itertools

KEYBOARD = {"1":"*", "2":"abc", "3":"def",
            "4":"ghi", "5":"jkl", "6":"mno",
            "7":"pqrs", "8":"tuv", "9":"wxyz",
            "0":" "}
X = input()
NEW_LIST = list(("".join(i) for i in itertools.product(*(KEYBOARD[t] for t in X))))
print(NEW_LIST)
