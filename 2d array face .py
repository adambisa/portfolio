
from typing import List

def is_face_on_photo(photo: List[List[str]]) -> bool:

    def find_all(matrix, element):  
        yield from ((row_no, col_no)   
        for row_no, row in enumerate(matrix)  
        for col_no, matrix_element in enumerate(row)  
        if matrix_element == element) 

         
    search= ['f', 'a', 'c', 'e']
    if len(photo) < 2:
        return False



    for i in search:
        if not any(i in x for x in photo):
            return False


    i=0
    for i in range(len(search)):
        for x,y in find_all(photo, search[i]): 
            vzdialenost=abs(x-y)
            if vzdialenost >=0 and vzdialenost <= 1:
                return True
        


# Veřejné testy:
print(is_face_on_photo([['f', 'a'], ['c', 'e']]))  # True
print(is_face_on_photo([['f', 'a', 'c', 'e']]))  # False
print(is_face_on_photo([['e', 'c', 'x'], ['a', 'f', 'x'], ['x', 'x', 'x']]))  # True
print(is_face_on_photo([['f', 'f', 'x'], ['a', 'a', 'x'], ['x', 'x', 'x']]))  # False
