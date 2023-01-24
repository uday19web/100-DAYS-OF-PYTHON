import pandas

word_data = pandas.read_csv("./data/french_words.csv")
print(type(word_data))
df = pandas.DataFrame.to_dict(word_data, orient="records")
print(df)
