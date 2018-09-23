import queue
import DFA as dfa

# 定义NFA
'''
k 状态集
e 字母表
f 转换函数
s 初态集
z 终态集
'''
NFA = {
  "k": ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"],
  "e": ["a", "b"],
  "f": {
    "0": {
      "ε": ["1", "7"]
    },
    "1": {
      "ε": ["2", "4"]
    },
    "2": {
      "a": ["3"]
    },
    "3": {
      "ε": ["6"]
    },
    "4": {
      "b": ["5"]
    },
    "5": {
      "ε": ["6"]
    },
    "6": {
      "ε": ["1", "7"]
    },
    "7": {
      "a": ["8"]
    },
    "8": {
      "b": ["9"]
    },
    "9": {
      "b": ["10"]
    }
  },
  "s": ["0"],
  "z": ["10"]
}

def ε_closure(I):
  '''
  状态集合I的ε-闭包
  '''
  return get_closure(I,'ε',set())

def move(I, e):
  '''
  集合I的e弧转换
  '''
  return get_closure(I,e,set())

def get_closure(I,e,res):
  '''
  递归查找
  '''
  for s in I:
    tmp = set()
    if e == 'ε':
      tmp.add(s)
    if s in NFA['f']:
        change = NFA['f'][s]
        if e in change:
            if e == 'ε':
              tmp |= get_closure(change[e],e,res)
            else:
              tmp = set(change[e])
    res |= tmp
  return res

def nfa_to_dfa():
  '''
  NFA 转 DFA的函数实现
  '''
  # 子集族
  C = []
  # 尚未标记的子集
  q = queue.Queue()

  # 获取T0
  T0 = sorted(ε_closure(NFA['s']))
  # 初始化DFA
  DFA = dfa.init_dfa(NFA,T0)

  C.append(T0)
  q.put(T0)

  # 记录当前元素
  i = 0

  while not q.empty():
    T = q.get()
    DFA['f'][str(i)] = {}
    for e in NFA['e']:
      nextT = sorted(ε_closure(move(T,e)))
      if nextT not in C:
        j = str(len(C))
        C.append(nextT)
        q.put(nextT)
        DFA["k"].append(j)
      else:
        j = str(C.index(nextT))
      DFA["f"][str(i)][e] = j
      # 判断是否为初态或终态
      dfa.has_intersection(DFA,NFA,nextT,'s',j)
      dfa.has_intersection(DFA,NFA,nextT,'z',j)
    i = i + 1
  return DFA

