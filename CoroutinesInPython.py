def Searcher():
    queote = "The Mind Is Everything, What You Think You Become"
    import time
    time.sleep(2)

    while True:
        text=(yield)
        if text in queote:
            print("Text Found In Queote")
        else:
            print("Text Not Found In Queote")

search=Searcher()
print("Search Started")
next(search)
j=input("Enter Any Word Of Search : ")
search.send(j)
search.close()
