# Sorting Functions

def sortList(list, order):
    """
    Sorts a list.
    Parameters:
    list: str/int[]
     List of values
    order:  str 
     can be values "asc", "desc" or "none" to returning ascending, descending on list again
     if no corresponding parameter, returns error message
    """
    
    if(order.lower() == 'asc'):
        print("ascended")
        return list.sort()
    
    if(order.lower() == 'desc'):
        print("descended")
        return list.sort(reverse=True)

    if(order.lower() != 'none'):
        print("ERROR: Please inform if list should be ascended, descending or 'none'")
    else:
        print("neither")
        return list
    
# listValues =  [5,6,4,9,1]
# sortList(listValues, 'asC')
# print(listValues)