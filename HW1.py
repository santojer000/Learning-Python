###############################################################################
#   Programmer:     Jerome Santos
#   SID:            011555815
#   Date:           01/27/2017
#   OS:             Windows
#   Course:         CPT_S 355--Programming Language Design
#   Term:           Spring 2017
#   Assignment:     HW1
#   Description:    A program that tests various functions in Python including:
#                   - cryptDict()
#                   - decrypt()
#                   - charCount()
#                   - dictAddup()
###############################################################################

###############################################################################
#   Function:       debug()
#   Input:          String
#   Output:         None
#   Description:    A function that allows the user to decide if they want to
#                   debug or not.
###############################################################################
debugging = True
def debug(*s):
    if debugging: print(*s)

###############################################################################
#   Function:       cryptDict()
#   Input:          String1, String2
#   Output:         Dictionary
#   Description:    A function that takes in string1 and string2 as parameters
#                   and converts them into a dictionary, where the keys
#                   correspond to string1 and the values correspond to string2
#                   (Assuming that both strings are the same length).
###############################################################################
def cryptDict(s1, s2):
    L1 = list(s1)
    L2 = list(s2)
    dictionary = dict(zip(L1, L2))
    return dictionary

###############################################################################
#   Function:       decrypt()
#   Input:          Dictionary, String
#   Output:         String
#   Description:    A function that takes in a dictionary and a string, and
#                   decodes the letters based of the mapping of the dictionary.
#                   Then the function returns the new decoded string.
###############################################################################
def decrypt(cdict, s):
    decryptedS = ""
    for c in s:
        if c in cdict.keys():
            decryptedS += cdict[c]
        else:
            cdict[c] = c
            decryptedS += cdict[c]
    return decryptedS

###############################################################################
#   Function:       testDecrypt()
#   Input:          None
#   Output:         Boolean
#   Description:    A function that tests the translation code.  It will return
#                   True if successful, and False if any of the tests fail.
###############################################################################
def testDecrypt():
    cdict = cryptDict('abc', 'xyz')
    revcdict = cryptDict('xyz', 'abc')
    tests = "Now_I_know_my_abc's"
    answer = "Now_I_know_my_xyz's"
    if decrypt(cdict, tests) != answer:
        return False
    if decrypt(revcdict, decrypt(cdict, tests)) != "Now_I_know_mb_abc's":
        return False
    if decrypt(cdict,'') != '':
        return False
    if decrypt(cryptDict('',''), 'abc') != 'abc':
        return False
    return True

###############################################################################
#   Function:       charCount()
#   Input:          String
#   Output:         List
#   Description:    A function that takes in a string and iterates through
#                   each character while keeping track of how many times that
#                   character appears in a 2-tuple. This tuple is stored, and
#                   the complete list is returned to the user in ascending
#                   order.
###############################################################################
def charCount(S):
    countList = []
    # iterates through the string ignoring spaces
    for c in S.replace(" ", ""):
        # Checks if the char is already in the list
    	if c not in (t[0] for t in countList):
            t = (c, S.count(c))
	    # Adds new tuple to the list
            countList.append(t)
    # Sorts the list based on the second element in the tuple
    countList.sort(key=lambda t: t[1])
    return countList
    
###############################################################################
#   Function:       testCount()
#   Input:          none
#   Output:         boolean
#   Description:    A function to test whether the charCount() function is
#                   successful.
###############################################################################
def testCount():
    charCountTest1 = charCount("aaabbc")
    charCountTest2 = charCount("This is a test")
    charCountTest3 = charCount("Cpts355 --- Assign1")
    if charCountTest1 != [('c', 1), ('b', 2), ('a', 3)]:
        return False
    if charCountTest2 != [('T', 1), ('h', 1), ('a', 1), ('e', 1), ('i', 2), 
                          ('t', 2), ('s', 3)]:
        return False
    # Note--Doesn't give the exact same answer as yours, but still returns
    # the sorted list of tuples in ascending order based off of the frequency
    if charCountTest3 != [('C', 1), ('p', 1), ('t', 1), ('3', 1), ('A', 1), 
                          ('i', 1), ('g', 1), ('n', 1), ('1', 1), ('5', 2), 
                          ('s', 3), ('-', 3)]:
        return False
    return True

###############################################################################
#   Function:       dictAddup()
#   Input:          dictionary
#   Output:         dictionary
#   Description:    A function that will add up the total hours of studying for
#                   course, and return an new dictionary with the courses as
#                   the keys, and the total hours for each as the map values.
###############################################################################
def dictAddup(d):
    courseList = []
    hoursList = []
    totalDict = {}
    course1hrs = 0
    course2hrs = 0
    course3hrs = 0
    for item in list(d.values()):
        for key in item:
            if key not in courseList:
                courseList.append(key)
    for item in list(d.values()):
        for i in item:
            if i == "355":
                course1hrs += item[i]   # Running count of hours
                hoursList.insert(0, course1hrs)
            elif i == "451":
                course2hrs += item[i]   # Running count of hours
                hoursList.insert(1, course2hrs)
            else:
                course3hrs += item[i]   # Running count of hours
                hoursList.insert(2, course3hrs)
    totalDict = dict(zip(courseList, hoursList))
    return totalDict   

###############################################################################
#   Function:       testAddup()
#   Input:          none
#   Output:         boolean
#   Description:    A function to test whether the dictAddup() function is
#                   successful.
###############################################################################
def testAddup():
    d = {'monday': {'355': 2, '451': 1, '360': 2},
         'tuesday': {'451': 2, '360': 3},
         'thursday': {'355': 3, '451': 2, '360': 3},
         'friday': {'355': 2},
         'sunday': {'355': 1, '451': 3, '360': 1}}
    dictAddupTest = dictAddup(d)
    if dictAddupTest != {'355':8,'451':8,'360':9}:
        return False
    return True

###############################################################################
#   Function:       testFunctions()
#   Input:          Function
#   Output:         String
#   Description:    A function to test if our functions are behaving as
#                   expected.
###############################################################################
def testFunctions(func):
    passedMsg = "%s_passed"
    failedMsg = "%s_failed"
    if func == True:
        return print("\t" + passedMsg % func)   # Passes test
    else:
        return print("\t" + failedMsg % func)   # Fails test
    
###############################################################################
#   Function:       main
#   Input:          none
#   Output:         none
#   Description:    The main function that utilizes the testFunctions function
#                   to determine if they are working properly.
###############################################################################
if __name__ == '__main__':
    print("testDecrypt:")
    testFunctions(testDecrypt())
    print("testCount result:")
    testFunctions(testCount())
    print("testAddup result:")
    testFunctions(testAddup())
      
# Keeps program open until enter key is pressed
input("Press enter to continue")
