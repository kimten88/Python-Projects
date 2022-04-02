import webbrowser

f = open("webpage.html", "w")
f.write("""<html>

<body>

<h1>

Stay tuned for our amazing summer sale!

</h1>

</body>

</html>""")
f.close()

#open and read the file after the appending:
##f = open("webpage.html", "r")
##print(f.read())

url = 'file:///C:/Users/Kimte/OneDrive/Documents/GitHub/Python-Projects/webpage.html'

webbrowser.open_new_tab(url)
