'''
Traverse a multi-list is a recurrence problem, and is widely needed in python world, in order to simplify it, I write
some method here. In the future, I will create more methods that can be applied to more data structure to meet the
demand in developing deep learning method
'''

def search_multi_list(source,target):
    tar_type=type(target)
    for i in source:
        if isinstance(i,tar_type):
            if i==target:
                return True
        elif isinstance(i,(list,tuple)):
            if search_multi_list(i,target):
                return True
    return False




if __name__=='__main__':
    a=[['PCXXX', ['0078', '8831'], ['0000', '7777']]]
    print(search_multi_list(a,'7777'))