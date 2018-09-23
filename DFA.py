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

def get_dfa():
    DFA ={'k': ['0', '1', '2', '3', '4'], 'e': ['a', 'b'], 'f': {'0': {'a': '1', 'b': '2'}, '1': {'a': '1', 'b': '3'}, '2': {'a': '1', 'b': '2'}, '3': {'a': '1', 'b': '4'}, '4': {'a': '1', 'b': '2'}}, 's': ['0'], 'z': ['4']}
    return DFA
