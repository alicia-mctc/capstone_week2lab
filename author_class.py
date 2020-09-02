class Author:

    try:

        def __init__ (self, name):
            self.name = name
            self.books = []#empty list is created to hold books

        def publish(self, title):
            self.books.append(title)#append () method adds title to book list

        def __str__(self):
            title = ', '.join(self.books) or 'No published books'
            return f'{self.name}. Books: {title}'

    except Exception as e:
        print("Books with same names could not be published")    

def main():
      
        austen = Author('Jane Austen')
        austen.publish('Pride and Prejudice')
        austen.publish('Sense and Sensibility')
        print("Author:", austen)    

        

main()             

 



