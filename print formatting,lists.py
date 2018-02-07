# String.format method(to insert variables)
 Used to call a variable multiple times,at different places..
 ex: print("this first: {x}, and second: {y} and third: {x}" .format(x="inserted",y="roundabout"))

# insert variable
x="hello"
print("I'll insert hello here: %s"%(x))

# Lists

- Sequence of variables
- These are mutable unlike strings.
- Lists are constructed with brackets [] and commas separating every element in the list.
  ex: my_list = ['A string',23,100.232,'o']
     Just like strings, the len() function will tell you how many items are in the sequence of the list.
     len(my_list)

## Indexing and Slicing lists
### Indexing:
We can grab stuff using this..ex: my_list[0]
##Grab index 1 and everything past it
  my_list[1:]

##grab everything upto index 3,but not it
my_list[:3]

###concatinate,but it wont reassign
my_list+["hello"]

###to reassign
my_list=my_list+["add permanently"]

##doubling list
my_list*2 ['one',
 'two',
 'three',
 4,
 5,
 'add new item permanently',
 'one',
 'two',
 'three',
 4,
 5,
 'add new item permanently']
 
 # Methods for lists
 
 ##append
 ex: l=[1,2,3]
 item to add to the end of the list, l.append('append me')
 
 ##pop
 l.pop()
 removes last item in the list
 
 ###pop off certain element with its index;
 x=l.pop(0), x has 1, l has 2,3 now
 
 
