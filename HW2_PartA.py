##############################################################################
#   Programmer:     Jerome Santos                                            #
#   SID:            011555815                                                #
#   Date:           02/13/17                                                 #
#   OS Used:        Windows 7                                                #
#   Course:         CPT_S 355--Programming Language Design                   #
#   Term:           Spring 2017                                              #
#   Assignment:     HW2 Part A                                               #
#   Description:    Program designed to interpret simple Postscript (SPS)    #
#                   code. This program utilizes Lists as the operand and     #
#                   dictionary stack. Common stack operations are provided   #
#                   such as:                                                 #
#                       - Pop()                                              #
#                       - Push()                                             #
#                   Various arithmetic operations are offered as well:       #
#                       - Add, subtract, multiply, divide                    #
##############################################################################

# ----------------------------- Operand Stack ------------------------------ #
##############################################################################
#   Variable:       opStack                                                  #
#   Data Type:      List                                                     #
#   Assoc Func:     opPop(), opPush(), add(), sub(), mult(), div()           #
#   Description:    Variable designed to hold various data types in a list.  #
#                   **NOTE** Top of the stack is the last slot in the list.  #
##############################################################################
opStack = []


##############################################################################
#   Function:       isString()                                               #
#   Parameters:     value                                                    #
#   Output:         boolean                                                  #
#   Description:    Function designed to determine if the value is a string  #
#                   type.                                                    #
##############################################################################
def isString(value):
    if isinstance(value, str):
        return True
    else:
        print("ERROR--Value is not of type: String!")
        return False


##############################################################################
#   Function:       isEmpty()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to determine if the stack is empty.    #
##############################################################################
def isEmpty():
    if len(opStack) < 1:
        print("ERROR--The stack is empty!")
        return True
    else:
        return False


##############################################################################
#   Function:       opPop()                                                  #
#   Parameters:     none                                                     #
#   Output:         value                                                    #
#   Description:    Function designed to pop a value off of the end of the   #
#                   operand stack, if it exists. That value is returned.     #
##############################################################################
def opPop():
    if len(opStack) >= 1:
        poppedVal = opStack[-1]
        del opStack[-1]
        return poppedVal
    else:
        print("ERROR--Insufficient stack size!")


##############################################################################
#   Function:       opPush()                                                 #
#   Parameters:     value                                                    #
#   Output:         none                                                     #
#   Description:    Function designed to push a new value onto the end of    #
#                   the operand stack.                                       #
##############################################################################
def opPush(value):
    opStack.append(value)


# ---------------------------- Dictionary Stack ---------------------------- #
##############################################################################
#   Variable:       dictStack                                                #
#   Data Type:      List                                                     #
#   Assoc Func:     dictPop(), dictPush()                                    #
#   Description:    Variable designed to hold various dictionaries in a list.#
##############################################################################
dictStack = []


##############################################################################
#   Function:       isDict()                                                 #
#   Parameters:     value                                                    #
#   Output:         boolean                                                  #
#   Description:    Function that determines if a value is of type dict.     #
##############################################################################
def isDict(value):
    if isinstance(value, dict):
        return True
    else:
        print("ERROR--Value is not of type: Dictionary!")
        return False


##############################################################################
#   Function:       dictPop()                                                #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop a dictionary off of the         #
#                   dictionary stack.                                        #
##############################################################################
def dictPop():
    if len(dictStack) >= 1:
        poppedDict = dictStack[-1]
        if isDict(poppedDict) is True:
            del dictStack[-1]
            return poppedDict
    else:
        print("ERROR--Insufficient stack size!")


##############################################################################
#   Function:       dictPush()                                               #
#   Parameters:     dictionary                                               #
#   Output:         none                                                     #
#   Description:    Function designed push a new dictionary on to the        #
##############################################################################
def dictPush(d):
    if isDict(d) is True:
        dictStack.append(d)


