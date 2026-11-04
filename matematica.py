import ast
import operator as op

OPS = {
    ast.Add: op.add, ast.Sub: op.sub,
    ast.Mult: op.mul, ast.Div: op.truediv,
    ast.Pow: op.pow, ast.USub: op.neg,
}

def _avaliar(no):
    if isinstance(no, ast.Constant) and isinstance(no.value, (int, float)):
        return no.value
    if isinstance(no, ast.BinOp) and type(no.op) in OPS:
        return OPS[type(no.op)](_avaliar(no.left), _avaliar(no.right))
    if isinstance(no, ast.UnaryOp) and type(no.op) in OPS:
        return OPS[type(no.op)](_avaliar(no.operand))
    raise ValueError

def calcular(expressao):
    try:
        expressao = expressao.replace("^", "**")
        resultado = _avaliar(ast.parse(expressao, mode="eval").body)
        return str(resultado)
    except Exception:
        return "Não consegui resolver essa expressão."