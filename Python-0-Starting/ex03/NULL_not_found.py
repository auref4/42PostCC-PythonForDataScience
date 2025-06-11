def NULL_not_found(object: any) -> int:
    if object == None:
        print("Nothing :", object, type(object))
    elif type(object) == float and object != object:
        print("Cheese :", object, type(object))
    elif type(object) == int and object == 0:
        print("Zero :", object, type(object))
    elif type(object) == str and object == '':
        print("Empty :", object, type(object))
    elif type(object) == bool and object == False:
        print("Fake :", object, type(object))
    else:
        print("Type not found")
        return 1
    return 0
