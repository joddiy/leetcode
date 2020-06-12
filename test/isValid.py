# O(n)
def solution(s):
    stack = []
    for c in s:
        if c in ("(", "[", "{"):
            stack.append(c)
        else:
            if not stack:
                return False
            cc = stack.pop(-1)
            if cc == "(" and c != ")":
                return False
            elif cc == "[" and c!= "]":
                return False
            elif cc == "{" and c!= "}":
                return False
    return not stack

print(solution(r"()[]{}"))