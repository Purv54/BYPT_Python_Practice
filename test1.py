st = "print only those words that start with s in this sentence"

for word in st.split():
    if word.startswith("s"):
        print(word)