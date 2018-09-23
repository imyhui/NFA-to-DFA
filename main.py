import NFA as nfa
import DFA as dfa


def main():
  DFA = nfa.nfa_to_dfa()
  min_DFA = dfa.min_dfa(DFA)
  print(min_DFA)

if __name__ == '__main__':
    main()