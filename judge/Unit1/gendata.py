import random
import sympy

intPool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 常量池
hasWhiteSpace = False  # 是否加入空白字符
hasLeadZeros = False  # 数字是否有前导零,如果传入sympy的表达式中数字有前导零，sympy将无法识别
maxTerm = 3  # 表达式中的最大项数
maxFactor = 3  # 项中最大因子个数
specialData = [
    "+(-03*x+-	 000*x^+1)*(		x^ 4*x 	* 	+2147483647  + 	+x^+008	*009*	 00--06*x)*(-017*0- -+01*x*x^007)---12*(10*		0023333333233333332333 	-+x ^+8*x^	+006*x^4+ -x^+08*x^005)		^+006*	(-x^+00 *-017*x+--0018*x*0010)	^+04"]  # 可以放一些特殊数据
specialData[0] = specialData[0].replace("^", "**")
globalPointer = 0


def rd(a, b):
    return random.randint(a, b)


def getWhiteSpace():
    if hasWhiteSpace == False:
        return ""
    str = ""
    cnt = rd(0, 2)
    for i in range(cnt):
        type = rd(0, 1)
        if type == 0:
            str = str + " "
        else:
            str = str + "\t"
    return str


def getSymbol():
    if rd(0, 1) == 1:
        return "+"
    else:
        return "-"


def getNum(positive):
    result = ""
    integer = intPool[rd(0, len(intPool) - 1)]
    iszero = rd(0, 2)
    for i in range(iszero):
        result = result + "0"
    if hasLeadZeros == False:
        result = ""
    result = result + str(integer)
    if rd(0, 1) == 1:
        if positive == True:
            result = "+" + result
        else:
            result = getSymbol() + result
            # print("num:"+result)
    return result


def getExponent():
    result = "**"
    result = result + getWhiteSpace()
    case = rd(0, 2)
    if rd(0, 1) == 1:
        result = result + "+"
    if case == 0:
        result = result + "0"
    elif case == 1:
        result = result + "1"
    else:
        result = result + "2"
        # result = result + getNum(True)
    # print("exponent:"+result)
    return result


def getPower():
    result = "x"
    if rd(0, 1) == 1:
        result = result + getWhiteSpace() + getExponent()
    # print("Power:"+result)
    return result


def getTerm(genExpr):
    factorNum = rd(1, maxFactor)
    result = ""
    if rd(0, 1) == 1:
        result = getSymbol() + getWhiteSpace()
    for i in range(factorNum):
        factor = rd(0, 2)
        if factor == 0:
            result = result + getNum(False)
        elif factor == 1:
            result = result + getPower()
        elif factor == 2 and genExpr == True:
            result = result + getExpr(True)
        else:
            result = result + "0"
        if i < factorNum - 1:
            result = result + getWhiteSpace() + "*" + getWhiteSpace()
            # print("term:"+result)
    return result


def getExpr(isFactor):
    termNum = rd(1, maxTerm)
    result = getWhiteSpace()
    genExpr = True
    if isFactor == True:
        genExpr = False
    for i in range(termNum):
        result = result + getSymbol() + getWhiteSpace() + getTerm(genExpr) + getWhiteSpace()
    if isFactor == True:
        result = "(" + result + ")"
        if rd(0, 1) == 1:
            result = result + getWhiteSpace() + getExponent()
            # print("Expr:"+result)
    return result


def genData():
    global globalPointer
    if globalPointer < len(specialData):
        expr = specialData[globalPointer]
        globalPointer = globalPointer + 1
    else:
        expr = getExpr(False)
    x = sympy.Symbol('x')
    simplifed = sympy.expand(eval(expr))
    return str(expr), str(simplifed)
