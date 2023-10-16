# -*- coding: utf-8 -*-
import itertools

#with brackets
def with_brackets(lst, ops_lst):
    for op in ops_lst: #无括号时的运算情形
        expr1 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+lst[2]+op[2]+lst[3]        
        # expr2 = lst[0]+op[0]+'('+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
        # expr3 = lst[0]+op[0]+lst[1]+op[1]+'('+lst[2]+op[2]+lst[3]+')'

        expr4 = '('+lst[0]+op[0]+lst[1]+op[1]+lst[2]+')'+op[2]+lst[3]
        expr5 = lst[0]+op[0]+'(' + lst[1]+op[1]+lst[2]+op[2]+lst[3]+')'        

        expr6 = '('+lst[0]+op[0]+lst[1]+')'+op[1]+'('+lst[2]+op[2]+lst[3]+')'

        
        
        # for expr in [expr1, expr2, expr3, expr4, expr5, expr6]:
        for expr in [expr1, expr4, expr5, expr6]:    
            try:
                t=eval(expr)
            except: #作除法时，跳过分母为0时的情形
                pass
            
            if abs(t-24) < 0.001:#float型数值计算存在微小的误差
                return expr
    return 0

#返回4个数计算24的方法
def hasMethod(numbers, ops_lst):
    for lst in itertools.permutations(numbers):
        lst = list(map(lambda x:str(x), lst))
        #without brackets
        for op in ops_lst:
            expr = lst[0]+op[0]+lst[1]+op[1]+lst[2]+op[2]+lst[3]
            if abs(eval(expr)-24) < 0.001:
                return expr
        #with brackets
        expr = with_brackets(lst, ops_lst)
        if expr != 0:
            return expr
    
    return 0
        
#返回4个数计算24的方法，无方法时返回"No Method"
def cal_24(numbers,outfile):
    ops = ['+','-','*','/']
    ops_lst = [[i,j,k] for i in ops for j in ops for k in ops]
    
    expr = hasMethod(numbers, ops_lst)
    if expr != 0:
        a = list(map(lambda x: str(x), numbers))
        methodInfo = "[%s,%s,%s,%s]: %s\n"%(a[0],a[1],a[2],a[3],expr)
        outfile.write(methodInfo)
        return expr
    else:
        return 'No method!'

#所有情况的计算24点的办法，并输出到文本文件
def main():
    
    
    numbers_1_lst = [[i,j,k,l] for i in range(1,14) for j in range(1,14)\
                             for k in range(1,14) for l in range(1,14)]
    outfile=open("24dian.txt","w")
    numbers_2_lst = []
    for numbers in numbers_1_lst:
        numbers.sort()
        if numbers not in numbers_2_lst:
            numbers_2_lst.append(numbers)
            cal_24(numbers, outfile)

    outfile.close()
    print("完成")    

main() 