##############################################################################
#   Function:       define()                                                 #
#   Parameters:     name, value                                              #
#   Output:         none                                                     #
#   Description:    Function designed add a new name:value to the top        #
#                   dictionary in the dictStack.                             #
##############################################################################
def define(name, value):
    dictStack[-1][name] = value


##############################################################################
#   Function:       lookup()                                                 #
#   Parameters:     name                                                     #
#   Output:         value                                                    #
#   Description:    Function designed to look up the key, and return the     #
#                   value associated with that key in the dictionary stack.  #
##############################################################################
def lookup(name):
    for d in dictStack:
        for k in d:
            if k == name:
                return d[k]
    return print("ERROR--Key does not exist!")


# ------------------------- Arithmetic Operations -------------------------- #
##############################################################################
#   Function:       isNumber()                                               #
#   Parameters:     value                                                    #
#   Output:         boolean                                                  #
#   Description:    Function designed to check if a value is a number or not.#
##############################################################################
def isNumber(value):
    try:
        value += 1
        return True
    except TypeError:
        print("ERROR--Value is not a number!")
        return False


##############################################################################
#   Function:       add()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the top 2 values of the operand #
#                   stack, if they exist (and are integers), and perform an  #
#                   addition on them and push the new value back onto the    #
#                   stack.                                                   #
##############################################################################
def add():
    if len(opStack) >= 2:
        op1 = opPop()
        op2 = opPop()
    else:
        return print("ERROR--Insufficient stack size!")
    if isNumber(op1) and isNumber(op2) is True:
        sum = op1 + op2
        opPush(sum)


##############################################################################
#   Function:       sub()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the top 2 values of the operand #
#                   stack, if they exist (and are integers), and perform a   #
#                   subtraction on them and push the new value back onto the #
#                   stack.                                                   #
##############################################################################
def sub():
    if len(opStack) >= 2:
        op1 = opPop()
        op2 = opPop()
    else:
        return print("ERROR--Insufficient stack size!")
    if isNumber(op1) and isNumber(op2) is True:
        diff = op1 - op2
        opPush(diff)
    else:
        opPush(op1)
        opPush(op2)


##############################################################################
#   Function:       mul()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the top 2 values of the operand #
#                   stack, if they exist (and are integers), and perform a   #
#                   multiplication on them and push the new value back onto  #
#                   the stack.                                               #
##############################################################################
def mul():
    if len(opStack) >= 2:
        op1 = opPop()
        op2 = opPop()
    else:
        return print("ERROR--Insufficient stack size!")
    if isNumber(op1) and isNumber(op2) is True:
        prod = op1 * op2
        opPush(prod)


##############################################################################
#   Function:       div()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the top 2 values of the operand #
#                   stack, if they exist (and are integers), and perform a   #
#                   division on them and push the new value back onto the    #
#                   stack.                                                   #
##############################################################################
def div():
    if len(opStack) >= 2:
        op1 = opPop()
        op2 = opPop()
    else:
        return print("ERROR--Insufficient stack size!")
    if isNumber(op1) and isNumber(op2) is True:
        quot = op1 / op2
        opPush(quot)


##############################################################################
#   Function:       mod()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the top 2 values of the operand #
#                   stack, if they exist (and are integers), and return the  #
#                   remainder of the division and push that value on to the  #
#                   stack.                                                   #
##############################################################################
def mod():
    if len(opStack) >= 2:
        op1 = opPop()
        op2 = opPop()
    else:
        print("ERROR--Insufficient stack size!")
    if isNumber(op1) and isNumber(op2) is True:
        remainder = op1 % op2
        opPush(remainder)


# ---------------------------- Array Operations ---------------------------- #
##############################################################################
#   Function:       isArray()                                                #
#   Parameters:     value                                                    #
#   Output:         boolean                                                  #
#   Description:    Function designed to determine if a value is of type list#
##############################################################################
def isArray(value):
    if isinstance(value, list):
        return True
    else:
        print("ERROR--Value is not of type: Array!")
        return False


