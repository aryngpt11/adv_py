import sys
print(sys.getrecursionlimit())
sys.setrecursionlimit(500)
print(sys.getrecursionlimit())
def demo():
    print("hello")
    #demo() recusrsion
demo()