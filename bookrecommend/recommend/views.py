from django.shortcuts import render
from django.http import HttpResponse

import pickle
import numpy as np

from matplotlib.style import context

popular_df=pickle.load(open('model/popular.pkl','rb'))
book=pickle.load(open('model/book.pkl','rb'))
similarity_score=pickle.load(open('model/similarity_score.pkl','rb'))
pt=pickle.load(open('model/pt.pkl','rb'))





book_name=list(popular_df['Book-Title'].values)
author=list(popular_df['Book-Author'].values)
image=list(popular_df['Image-URL-M'].values)
vote=list(popular_df['num-rating'].values)
avg_rating=list(popular_df['avg-rating'].values)

mylist = zip(image,book_name,author,vote)
context = {
            'mylist': mylist,
        }

# Create your views here.

def home(request):
   return render(request,'recommend/index.html',context)


def recommend(request):
   return render(request,'recommend/input.html')


def recommend_books(request):
     if request.method == 'POST':
       val=request.POST['bookname']
       print(val)
       index=np.where(pt.index==val)[0][0]
       print(index)
       similar_item=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
       distance=similarity_score[index]
       
       data=[]
       for i in similar_item:
           item=[]
           tempdf=book[book['Book-Title']==pt.index[i[0]]]
           item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Title'].values))
           item.extend(list(tempdf.drop_duplicates('Book-Title')['Book-Author'].values))
           item.extend(list(tempdf.drop_duplicates('Book-Title')['Image-URL-M'].values))
           #print(i)
           #data.append(item)
           data.append(item)
       print(data)

    
     return render(request,'recommend/input.html',{'data':data})
