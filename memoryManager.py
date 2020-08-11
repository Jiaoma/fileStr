# Though, python has its memory collector, but in deep learning task, I often meet
# cuda out of memory, which may cause big damage to the productivity.
# This memoryManager is used to collect both memory in dram and memory in GPU.
import torch
class MemoryManager:
    def __init__(self,vars):
        self.variable=[]
        vars=vars.split(',')
        for i in vars:
            if not any([i==x for x in self.variable]):
                self.variable.append(i)

    def store(self,vars):
        vars = vars.split(',')
        for i in vars:
            if not any([i == x for x in self.variable]):
                self.variable.append(i)

    def soft_clear(self):
        # notice: you must exec(mm.soft_clear())
        re=''
        for i in self.variable:
            re+=i+'=None\n'
        return re

    def hard_clear(self):
        # notice: you must exec(mm.hard_clear()) before soft_clear()
        re=''
        for i in self.variable:
            re+='''try:
    del %s
except:
    pass\n'''%i
        re+='torch.cuda.empty_cache()\n'
        return re


if __name__=='__main__':
    a=torch.Tensor([1232344])
    b=torch.Tensor([21312])
    testMM=MemoryManager('a,b')
    exec(testMM.soft_clear())
    exec(testMM.hard_clear())
