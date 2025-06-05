import streamlit as st 
import numpy as np 
import pickle
import tensorflow 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing.sequence import pad_sequences

model=load_model('mymodel.h5')

with open('tokenizer.pkl','rb') as handel:
    tokenizer=pickle.load(handel)


def predict(model,tokenizer,text,max_sequence_len):
    token_list=tokenizer.texts_to_sequences([text])[0]
    if len(token_list)>=max_sequence_len:
        token_list=token_list[-(max_sequence_len-1):]
    token_list=pad_sequences([token_list],maxlen=max_sequence_len-1,padding='pre')
    predicted=model.predict(token_list,verbose=0)
    predicted_index=np.argmax(predicted,axis=1)
    for word,index in tokenizer.word_index.items():
        if index==predicted_index:
            return word
    return None


st.title("Next word Prediction")
input_text=st.text_input("enter the sequence of Word","To bo or not to")
if st.button("predict next word"):
    max_sq=model.input_shape[1]+1
    next_word=predict(model,tokenizer,input_text,max_sq)
    st.write("next word  "+ next_word)
