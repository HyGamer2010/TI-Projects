class node:
    val = ""
    children_nodes = []
    abs_val = False

    def __init__(self, val, children, abs_val = False):
        self.val = val
        self.children_nodes = children
        self.abs_val = abs_val

    def __str__(self):
        left = self.children_nodes[0]
        right = self.children_nodes[1]

        l_out = str(left)
        r_out = str(right)

        if(self.val == "/"):
            if(type(left) is not str):
                l_out = "(" + l_out + ")"
            if(type(right) is not str):
                r_out = "(" + r_out + ")"
        elif(self.val == "*"):
            if(type(left) is node):
                if(left.val == "+" or left.val == "-"):
                    l_out = "(" + l_out + ")"
            elif(len(l_out.lstrip("-")) == 1):
                l_out = l_out.replace("1", "")
            if(type(right) is node):
                if(right.val == "+" or right.val == "-"):
                    r_out = "(" + r_out + ")"
                if(type(left) is str):
                    if(is_const(left)):
                        return l_out + r_out
            elif(type(right) is str):
                if(type(left) is node):
                    c_node = left.children_nodes[1]
                    if(type(c_node) is node):
                        if(c_node.val == "^"):
                            return l_out + " * " + r_out
                if(not right.lstrip("-").isdigit()):
                    return l_out + r_out
        elif(self.val == "^" or self.val == "-"):
            if(type(left) is node):
                l_out = "(" + l_out + ")"
            if(type(right) is node):
                r_out = "(" + r_out + ")"
        elif(self.val == "func"):
            return l_out + "(" + r_out + ")"
        elif(self.val == "log"):
            if(r_out == "e"):
                return "ln(" + l_out + ")"
            else:
                return "log(" + l_out + "," + r_out + ")"

        if(not self.abs_val):
            return l_out + (" " + self.val + " " if self.val != "^" else self.val) + r_out
        else:
            return "| " + l_out + (" " + self.val + " " if self.val != "^" else self.val) + r_out + " |"
            
def is_const(x:str):
    return x.lstrip("-").isdigit() or x == "e" or x == "&"

equation_in = "(" + input("Enter an equation. (Don't use the regular x. Use the x/y found by pressing alpha + sto->/1 respectively)\n").replace("**", "^").replace(")(", "*").replace("1/sin", "csc").replace("1/cos", "sec").replace("1/tan", "cot").replace("1/asin", "acsc").replace("1/acos", "asec").replace("1/atan", "acot").replace("pi", "&") + ")"
#equation_in = "tan(x*y)+x^2*y^2=2x^2+3x"

equation = ""
prev_c = ""
for c in equation_in:
    if(((c.lstrip("-").isdigit() and not prev_c.lstrip("-").isdigit()) or (prev_c.lstrip("-").isdigit() and not c.lstrip("-").isdigit()) or (c == "x" or c == "y" or c == "s" or c == "c" or c == "t" or c == "a" or c == "l")) and is_const(prev_c) and c != "^" and c != "+" and c != "-" and c != "*" and c != "/" and c != ")" and c != "="):
        equation += "*"
    equation += c
    prev_c = c
equation = equation.split("=")
for i in range(len(equation)):
    equation[i] = "(" + equation[i] + ")"
side = 0

current_char = 0

def get_char():
    global current_char
    return equation[side][current_char:current_char + 1]

def parse_expression(other_side = False):
    global current_char
    global side
    if(other_side):
        if("=" in equation_in):
            current_char = 0
            side += 1
        else:
            return None
    left_node = parse_term()

    while(get_char() == "+" or get_char() == "-"):
        op = get_char()
        current_char += 1
        right_node = parse_term()
        left_node = node(op, [left_node, right_node])

    return left_node

def parse_term():
    global current_char
    left_node = parse_power()

    while(get_char() == "*" or get_char() == "/"):
        op = get_char()
        current_char += 1
        right_node = parse_power()
        left_node = node(op, [left_node, right_node])

    return left_node

def parse_power():
    global current_char
    left_node = parse_factor()

    if(get_char() == "^"):
        op = get_char()
        current_char += 1
        right_node = parse_factor()
        left_node = node(op, [left_node, right_node])

    return left_node

