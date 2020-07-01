# BEGIN (write your solution here)
def rpn_calc(item):
    sym = []
    for i in item:
        if i == '+':
            sym[-2: -1] = [sym[-2] + sym[-1]]
            sym.pop()
        elif i == '*':
            sym[-2: -1] = [sym[-2] * sym[-1]]
            sym.pop()
        elif i == '-':
            sym[-2: -1] = [sym[-2] - sym[-1]]
            sym.pop()
        elif i == '/':
            sym[-2: -1] = [sym[-2] / sym[-1]]
            sym.pop()
        else:
            sym.append(i)
    return sym[0]
# END
rpn_calc([7, 2, 3, '*', '-'])