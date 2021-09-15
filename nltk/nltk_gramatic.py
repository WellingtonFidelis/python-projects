import re
import nltk

grammar2 = nltk.CFG.fromstring("""
    list -> element list | element
    element -> letter digit
    letter -> "A" | "B" | "C"
    digit -> "1" | "2" | "3" | "4"
""")

def main():
    print("Entre com uma expressão")
    test_string: str = input()
    regex_config = '([A|B|C]+[1|2|3|4])'
    result = re.match(regex_config, test_string)

    if result is None:
        print(f'String "{test_string}", inválida.')
    else:
        print('String "{}", válida.'.format(test_string))

    return test_string


result_string = " ".join(main())
print(result_string)

tokens = result_string.split()  # separa a string
cp = nltk.ChartParser(grammar2)
for tree in cp.parse(tokens):
    print(tree)
    