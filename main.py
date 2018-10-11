import NFA as nfa
import DFA as dfa


def main():
  DFA = nfa.nfa_to_dfa()
  print("DFA=",DFA)
  min_DFA = dfa.min_dfa(DFA)
  print("NFA=",min_DFA)

if __name__ == '__main__':
    main()