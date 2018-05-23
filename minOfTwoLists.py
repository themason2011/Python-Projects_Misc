import pytest

def minOfTwoLists(alist, blist):  

  '''
  Creates a list with each element being the smallest element at each index, comparing elements in alist and blist. 
  If both elements are the same size in alist and blist, the element from alist is chosen.
  '''

    if type(alist) != list or type(blist) != list:
        return False

    if len(alist) != len(blist):
        return False

    for item in alist:
        if type(item) != str:
            return False

    for item in blist:
        if type(item) != str:
            return False

    combList = alist

    for i in range(len(blist)):
        if len(blist[i]) < len(combList[i]):
            combList[i] = blist[i]

    return combList
    

def test_minOfTwoLists_0():
  assert(minOfTwoLists(42, [1])==False)

def test_minOfTwoLists_1():
  assert(minOfTwoLists(['ox'],['cat'])==['ox'])

def test_minOfTwoLists_2():
  assert(minOfTwoLists(['ox','bear'],['cat', 'cow'])==['ox', 'cow'])

def test_minOfTwoLists_3():
  assert(minOfTwoLists(['bear','cow'],['ox','cat'])==['ox', 'cow'])

def test_minOfTwoLists_4():
  assert(minOfTwoLists(['bear','cow','crow','sparrow'],\
                       ['ox','cat','mouse','ox'])==\
                       ['ox', 'cow','crow','ox'])
  
def test_minOfTwoLists_5():
  assert(minOfTwoLists(['bear','cow','crow'],['ox','cat','mouse'])==\
['ox', 'cow','crow'])

def test_minOfTwoLists_6():
  assert(minOfTwoLists(['ox'],42)==False)

def test_minOfTwoLists_7():
  assert(minOfTwoLists(42,['ox'])==False)

def test_minOfTwoLists_8():
  assert(minOfTwoLists(['ox', 'fox'],['ox',17])==False)

def test_minOfTwoLists_9():
  assert(minOfTwoLists(['cow','bear'],['ox'])==False)
