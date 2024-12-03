import pickle
import pandas as pd

print("============ Input ==========")
mail=input("Enter the mail body: ")

mail=pd.Series(mail)

with open('feature_extraction.pkl', 'rb') as file:
    feature_extraction=pickle.load(file)

with open('logistic_regression.pkl', 'rb') as file:
    logistic_regression=pickle.load(file)

mail_feature=feature_extraction.transform(mail)

prediction=logistic_regression.predict(mail_feature)

print("============ Result ==========")

print("Your mail is a ",end='')
if(prediction[0]==1):
    print("Spam")
else:
    print("Ham")