import NFA as nfa
import DFA as dfa


def main():
  f = nfa.nfa_to_dfa()
  print(f)
#   DFA = dfa.get_dfa()
  # min_dfa(DFA)

if __name__ == '__main__':
    main()