def parse_factor():
    global current_char
    token = ""
    if(is_const(get_char())):
        while is_const(get_char()):
            token += get_char()
            current_char += 1
        return token

    if(get_char() == "x" or get_char() == "y"):
        token += get_char()
        current_char += 1
        return token

    posible_func_starts = ["a", "s", "c", "t"]
    cur_char = get_char()
    if(cur_char in posible_func_starts):
        for i in range(4 if cur_char == "a" else 2 if cur_char == "l" else 3):
            token += get_char()
            current_char += 1
        current_char += 1
        return node("func", [token, parse_expression()])

    if(cur_char == "l"):
        current_char += 1
        if(get_char() == "n"):
            current_char += 2
            inside = parse_expression()
            return node("log", [inside, "e"])
        if(get_char() == "o"):
            current_char += 3
            inside = parse_expression()
            current_char += 1
            base = parse_expression()
            return node("log", [inside, base])
            
    
    if(get_char() == "(" or get_char() == "|"):
        abs_val = get_char() == "|"
        current_char += 1

        tree = parse_expression()
        if(type(tree) is node):
            tree.abs_val = abs_val

        current_char += 1
        return tree

def find_derivative(node_o):
    if(type(node_o) is node):
        if(node_o.val == "+" or node_o.val == "-"):
            return node(node_o.val, [find_derivative(node_o.children_nodes[0]), find_derivative(node_o.children_nodes[1])])

        elif(node_o.val == "*"):
            u = node_o.children_nodes[0]
            deriv_u = find_derivative(u)

            v = node_o.children_nodes[1]
            deriv_v = find_derivative(v)

            return node("+", [node("*", [deriv_u, v]), node("*", [u, deriv_v])])

        elif(node_o.val == "/"):
            u = node_o.children_nodes[0]
            deriv_u = find_derivative(u)

            v = node("^", [node_o.children_nodes[1], "-1"])
            deriv_v = find_derivative(v)

            return node("+", [node("*", [deriv_u, v]), node("*", [u, deriv_v])])

        elif(node_o.val == "^"):
            if(type(node_o.children_nodes[1]) is str):
                if(is_const(node_o.children_nodes[1])):
                    new_power = node_o.children_nodes[1]
                    if(type(new_power) is node):
                        if(new_power.val == "/"):
                            comps = new_power.children_nodes
                            comps[0] = str(int(comps[0]) - int(comps[1]))
                            new_power = node("/", *comps)
                    else:
                        new_power = str(int(new_power) - 1)
                    return node("*", [node("*", [node_o.children_nodes[1], node("^", [node_o.children_nodes[0], new_power])]), find_derivative(node_o.children_nodes[0])])
                else:
                    return node("*", [node("*", [node("log", [node_o.children_nodes[0], "e"]), node("^", [node_o.children_nodes[0], node_o.children_nodes[1]])]), find_derivative(node_o.children_nodes[1])])
            else:
                return node("*", [node("*", [node("log", [node_o.children_nodes[0], "e"]), node("^", [node_o.children_nodes[0], node_o.children_nodes[1]])]), find_derivative(node_o.children_nodes[1])])

        elif(node_o.val == "func"):
            func = node_o.children_nodes[0]
            inside = node_o.children_nodes[1]

            if(func == "sin"):
                node_o = node("func", ["cos", inside])
            elif(func == "cos"):
                node_o = node("*", ["-1", node("func", ["sin", inside])])
            elif(func == "tan"):
                node_o = node("^", [node("func", ["sec", inside]), "2"])
            elif(func == "csc"):
                node_o = node("*", ["-1", node("*", [node("func", ["csc", inside]), node("func", ["cot", inside])])])
            elif(func == "sec"):
                node_o = node("*", [node("func", ["sec", inside]), node("func", ["tan", inside])])
            elif(func == "cot"):
                node_o = node("*", ["-1", node("^", [node("func", ["csc", inside]), "2"])])
            elif(func == "asin" or func == "acos"):
                return(node("*", ["1" if func == "asin" else "-1", node("/", [find_derivative(inside), node("^", [node("-", ["1", node("^", [inside, 2])]), node("/", ["1", "2"])])])]))
            elif(func == "asec" or func == "acsc"):
                return node("*", [("1" if func == "asec" else "-1"), node("/", [find_derivative(inside), node("*", [node("+", ["0", inside], True), node("^", [node("-", [node("^", [inside, "2"]), "1"]), node("/", ["1", "2"])])])])])
            elif(func == "atan" or func == "acot"):
                return(node("*", ["1" if func == "atan" else "-1", node("/", [find_derivative(inside), node("+", ["1", node("^", [inside, 2])])])]))

            return node("*", [node_o, find_derivative(inside)])
        elif(node_o.val == "log"):
            return node("/", [find_derivative(node_o.children_nodes[0]), node("*", [node("log", [node_o.children_nodes[1], "e"]), node_o.children_nodes[0]])])


    else:
        if(node_o == "x" or node_o == "y"):
            return node_o + "'"
        elif(is_const(node_o)):
            return "0"

