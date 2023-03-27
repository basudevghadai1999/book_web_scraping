import requests
from bs4 import BeautifulSoup


def recommend_books(title):
    #name ='abc'
    url = f'https://www.goodreads.com/search?q={title}'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    #whole_div = soup.find_all('div', class_='leftContainer')

    book_info = soup.find_all('table',{'class':'tableList'})
    book_url = soup.find_all('a',{'class':'bookTitle'})#.get('href')
    
    whole_list=[]
    book_name_list=[]
    author_name_list=[]
    rating_list=[]
    image_list=[]
    try:

        for item in book_url:
            book_name = item.text
            book_name_list.append(book_name)
            #print('bookname',item.text)

            #url = item.get('href')


        author = soup.findAll("a",{'class':'authorName'})
        for items in author:
            author_name = items.text
            author_name_list.append(author_name)
            #print('author',items.text)
            
        #print(author)

        rating = soup.findAll("span",{'class':'minirating'})

        for rate in rating:
            rating_of_books = rate.text
            rating_list.append(rating_of_books)
            # print('rating',rate.text)

        imgs = soup.findAll("img",{'class':'bookCover'})
        for item2 in imgs:
            book_image = item2.get('src')
            image_list.append(book_image)

        # print('iamge',item2.get('src'))
        # print(book_name_list)
        # print(rating_list)
        # print(author_name_list)
        # print(image_list)


        #print(url)
        for i in range(len(book_name_list)):

            dic1={
                'book name': book_name_list[i],
                'author name': author_name_list[i],
                'rating':rating_list[i],
                'book image':image_list[i] 
            }
            whole_list.append(dic1)

            #print(image_list[i])
        print(whole_list)
    except:
        print('error occured')
    #return book_url

# Example usage
input_value = input("Enter the text here!!!")
recommended_books = recommend_books(input_value)

#print(recommended_books)