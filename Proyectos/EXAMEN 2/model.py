# model.py

import re

class Stack:
    """Implementación simple de una Pila (LIFO)."""
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        # El IndexError ocurre si se intenta pop de una pila vacía.
        raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        raise IndexError("peek from empty stack")

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

# --- FIN DE CLASE STACK ---

class ExpressionProcessor:
    """Procesa expresiones matemáticas infijas, las convierte a prefija y las evalúa."""
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.associativity = {'+': 'left', '-': 'left', '*': 'left', '/': 'left', '^': 'right'}

    def _is_operator(self, char):
        return char in self.precedence

    def _apply_operator(self, op, val1, val2):
        """
        Aplica un operador a dos valores. val1 es el segundo operando, val2 es el primero.
        """
        if op == '+':
            return val2 + val1
        elif op == '-':
            return val2 - val1 
        elif op == '*':
            return val2 * val1
        elif op == '/':
            if val1 == 0:
                raise ValueError("División por cero.")
            return val2 / val1
        elif op == '^':
            return val2 ** val1
        raise ValueError(f"Operador desconocido: {op}")

    def _tokenize(self, expression):
        """Divide la expresión en tokens: números, operadores y paréntesis."""
        token_spec = [
            (r'\d+\.\d+|\d+', 'NUMBER'),      # Números (con o sin decimal)
            (r'[+\-*/^]', 'OPERATOR'),        # Operadores
            (r'[\(\)]', 'PARENTHESIS'),       # Paréntesis
            (r'\s+', 'SKIP'),                 # Ignorar espacios en blanco
            (r'.', 'ERROR')                   # Carácter inválido
        ]
        
        tok_regex = '|'.join(f'(?P<{name}>{pattern})' for pattern, name in token_spec)
        tokens = []
        
        for mo in re.finditer(tok_regex, expression):
            kind = mo.lastgroup
            value = mo.group(kind)
            if kind == 'SKIP':
                continue
            elif kind == 'ERROR':
                raise ValueError(f"Carácter inválido en la expresión: {value}")
            tokens.append(value)
            
        return tokens

    def infix_to_prefix(self, infix_expr):
        """Convierte una expresión infija a su notación prefija."""
        
        tokens = self._tokenize(infix_expr)
        tokens.reverse()
        tokens = [')' if t == '(' else '(' if t == ')' else t for t in tokens]
        
        output_stack = Stack()
        operator_stack = Stack()

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output_stack.push(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                while not operator_stack.is_empty() and operator_stack.peek() != '(':
                    output_stack.push(operator_stack.pop())
                if not operator_stack.is_empty() and operator_stack.peek() == '(':
                    operator_stack.pop()
                else:
                    raise ValueError("Paréntesis desequilibrados.")
            elif self._is_operator(token):
                op1 = token
                while (not operator_stack.is_empty() and 
                       operator_stack.peek() != '(' and 
                       ((self.precedence[operator_stack.peek()] > self.precedence[op1]) or
                        (self.precedence[operator_stack.peek()] == self.precedence[op1] and self.associativity[op1] == 'right'))):
                    output_stack.push(operator_stack.pop())
                operator_stack.push(op1)
            else:
                try:
                    float(token)
                    output_stack.push(token)
                except ValueError:
                    raise ValueError(f"Token desconocido: {token}")

        while not operator_stack.is_empty():
            if operator_stack.peek() == '(':
                raise ValueError("Paréntesis desequilibrados.")
            output_stack.push(operator_stack.pop())
        
        prefix_tokens = []
        while not output_stack.is_empty():
            prefix_tokens.append(output_stack.pop())
            
        return ' '.join(prefix_tokens)

    def evaluate_prefix(self, prefix_expr):
        """Evalúa una expresión en notación prefija."""
        if not prefix_expr.strip():
            return 0

        tokens = prefix_expr.split()
        operand_stack = Stack()

        for token in reversed(tokens):
            try:
                operand_stack.push(float(token))
            except ValueError:
                if self._is_operator(token):
                    if operand_stack.size() < 2:
                        raise ValueError("Expresión prefija inválida: operandos insuficientes.")
                    
                    val1 = operand_stack.pop()
                    val2 = operand_stack.pop()
                    
                    result = self._apply_operator(token, val1, val2) 
                    operand_stack.push(result)
                else:
                    raise ValueError(f"Token desconocido en expresión prefija: {token}")

        if operand_stack.size() == 1:
            return round(operand_stack.pop(), 4) 
        else:
            raise ValueError("Expresión prefija inválida: demasiados operandos o pocos operadores.")