# libraries
import datetime
import os

# os.getcwd() #muestra la carpeta donde se encuentra el archivo

class LMS:
    """this class is used to keep record of book library
    It has total four module: - Display books
                              - Issue books
                              - Return books
                              - Add books"""
    def __init__(self, list_of_books, library_name):
        self.list_of_books = 'List_of_books.txt'
        self.library_name = library_name
        self.books_dict = {}  #contiene toda la informacion de cada libro
        Id = 101  #identificador

        #leemos el archivo txt
        with open(self.list_of_books) as bk:
            content = bk.readlines()  #almacena las lineas del archivo

        for line in content:
            #actualizamos la informacion de cada libro en su respectivo diccionario
            self.books_dict.update({str(Id):{'books_title':line.replace('\n',''),
            'lender_name':'', 
            'Issue_data':'',
            'Status':'Available'}})
            Id += 1

    
    #funcion que muestra la informacion de cada libro
    def display_books(self):
        print("-----------List of Books--------------")
        print('Books ID', "\t", "Title", )
        print("--------------------------------------")

        #bucle que muestra las llave-valor de los diccionarios
        for key, value in self.books_dict.items():
            print(key,"\t\t",value.get('books_title'), "- [",value.get('Status'),"]")


l = LMS("List_of_books.txt", "Python's Library")
print(l.display_books())
#print(LMS("List_of_books.txt", "Python's library"))

