import queue
from NFA import NFA
import DFA as dfa

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
    DFA['f'][i] = {}
    for e in NFA['e']:
      nextT = sorted(ε_closure(move(T,e)))
      if nextT not in C:
        j = len(C)
        C.append(nextT)
        q.put(nextT)
        DFA["k"].append(j)
      else:
        j = C.index(nextT)
      DFA["f"][i][e] = j
      # 判断是否为初态或终态
      dfa.has_intersection(DFA,NFA,nextT,'s',j)
      dfa.has_intersection(DFA,NFA,nextT,'z',j)
    i = i + 1
  return DFA

def main():
  f = nfa_to_dfa()
  print(f)

if __name__ == '__main__':
    main()