##############################################################################
#   Function:       length()                                                 #
#   Parameters:     item                                                     #
#   Output:         integer                                                  #
#   Description:    Function designed to return the length of an array in    #
#                   the stack at the specified index.                        #
##############################################################################
def length(item):
    if isArray(item) is True:
        return len(item)


##############################################################################
#   Function:       get()                                                    #
#   Parameters:     item                                                     #
#   Output:         item, or value                                           #
#   Description:    Function designed to get the item at specified index.    #
##############################################################################
def get(list, item):
    if isArray(list) is True:
        return list[item]
    else:
        print("ERROR--Value does not exist!")


# ------------------ Stack Manipulation & Print Operations ----------------- #
##############################################################################
#   Function:       dup()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to duplicate the last value in the     #
#                   stack, and pushes it onto the stack.                     #
##############################################################################
def dup():
    if isEmpty() is True:
        pass
    else:
        duplicate = opStack[-1]
        opPush(duplicate)


##############################################################################
#   Function:       exch()                                                   #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to swap the top two values in the stack#
##############################################################################
def exch():
    if len(opStack) >= 2:
        val1 = opPop()
        val2 = opPop()
        opPush(val1)
        opPush(val2)
    else:
        print("ERROR--Insufficient stack size!")


##############################################################################
#   Function:       pop()                                                    #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop off the last value in the stack.#
##############################################################################
def pop():
    if len(opStack) >= 1:
        del opStack[-1]
    else:
        print("ERROR--Insufficient stack size!")


def roll():
    pass


##############################################################################
#   Function:       copy()                                                   #
#   Parameters:     integer                                                  #
#   Output:         none                                                     #
#   Description:    Function designed to copy the top n values of the stack  #
#                   and push them onto the stack.                            #
##############################################################################
def copy(number):
    sizeOfStack = len(opStack)
    if number <= sizeOfStack:
        tempList = opStack[sizeOfStack - number:]
        for v in tempList:
            opPush(v)
    else:
        print("ERROR--Insufficient stack size!")


##############################################################################
#   Function:       clear()                                                  #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to clear the stack.                    #
##############################################################################
def clear():
    if isEmpty() is True:
        pass
    else:
        global opStack
        opStack = []


##############################################################################
#   Function:       stack()                                                  #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed print all of the contents of the stack.#
##############################################################################
def stack():
    if isEmpty() is True:
        pass
    else:
        for value in opStack:
            print(value)


# ------------------- Dictionary Manipulation Operations ------------------- #
##############################################################################
#   Function:       psDict()                                                 #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to create a new empty dictionary, and  #
#                   pushes that onto the dictionary stack.                   #
##############################################################################
def psDict():
    dictPush({})


def begin():
    pass


def end():
    pass


##############################################################################
#   Function:       psDef()                                                  #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to pop the last 2 values in the stack, #
#                   if they exist and are of the correct types. The first    #
#                   popped value is the value, and the second popped value is#
#                   the variable name. These values are converted to a       #
#                   dictionary and pushed on to the dictionary stack.        #
##############################################################################
def psDef():
    if len(opStack) >= 2:
        value = opPop()
        varName = opPop()
        if isString(varName) is True:
            varName = str(varName)
            if varName.startswith('/'):
                tempName = varName.replace('/', "")
                dictPush({tempName: value})
            else:
                opPush(varName)
                opPush(value)
                print("ERROR--Insufficient stack contents!")
        else:
            opPush(varName)
            opPush(value)
            print("ERROR--Insufficient stack contents!")
    else:
        print("ERROR--Insufficient stack contents!")


# ----------------------------- Test Functions ----------------------------- #
##############################################################################
#   Function:       testAdd()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the add() function to see if it#
#                   produces the correct answer.                             #
##############################################################################
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    else:
        return True


##############################################################################
#   Function:       testSub()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the sub() function to see if it#
#                   produces the correct answer.                             #
##############################################################################
def testSub():
    opPush(1)
    opPush(2)
    sub()
    if opPop() != 1:
        return False
    return True


