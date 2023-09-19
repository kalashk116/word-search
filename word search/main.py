import webbrowser
word=input("Enter what you want to search: ")
query = "https://www.google.com/search?q=" + word
webbrowser.open_new_tab(query)