def get_terms(node_o, negative = False):
    if(type(node_o) is node):
        if(node_o.val == "+" or node_o.val == "-"):
            terms = []
            terms.extend(get_terms(node_o.children_nodes[0], negative))
            terms.extend(get_terms(node_o.children_nodes[1], (node_o.val == "-" and not negative) or (node_o.val == "+" and negative)))

            return terms
        else:
            if(not negative):
                return [node_o]
            else:
                return [node("*", ["-1", node_o])]
    else:
        if(not negative):
            return [node_o]
        else:
            return [node("*", ["-1", node_o])]

def find_y_prime(node_o):
    if(type(node_o) is node):
        left = find_y_prime(node_o.children_nodes[0])
        right = find_y_prime(node_o.children_nodes[1])

        return left or right
    elif(type(node_o) is str):
        return node_o == "y'"

def take_out_y_prime(node_o):
    if(type(node_o) is node):
        left = take_out_y_prime(node_o.children_nodes[0])
        right = take_out_y_prime(node_o.children_nodes[1])

        node_o.children_nodes[0] = left
        node_o.children_nodes[1] = right

        return node_o
    elif(type(node_o) is str):
        if(node_o == "y'"):
            return "1"
        else:
            return node_o

def solve_for_y_prime(left, right):
    new_left = "0"
    new_right = "0"

    left_terms = get_terms(left)
    for term in left_terms:
        if(find_y_prime(term)):
            term_left = term.children_nodes[0]
            term_right = term.children_nodes[1]
            if(term.val == "*"):
                if(type(term_left) is node and find_y_prime(term_left)):
                    if(term_left.val == "+"):
                        left_terms.extend([node("*", [term_left.children_nodes[0], term_right]),node("*", [term_left.children_nodes[1], term_right])])
                        continue
                    if(term_left.val == "-"):
                        left_terms.extend([node("*", [term_left.children_nodes[0], term_right]),node("*", ["-1",node("*", [term_left.children_nodes[1], term_right])])])
                        continue
                elif(type(term_right) is node and find_y_prime(term_right)):
                    if(term_right.val == "+"):
                        left_terms.extend([node("*", [term_right.children_nodes[0], term_left]),node("*", [term_right.children_nodes[1], term_left])])
                        continue
                    elif(term_right.val == "-"):
                        left_terms.extend([node("*", [term_right.children_nodes[0], term_left]),node("*", ["-1",node("*", [term_right.children_nodes[1], term_left])])])
                        continue
            new_left = node("+", [new_left, term])
        else:
            new_right = node("-", [new_right, term])

    right_terms = get_terms(right)
    for term in right_terms:
        if(find_y_prime(term)):
            term_left = term.children_nodes[0]
            term_right = term.children_nodes[1]
            if(term.val == "*"):
                if(type(term_left) is node and find_y_prime(term_left)):
                    if(term_left.val == "+"):
                        right_terms.extend([node("*", [term_left.children_nodes[0], term_right]),node("*", [term_left.children_nodes[1], term_right])])
                        continue
                    if(term_left.val == "-"):
                        right_terms.extend([node("*", [term_left.children_nodes[0], term_right]),node("*", ["-1",node("*", [term_left.children_nodes[1], term_right])])])
                        continue
                elif(type(term_right) is node and find_y_prime(term_right)):
                    if(term_right.val == "+"):
                        right_terms.extend([node("*", [term_right.children_nodes[0], term_left]),node("*", [term_right.children_nodes[1], term_left])])
                        continue
                    elif(term_right.val == "-"):
                        right_terms.extend([node("*", [term_right.children_nodes[0], term_left]),node("*", ["-1",node("*", [term_right.children_nodes[1], term_left])])])
                        continue
            new_left = node("-", [new_left, term])
        else:
            new_right = node("+", [new_right, term])

    new_left = take_out_y_prime(new_left)

    return node("/", [new_right, new_left])

