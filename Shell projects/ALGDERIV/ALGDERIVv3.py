class node:
    val = ""
    children_nodes = []
    abs_val = False

    def __init__(self, val, children, abs_val = False):
        self.val = val
        self.children_nodes = children
        self.abs_val = abs_val

    def __str__(self):
        #return "(" + str(self.children_nodes[0]) + self.val + str(self.children_nodes[1]) + ")"
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
            if(type(right) is node):
                if(right.val == "+" or right.val == "-"):
                    r_out = "(" + r_out + ")"
        elif(self.val == "^" or self.val == "-"):
            if(type(left) is node):
                l_out = "(" + l_out + ")"
            if(type(right) is node):
                r_out = "(" + r_out + ")"
        elif(self.val == "trig"):
            return l_out + "(" + r_out + ")"
        if(not self.abs_val):
            return l_out + self.val + r_out
        else:
            return "|" + l_out + self.val + r_out + "|"
            
            

equation_in = "(" + input("Enter an equation. (Don't use the regular x. Use the x/y found by pressing alpha + sto->/1 respectively)\n").replace("**", "^").replace(")(", "*") + ")"
#equation_in = "(4x^3+2x^2+5)/(6x+3)"

equation = ""
prev_c = ""
for c in equation_in:
    if((c == "x" or c == "y" or c == "s" or c == "c" or c == "t" or c == "a") and prev_c.isdigit()):
        equation += "*"
    equation += c
    prev_c = c

equation = equation.split("=")
side = 0

current_char = 0

def get_char():
    global current_char
    return equation[side][current_char:current_char + 1]

def parse_expression(other_side = False):
    global current_char
    if(other_side):
        if("=" in equation_in):
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
    if(get_char().isdigit()):
        while get_char().isdigit():
            token += get_char()
            current_char += 1
        return token

    if(get_char() == "x" or get_char() == "y"):
        token += get_char()
        current_char += 1
        return token

    posible_trig_starts = ["a", "s", "c", "t"]
    cur_char = get_char()
    if(cur_char in posible_trig_starts):
        for i in range(4 if cur_char == "a" else 3):
            token += get_char()
            current_char += 1
        current_char += 1
        return node("trig", [token, parse_expression()])
    
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

            v = node_o.children_nodes[1]
            deriv_v = find_derivative(v)

            return node("/", [node("-", [node("*", [deriv_u, v]), node("*", [u, deriv_v])]), node("^", [v, 2])])

        elif(node_o.val == "^"):
            new_power = node_o.children_nodes[1]
            if(type(new_power) is node):
                if(new_power.val == "/"):
                    comps = new_power.children_nodes
                    comps[0] = str(int(comps[0]) - int(comps[1]))
                    new_power = node("/", *comps)
            else:
                new_power = str(int(new_power) - 1)
            return node("*", [node("*", [node_o.children_nodes[1], node("^", [node_o.children_nodes[0], new_power])]), find_derivative(node_o.children_nodes[0])])

        elif(node_o.val == "trig"):
            func = node_o.children_nodes[0]
            inside = node_o.children_nodes[1]

            if(func == "sin"):
                node_o = node("trig", ["cos", inside])
            elif(func == "cos"):
                node_o = node("*", ["-1", node("trig", ["sin", inside])])
            elif(func == "tan"):
                node_o = node("^", [node("trig", ["sec", inside]), 2])
            elif(func == "csc"):
                node_o = node("*", ["-1", node("*", [node("trig", ["csc", inside]), node("trig", ["cot", inside])])])
            elif(func == "sec"):
                node_o = node("*", [node("trig", ["sec", inside]), node("trig", ["tan", inside])])
            elif(func == "cot"):
                node_o = node("*", ["-1", node("^", [node("trig", ["csc", inside]), 2])])
            elif(func == "asin" or func == "acos"):
                return(node("*", ["1" if func == "asin" else "-1", node("/", [find_derivative(inside), node("^", [node("-", ["1", node("^", [inside, 2])]), node("/", ["1", "2"])])])]))
            elif(func == "asec" or func == "acsc"):
                return node("*", [("1" if func == "asec" else "-1"), node("/", [find_derivative(inside), node("*", [node("+", ["0", inside], True), node("^", [node("-", [node("^", [inside, "2"]), "1"]), node("/", ["1", "2"])])])])])
            elif(func == "atan" or func == "acot"):
                return(node("*", ["1" if func == "atan" else "-1", node("/", [find_derivative(inside), node("+", ["1", node("^", [inside, 2])])])]))

            return node("*", [node_o, find_derivative(inside)])


    else:
        if(node_o == "x" or node_o == "y"):
            return node_o + "'"
        elif(node_o.isdigit()):
            return "0"

def simplify_node(node_o):
    if(type(node_o) is node):
        print(node_o.val)
        left = simplify_node(node_o.children_nodes[0])
        right = simplify_node(node_o.children_nodes[1])
        if(node_o.val == "*"):
            if(left == "0" or right == "0"):
                return "0"
            elif(right == "1"):
                return left
            elif(left == "1"):
                return right
            elif(type(left) is str and type(right) is str):
                if(left.isdigit() and right.isdigit()):
                    return str(int(left) * int(right))
            elif(type(left) is node and type(right) is str):
                if(right.isdigit()):
                    if(left.val == "*"):
                        child = left.children_nodes[1]
                        if(type(child) is str):
                            if(child.isdigit()):
                                right = str(int(child) * int(right))
                                left = left.children_nodes[0]
                    elif(right.val == "/"):
                        child = left.children_nodes[0]
                        if(type(child) is str):
                            if(child.isdigit()):
                                return node("+", [node("/", [str(int(child) * int(right)), left[1]]), 0])
            elif(type(left) is str and type(right) is node):
                if(left.isdigit()):
                    if(right.val == "*" or right.val == "/"):
                        child = right.children_nodes[0]
                        if(type(child) is str):
                            if(child.isdigit()):
                                if(right.val == "*"):
                                    left = str(int(child) * int(left))
                                    right = right.children_nodes[1]
                                else:
                                    return node("/", [str(int(child) * int(left)), right[1]])


        elif(node_o.val == "/"):
            if(right == "1" or left == "0"):
                return left
        elif(node_o.val == "+" or node_o.val == "-"):
            if(right == "0"):
                return left
            elif(left == "0"):
                return right
            elif(type(left) is str and type(right) is str):
                if(left.isdigit() and right.isdigit()):
                    return str(int(left) + int(right) if node_o.val == "+" else int(left) - int(right))
        elif(node_o.val == "^"):
            if(right == "1"):
                return left
            elif(right == "0"):
                return "1"
        node_o.children_nodes = [left, right]
    else:
        if(node_o == "x'"):
            return "1"
    return node_o
            
def simplify_side(e:node):
    return simplify_node(e)

def simplify(left, right):
    left = simplify_side(left)
    if(right == None):
        return left
    else:
        right = simplify_side(right)


expr_l = parse_expression()
deriv_l = find_derivative(expr_l)

expr_r = parse_expression(True)
deriv_r = find_derivative(expr_r) if expr_r != None else None

final = simplify(deriv_l, deriv_r)

print(final)