##############################################################################
#   Function:       testMul()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the mul() function to see if it#
#                   produces the correct answer.                             #
##############################################################################
def testMul():
    opPush(2)
    opPush(3)
    mul()
    if opPop() != 6:
        return False
    else:
        return True


##############################################################################
#   Function:       testDiv()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the div() function to see if it#
#                   produces the correct answer.                             #
##############################################################################
def testDiv():
    opPush(2)
    opPush(3)
    div()
    if opPop() != 1.5:
        return False
    else:
        return True


##############################################################################
#   Function:       testMod()                                                #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the mod() function to see if it#
#                   produces the correct answer.                             #
##############################################################################
def testMod():
    opPush(3)
    opPush(10)
    mod()
    if opPop() != 1:
        return False
    else:
        return True


##############################################################################
#   Function:       testOpPop()                                              #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the opPop() function to see if #
#                   it produces the correct answer.                          #
##############################################################################
def testOpPop():
    opPush(2)
    opPush(3)
    opPop()
    if opStack != [2]:
        return False
    else:
        return True


##############################################################################
#   Function:       testOpPush()                                             #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the opPush() function to see if#
#                   it produces the correct answer.                          #
##############################################################################
def testOpPush():
    if isEmpty() is False:
        clear()
    opPush(2)
    opPush(3)
    if opStack != [2, 3]:
        return False
    else:
        return True


##############################################################################
#   Function:       testDictPop()                                            #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the DictPop() function to see  #
#                   if it produces the correct answer.                       #
##############################################################################
def testDictPop():
    global dictStack
    dictStack = []
    dictPush({1: 'a'})
    dictPush({2: 'b'})
    dictPop()
    if dictStack != [{1: 'a'}]:
        return False
    else:
        return True


##############################################################################
#   Function:       testDictPush()                                           #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the dictPush() function to see #
#                   if it produces the correct answer.                       #
##############################################################################
def testDictPush():
    global dictStack
    dictStack = []
    dictPush({1: 'a'})
    dictPush({2: 'b'})
    if dictStack != [{1: 'a'}, {2: 'b'}]:
        return False
    else:
        return True


##############################################################################
#   Function:       testDefine()                                             #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the define() function to see   #
#                   if it produces the correct answer.                       #
##############################################################################
def testDefine():
    global dictStack
    dictStack = []
    psDict()
    define(1, 'a')
    if dictStack != [{1: 'a'}]:
        return False
    else:
        return True


##############################################################################
#   Function:       testLookup()                                             #
#   Parameters:     none                                                     #
#   Output:         boolean                                                  #
#   Description:    Function designed to test the lookup() function to see   #
#                   if it produces the correct answer.                       #
##############################################################################
def testLookup():
    global dictStack
    dictStack = []
    dictPush({1: 'a'})
    value = lookup(1)
    if value != 'a':
        return False
    else:
        return True


# ------------------------------ Main Program ------------------------------ #
##############################################################################
#   Function:       testProgram()                                            #
#   Parameters:     none                                                     #
#   Output:         none                                                     #
#   Description:    Function designed to test all of the test cases in the   #
#                   program, and determines if they all return the correct   #
#                   values.                                                  #
##############################################################################
def testProgram():
    testCases = [('add', testAdd), ('sub', testSub), ('mul', testMul),
                 ('div', testDiv), ('mod', testMod), ('opPop', testOpPop),
                 ('opPush', testOpPush), ('dictPop', testDictPop),
                 ('dictPush', testDictPush), ('define', testDefine),
                 ('lookup', testLookup)]
    failedTests = [testName for (testName, testProc) in
                   testCases if not testProc()]
    if failedTests:
        return print('Some tests failed...', failedTests)
    else:
        return print('All tests passed!!!')


# Call the function to test if all the functions are running correctly
testProgram()

# End Program
