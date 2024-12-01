def finder(author_name):  # Это поисковик. После того как в консоли вывелось все остальное,
    for book_i in books:  # нужно ввести имя автора и он выведет его книги
        if book_i[2].lower() == author_name.lower():
            if int(book_i[6]) < 200:
                return ' '.join(book_i)


with open('books-en.csv') as f:
    file = f.readlines()
    semi_ready_list = [file[i][:-1] for i in range(len(file))][1:]
    books = []
    cnt_long_names = 0
    authors = set()

    for i in semi_ready_list:  # Тут составляю множество издателей и число книг по длинному названию
        if '&amp;' in i:
            i = i.replace('&amp;', '&')
        book = i.split(';')
        authors.add(book[-3] + '\n')
        if len(book[1]) > 30:
            cnt_long_names += 1
        books.append(book)

    downloadings = []  # Здесь создал словарь по парам Название - Загрузки,
    names = []  # потом в принте указывается кол-во самых популярных книг
    for each_book in books:
        downloadings.append(int(each_book[-2]))
        names.append(f'{each_book[1]}. {each_book[2]}')
    books_dictionary = dict(zip(names, downloadings))
    the_most_popular_books = sorted(books_dictionary.items(), key=lambda item: item[1], reverse=True)
    
    biblio = open('bibliographic_list.txt', 'w')  # Здесь формирование библиографического списка
    for i in range(20):
        book = books[i]
        biblio.write(str(i + 1) + ". ")
        biblio.write(f'{book[2]}. {book[1]} - {book[3]}' + '\n')
    biblio.close()
    print(cnt_long_names)
    print(*authors)
    for i in range(0, 20):
        print(*(the_most_popular_books[i]))
    print(finder(input()))
