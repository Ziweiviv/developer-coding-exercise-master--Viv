# Feel free to move this to a new file if you are carrying out the 'tags' calculation there
import os
from django.shortcuts import get_object_or_404, render
from markdown import markdown
from collections import Counter

 
stopWords = [
    "#", "##", "a", "about", "above", "after", "again", "against", "all", "am",
    "an", "and", "any", "are", "aren't", "as", "at", "be", "because", "been",
    "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
    "could", "couldn't", "did", "didn't", "do", "does", "doesn't", "doing", "don't",
    "down", "during", "each", "few", "for", "from", "further", "had", "hadn't",
    "has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's",
    "her", "here", "here's", "hers", "herself", "him", "himself", "his", "how",
    "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
    "it", "it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my",
    "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or", "other",
    "ought", "our", "ours", "ourselves", "out", "over", "own", "same", "shan't", "she",
    "she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that",
    "that's", "the", "their", "theirs", "them", "themselves", "then", "there", "there's",
    "these", "they", "they'd", "they'll", "they're", "they've", "this", "those", "through",
    "to", "too", "under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll",
    "we're", "we've", "were", "weren't", "what", "what's", "when", "when's", "where",
    "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with", "won't",
    "would", "wouldn't", "you", "you'd", "you'll", "you're", "you've", "your", "yours",
    "yourself", "yourselves"  
] 


        

# os.path.join(path, i)
path='./assets/posts'
title={}






def post(request, slug):
    # open the selected file and retrieve data
    i=request.GET.get('i')
    if i in os.listdir(path):
       with open(path+'/'+i, 'r',encoding='utf-8') as file:
        h = file.read()
        description = bytes(h, 'utf-8')
        title=description.decode("utf-8").split("===")[1].split("\n")[1].split(":")[1]
        author=description.decode("utf-8").split("===")[1].split("\n")[2].split(":")[1]
        c=description.decode("utf-8").split("===")
        info={}
        info[title,markdown(description.decode("utf-8")).split("===")[-1],author]= author
        k=Counter([value for value in c[-1].split() if value.lower() not in stopWords and value.isalpha()]).most_common(5)
        tags={}
        for tag in k:
            tags[tag[0]] = [tag[1]]
    return render( request,'post.html',locals())


def posts(request):
    # using file name to show all posts
   
    title={}
    path='./assets/posts'
    for i in os.listdir(path):
       with open(path+'/'+i, 'r',encoding='utf-8') as file:
        h = file.read()
        description = bytes(h, 'utf-8')
        c=description.decode("utf-8").split("===")[1].split("\n")[1].split(":")[1]
        
        title[c,i]= i
    return render( request,'posts.html', locals())
    





    







