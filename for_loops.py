# Lists.
# 	- how to iterate through a list  w/out range
# 	- how to iterate through a list  with  range
# 	- how to add a counter to a list
# 	- how to change the increment amount of a for loop
# 	- hwo to change to a decrementer
# 	- indexing with a list

fruits = ['banana', 'apple',  'mango']

# element @ 0 == banana    iteration 0
# element @ 1 == apple     iteration 1
# element @ 2 == mango     iteration 2  ...

idex_num = 0
# for element in fruits:  # go through the entire list
#     print( "element @ " ,idex_num, "==", element )
#     idex_num += 1

# for whatever in fruits:  # go through the entire list
#     print( "element @ " ,idex_num, "==", whatever )
#     idex_num += 1  # <--this line increases the number by 1 each iteartion
#

#  say i didnt want to print the first elemet
# for index in range(1, len(fruits) ):
#     print( fruits[index] )

#list_apple  = ['a', 'p', 'p', 'l', 'e']
word = "apple"

# print apple character by character starting at a
# for character in word:
#     print(character)

# print apple character by character starting at e

word = "apple"  # 5 characters in the word apple
len_apple = len( word )


#       0   1   2   3     4
# word = "a   p   p   l    e"
#
#                     # start = 4  ,end = -1 , go down by one
# for index  in  range( len(word)-1,      -1,       -1 ):
#     print( word[index] )


# my_name = "thomas"
# startNumber  = 0
# endNumber    = len( my_name)
# howMuchIncrease = 1
# for number in range(startNumber, endNumber, howMuchIncrease):
#     print( my_name[number] , end='')


even_word = "acefdb"

# even_word = "cefd"
# even_word = "ef"
# even_word = ""

# END GOAL:
# "front==", a "... end==",  b          # iteration 0
# "front==", c "... end==",  d          # iteration 1
# "front==", e "... end==",  f          # iteration 2


#hint use a for loop and a counter
counter = len(even_word)-1

start_index = 0
end_index   = len(even_word)

# the for loop ran a total of 6 times
# but we want the for loop to run a total of 3 times


for index in range(start_index, int( end_index/2)  ):
    print( "front==", even_word[index] ,"  ", end='')
    print( "end==", even_word[counter])
    counter = counter - 1


#hint:
# counter = 5
# print( "what is the current value of counter== ", counter )
# # decrease counter by one
# counter = counter - 1
# print( "what is the current value of counter== ", counter )


p1 = "racecar"
print( p1 )
