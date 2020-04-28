# List1 = [1,2,3,4] , indexNumber = 50  -> False
# List2 = [1,2 ]    ,  indexNumber = 1  -> True
# List1 = [1,2,3,4]  , indexNumber = 2  -> True


def isValidIndex( List, indexNumber ):

    if( indexNumber  >=  0  and  indexNumber  < len( List )   ):
        return True
    else:
        return False


# print( isValidIndex( [1,2]    , 1)  )
# print( isValidIndex( [1,2,3,4], 2)  )  # 0,1,2,3
# print( isValidIndex( [1,2,3,4], -1) )  # 0,1,2,3
#




def isEven( num ):
    if num % 2 == 0:
        return True
    else:
        return False

# print( isEven(4)  )
# print( isEven(5)  )




def getId( name, company="robolink"):
    print("Hello", name, " from ", company)


getId("thomas")
getId("Rom", "Google")
getId("Sam", "Apple")