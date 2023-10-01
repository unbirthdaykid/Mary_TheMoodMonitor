import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

primary = pd.read_csv("Stress.csv")
df_main = primary[["subreddit", "text"]].copy()

new_column = []

for i in range(len(primary)):
    extracted_strings = primary["text"].tolist()[i].lower().strip().split()
    extracted_strings_cleaned = ""
    for word in extracted_strings:
        word_cleaned = word.replace(".", "").replace(",", "").replace("?", "").replace("!", "").replace("(", "").replace(")", "").replace("<", "").replace(">", "").replace("*", "").replace("_", "").replace("[", "").replace("]", "")
        if  word_cleaned != "":
            extracted_strings_cleaned = word_cleaned + " " + extracted_strings_cleaned
    
    new_column.append(extracted_strings_cleaned)
    


#corpus = []

#for i in range(len(new_column)):
    #for j in range(len(new_column[i])):
        #if new_column[i][j] not in corpus:
            #corpus.append(new_column[i][j])
            

    
df_main["parsed_words"] = new_column
df_main.drop(["text"], axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(df_main["parsed_words"], df_main["subreddit"], test_size = 0.25)

v = CountVectorizer()

X_train_count = v.fit_transform(X_train)


model = MultinomialNB()
model.fit(X_train_count, Y_train)

X_test_count = v.transform(X_test)
#print(model.score(X_test_count, Y_test))


def user_input(sentence):
    new_x = [sentence]
    new_x_vectorized = v.transform(new_x)
    predict = model.predict(new_x_vectorized)
    print(predict)


    #model.predict(count)


#model = gensim.models.Word2Vec(window=5, min_count=2, workers=4, sg=0)
#model.build_vocab(new_column, progress_per=1000)
#model.train(new_column, total_examples=model.corpus_count, epochs=model.epochs)

#model.save("./posts.model")

