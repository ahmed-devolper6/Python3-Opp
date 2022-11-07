class Math:
    def sum(self,x,y):
        return x+y
    def mull(self,x,y):
        return x*y

class Sum(Math):
    pass

obj = Sum()
sum_two_numbers = obj.sum(5,4)

print(sum_two_numbers)

'''
the outpot of the code well be 9 the sum of parmter 5 , 4
the Sum class dos'not have the sum function but Inheritance from math class
'''