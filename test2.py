#!/usr/bin/python

# list
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
print list
list[2]=1000
print list

# tuple
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
print tuple

#dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
print dict
dict['one'] = "This is one modified"
print dict
print dict.keys()
print dict.values()

#end
raw_input("\nPress the enter key to exit.")
