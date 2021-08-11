from transformers import DistilBertTokenizer
from transformers import TFDistilBertForSequenceClassification
import tensorflow as tf
import pandas as pd
import json

col_names=['text','B','category']
df = pd.read_csv("Train.csv",names=col_names,header=None)
df['encoded_cat'] = df['category'].astype('category').cat.codes
save_directory="./MODELS/"
loaded_tokenizer = DistilBertTokenizer.from_pretrained(save_directory)
loaded_model = TFDistilBertForSequenceClassification.from_pretrained(save_directory)

# test_text='Water + Potassium oxide'
# print(test_text)

def VCR(test_text):
    predict_input = loaded_tokenizer.encode(test_text,
                                     truncation=True,
                                     padding=True,
                                     return_tensors="tf")

    output = loaded_model(predict_input)[0]

    prediction_value = tf.argmax(output, axis=1).numpy()[0]
    Result=df.loc[df['encoded_cat'] == prediction_value, 'category'].iloc[0]
    print(Result)
    return Result