def take_out_constants(node_o):
    if(type(node_o) is not str and type(node_o) is not node):
        const_list = node_o[0]
        node_o = node_o[1]
    else:
        const_list = []
    if(type(node_o) is node):
        if(node_o.val == "*"):
            left = take_out_constants(node_o.children_nodes[0])
            right = take_out_constants(node_o.children_nodes[1])

            final_nodes = []
            if(type(left) is not str and type(left) is not node):
                const_list.extend(left[0])
                final_nodes.append(left[1])
            else:
                final_nodes.append(left)
            if(type(right) is not str and type(right) is not node):
                const_list.extend(right[0])
                final_nodes.append(right[1])
            else:
                final_nodes.append(right)

            if(type(left) is str):
                if(left.lstrip("-").isdigit()):
                    const_list.append(left)
            if(type(right) is str):
                if(right.lstrip("-").isdigit()):
                    const_list.append(right)

            return (const_list, node("*", *final_nodes))
                        
        else:
            return node_o
    else:
        return node_o

def simplify_node(node_o):
    if(type(node_o) is node):
        left = simplify_node(node_o.children_nodes[0])
        right = simplify_node(node_o.children_nodes[1])
        if(node_o.val == "*"):
            if(left == "0" or right == "0"):
                return "0"
            elif(right == "1"):
                return left
            elif(left == "1"):
                return right
            # else:
            #     vals = take_out_constants(node("*", [left, right]))
            #     final_const = 1
            #     for const in vals[0]:
            #         final_const *= int(const)

            #     return node("*", [str(final_const), vals[1]])

            elif(type(left) is str and type(right) is str):
                if(left.lstrip("-").isdigit() and right.lstrip("-").isdigit()):
                    return str(int(left) * int(right))
                
            elif(type(left) is node and type(right) is str):
                if(right.lstrip("-").isdigit()):
                    if(left.val == "*"):
                        child = left.children_nodes[1]
                        if(type(child) is str):
                            if(child.lstrip("-").isdigit()):
                                right = str(int(child) * int(right))
                                left = left.children_nodes[0]
                    elif(left.val == "/"):
                        child = left.children_nodes[0]
                        if(type(child) is str):
                            if(child.lstrip("-").isdigit()):
                                return node("+", [node("/", [str(int(child) * int(right)), left.children_nodes[1]]), 0])

            elif(type(left) is str and type(right) is node):
                if(left.lstrip("-").isdigit()):
                    if(right.val == "*" or right.val == "/"):
                        prev_gp = node_o
                        prev_child = right
                        child = right.children_nodes[0]
                        other = right.children_nodes[1]
                        if(type(child) is str):
                            if(child.lstrip("-").isdigit()):
                                if(prev_gp.val == "*" and prev_child.val == "*"):
                                    left = str(int(child) * int(left))
                                    right = other

        elif(node_o.val == "/"):
            if(right == "1" or left == "0"):
                return left
        elif(node_o.val == "+" or node_o.val == "-"):
            if(right == "0"):
                return left
            elif(left == "0"):
                if(node_o.val == "+"):
                    return right
                else:
                    return node("*", ["-1", right])
            elif(type(left) is str and type(right) is str):
                if(left.lstrip("-").isdigit() and right.lstrip("-").isdigit()):
                    return str(int(left) + int(right) if node_o.val == "+" else int(left) - int(right))
        elif(node_o.val == "^"):
            if(right == "1"):
                return left
            elif(right == "0"):
                return "1"
        elif(node_o.val == "log"):
            if(left == right):
                return "1"
            if(left == "1"):
                return "0"
        node_o.children_nodes = [left, right]
    else:
        if(node_o == "x'"):
            return "1"
    return node_o

def simplify(left, right):
    left = simplify_node(left)
    if(right == None):
        return left
    else:
        right = simplify_node(right)

        return "y' = " + str(simplify_node(solve_for_y_prime(left, right)))

expr_l = parse_expression()
deriv_l = find_derivative(expr_l)

expr_r = parse_expression(True)
deriv_r = find_derivative(expr_r) if expr_r != None else None

final = str(simplify(deriv_l, deriv_r)).replace("&", "pi")

print(final)