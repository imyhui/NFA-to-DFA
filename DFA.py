def init_dfa(NFA,first):
    '''
    初始化DFA
    '''
    DFA = {
    "k" : [],
    "e" : NFA['e'],
    "f" : {},
    "s" : [],
    "z" : [],
    }
    DFA["k"].append("0")
    DFA["s"].append("0")
    has_intersection(DFA,NFA,first,'z',0)
    return DFA

def has_intersection(DFA,NFA,T,m,value):
    '''
    判断是否与初态集或终态集有交集，如果有，添加到DFA的对应集合中
    '''
    if not len(set(T) & set(NFA[m])) == 0:
        DFA[m].append(value)   
