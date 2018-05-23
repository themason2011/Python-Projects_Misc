import pytest

def count_au(s):

  '''
  Counts the number of "a"s and "u"s in a string, both capitalized and lowercase.
  '''

    if type(s) != str:
        return 0

    count = 0

    for item in s:
        
        if item == 'a' or item == 'A' or item == 'u' or item == 'U':
            count += 1

    return count

    
def test_count_au_0():
  assert(count_au(42)==0)

def test_count_au_1():
  assert(count_au('mai')==1)

def test_count_au_2():
  assert(count_au('MAYA')==2)

def test_count_au_3():
  assert(count_au('maui')==2)

def test_count_au_4():
  assert(count_au('moana')==2)

def test_count_au_5():
  assert(count_au('Auckland')==3)

def test_count_au_6():
  assert(count_au('Meeseeks')==0)
