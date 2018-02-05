#Strings

Strings are used in Python to record text information, such as name. 
Strings in Python are actually a sequence, which basically means Python keeps track of every element in the string as a sequence.
For example, Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

-Create strings using '' or ""

-print() syntax to print strings.. Python 2 doesn't have (), to import this  we should use from __future__ import print_function

-\n for new line and \t for tab

-To check Length of a string.. len('hello world').. it also counts space as a count.

-Assigning a label and creating a variable;
      s="Hello world"
      print (s)..it prints "hello world"

*Index: 
        s[0]= H
        s[1]= e

*Slicing:
  Grabbing everything upto the designated point and syntax is :
  s[1:] -> for s object, grab everything from the index 1 and : means onwards.. it gives ello world
  s[:3] -> grab everything upto the index 3,but not the index 3 letter.
  s[-1] -> Negative index means after 0, the first letter, negative index means letters from backwards.this is last element in the string// d
  s[:-1]-> Grab everything except last letter
  s[::1] ->Grab everything everything with a step size one..it prints everything
  s[::2]->Grab every other letter 
  s[:] -> grab everything
  ##s[::-1]-> to print the string backwards... grab from the beginning of everything to the end off everything but the step size is backwards.. so the string will be reversed.
  Ex: s="hello world"
            
            s[:2] -> 'he'  s[2:] -> 'llo'
            
            
  *Properties:
  ##Immutability: Elements in it cant be changed or replaced.
  we declared s="Hello world" so we cant change s[0]=z..it gives error..
  ##we can concatinate..it means add to the string.. ex: s + "concatinating this"
  ##Reassign: concatination reassigns variable.
  ##Multiplying string: letter="z" 
              letter * 10 gives "zzzzzzzzzz"
  
  #Built-in string methods:
  Objects in pyton has built in methods.. these are functions insiede objects.They allow us to perform actions or commands on the objects itself.
  ##Syntax for methods on objects :
  is whatever the object label name is.method ex: s='hello' (s is an object(string))  and method.. s.upper() to convert to uppercase. Another ex: s.split('e') gives 'h' and 'llo'  (##Clicking tab shows all methods list in jupyter)
  
