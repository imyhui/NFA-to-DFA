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
    '''
    获取DFA
    '''
    DFA ={'k': ['0', '1', '2', '3', '4'], 'e': ['a', 'b'], 'f': {'0': {'a': '1', 'b': '2'}, '1': {'a': '1', 'b': '3'}, '2': {'a': '1', 'b': '2'}, '3': {'a': '1', 'b': '4'}, '4': {'a': '1', 'b': '2'}}, 's': ['0'], 'z': ['4']}
    return DFA

def leads_to_status(DFA,statuses,e):
    '''
    找出DFA的状态中，经过一条e弧结果在statuses中的状态
    '''
    res = set()
    for s in DFA['f']:
        if e in DFA['f'][s]:
            if str(DFA['f'][s][e]) in statuses:
                res.add(s)
    return res
def get_divide(DFA):
    '''
    获取最小化DFA划分，详见
    [Hopcroft's algorithm](https://en.wikipedia.org/wiki/DFA_minimization)
    '''
    final = set(DFA['z'])
    no_final = set(DFA['k']) - final
    P = [final,no_final]
    W = [final]
    while len(W):
        A = W[0]
        W.remove(A)
        for e in DFA['e']:
            X = leads_to_status(DFA, A, e)
            for Y in P:
                S1 = X & Y
                S2 = Y - X
                if len(S1) and len(S2):
                    P.remove(Y)
                    P.append(S1)
                    P.append(S2)
                    if Y in W:
                        W.remove(Y)
                        W.append(S1)
                        W.append(S2)
                    else:
                        if len(S1) <= len(S2):
                            W.append(S1)
                        else:
                            W.append(S2)
    return P

def min_dfa(DFA):
    '''
    最小化DFA函数实现
    '''
    # 获取合并数组
    divide = get_divide(DFA)
    to_merge = [i for i in divide if len(i)>1]
    
    for m in to_merge:
        save = min(m)
        to_rm = set(m) - set(save)
        for i in to_rm:
            # 状态集合删除
            DFA['k'].remove(i)
            # 转换函数删除
            for e in DFA['e']:
                for s in DFA['f']:
                    if e in DFA['f'][s]:
                        if DFA['f'][s][e] ==  i:
                            DFA['f'][s][e] = save
            if i in DFA['f']:
                for e in DFA['f'][i]:
                    DFA['f'][save][e] =  DFA['f'][i][e]
            DFA['f'].pop(i)
            # 初态与态删除
            if i in DFA['s']:
                DFA['s'].remove(i)
            if i in DFA['z']:
                DFA['z'].remove(i)
    return DFA
