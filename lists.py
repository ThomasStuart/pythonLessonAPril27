# Lists.
# 	- list of lists is ok

#TODO:: COME BACK AFTER FOR LOOPS
row = [ 'X', 'X' , 'X']
GameBoard  = [ row, row, row  ]

# for r in GameBoard:
#     for c in r:
#         print( c , end='')
#     print()
#

# 	- duplicate elements are ok

# 	- colons and lists

# 	- colons and lists
        # 0 , 1 , 2  ,3  , 4,  5 ,   6    ,7
array =  [1,   2, 3,  4,  5,   6,   7,   8]

#        list[ startIndex : endIndex ]
#               ^inclusive  ^exclusive
print( array[1:5] ) #  [2, 3,  4,  5,   6]

# question, print all the elements after index 4 ?
print( array[4:] )

# question, print all the elements before index 4 ?
print( array[:4] )



# 	- deleting and appending elements
CHARS = ['A', 'B', 'C', 'D']

# add <- E, F
CHARS.append('E')
CHARS.append('F')

print(CHARS)

#
CHARS = ['A', 'B', 'C', 'D']
CHARS.clear()
print(CHARS)


# how would i remove the value 'B' from list Chars and store it in the variable removed
CHARS = ['A', 'B', 'C', 'D']
removed = CHARS.pop(1)
print( removed ) # B

# I wanted to delete/remove B all together
CHARS = ['A', 'B', 'C', 'D']
del CHARS[1]
print( CHARS )


numbers = [  1, 3, 4, 1,  8, 9 , 1]
# remove all the ones from the list numbers
numbers.remove(1)
print( numbers)


# 	- contains functions
names = ["Tom" , "Bob" , "Adam"]

if "Tom" in names:
    print( "True")
else:
    print("False")


# write a function called doesContainName that checks if a provided name is in the list
# returns a true if the name is in the list
# False if not
def doesContainName( name, List ):
    if name in List:
        return True
    else:
        return False



print(  doesContainName( "Tom", ["Tom" , "Bob" , "Adam"] )  )
print(  doesContainName( "Kim", ["Tom" , "Bob" , "Adam"] )   )


# 	- what is a tuples
#TODO:: DID NOT GO OVER