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
  "k": ["0", "1", "2", "3", "4"],
  "e": ["a", "b"],
  "f": {
    "0": {
      "a": ["0", "3"],
      "b": ["0", "1"]
    },
    "1": {
      "b": ["2"]
    },
    "2": {
      "a": ["2"],
      "b": ["2"]
    },
    "3": {
      "a": ["4"]
    },
    "4": {
      "a": ["4"],
      "b": ["4"]
    }
  },
  "s": ["0"],
  "z": ["2","4"]
}

def ε_closure(I):
  '''
  状态集合I的ε-闭包
  '''
  return get_closure(I,set())

def move(I, e):
  '''
  集合I的e弧转换
  '''
  res = set()
  for s in I:
    if s in NFA['f']:
        change = NFA['f'][s]
        if e in change:
              res |= set(change[e])
  return res

def get_closure(I,res):
  '''
  递归查找
  '''
  for s in I:
    tmp = set()
    tmp.add(s)
    if s in NFA['f']:
        change = NFA['f'][s]
        if 'ε' in change:
              tmp |= get_closure(change['ε'], res)
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
      # 判断是否为终态
      dfa.has_intersection(DFA,NFA,nextT,'z',j)
    i = i + 1
  return DFA

