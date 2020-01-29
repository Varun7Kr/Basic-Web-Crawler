fw= open("sample.txt", "w")
fw.write("This is sample text\n")
fw.write("The second line")
fw.close()

fr=open("sample.txt","r")
text=fr.read()
print(text)
fr.close()