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


    #funcion que publica los libros
    def Issue_books(self):
        books_id = input('Enter books ID: ')
        #fecha actualizada
        current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        #verificamos si el ID existe o no en la BD
        if books_id in self.books_dict.keys():
            if not self.books_dict[books_id]['Status'] == 'Available':
                print(f"This books is already issued to {self.books_dict[books_id]['lender_name']} \
                    on {self.books_dict[books_id]['Issue_data']}")
                return self.Issue_books()
            elif self.books_dict[books_id]['Status'] == 'Available':
                your_name = input('Enter your name: ')
                self.books_dict[books_id]['lender_name'] == your_name
                self.books_dict[books_id]['Issue_date'] == current_date

                #cambiar el estado del libro
                self.books_dict[books_id]['Status'] == "Already Issued"
                print('Books issued succesfully! \n')
        else:
            print('Book ID not found')
            return self.Issue_books()

            
    #Funcion agregar un libro
    def add_books(self):

        new_books = input('Enter books title: ')
        # si la entrada es vacia
        if new_books == "":
            return self.add_books()
        # Si el titulo es mayor de 25 caracteres
        elif len(new_books) > 25:
            print('Books title length is too long! Title length should be 20 chars')
            return self.add_books()
        else:
            # abrir el archivo txt y guardar el nuevo libro
            with open(self.list_of_books, 'a') as bk:
                bk.writelines(f"{new_books}\n")

                # actualizar el ID del nuevo libro
                self.books_dict.update({str(int(max(self.books_dict)) + 1):{'books_title':new_books,
                'lender_name':'',
                'Issue_data':'',
                'Status':'Available'}})
                print(f"This books '{new_books}' has been added successfull!")



l = LMS("List_of_books.txt", "Python's Library")
print(l.display_books())
#print(LMS("List_of_books.txt", "Python's library"))

