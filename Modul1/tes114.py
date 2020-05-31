# nama = 'Andi'

# def tesfunc(x):
#     return x

# class A():
#     def __init__(self,nama) :
#         self.nama = 'Hadi'

# d = vars(A(A))
# print(d)

import json
# def buka(x) :
#     with open (x,'r') as y:
#         data = json.load(y)
#     return data

class jsonku():
    def __init__(self,file):
        self.file=file
    def buka(self):
        with open(self.file) as x:
            return json.load(x) 

