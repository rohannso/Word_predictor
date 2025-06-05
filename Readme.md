# Next Word Prediction

This is a Streamlit app that predicts the next word in a sequence using a trained Keras model.

## Files

- `app.py`: Main Streamlit application.
- `mymodel.h5`: Trained Keras model.
- `tokenizer.pkl`: Tokenizer used for preprocessing.
- `requirements.txt`: Python dependencies.
- `next_word.ipynb`: Jupyter notebook for model development.

## Usage

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the app:
    ```sh
    streamlit run app.py
    ```

3. Enter a sequence of words in the input box and click "predict next word" to see the predicted next word.

## Example

You can use a line from Shakespeare's Hamlet to test the app. For example, enter:

```
Ham. I humbly thank you Sir, dost know 
```

and click "predict next word". The app will predict the next word in the sequence based on the trained model.

## Requirements

- Python 3.x
- See `requirements.txt` for package list.

## Notes

- Ensure `mymodel.h5` and `tokenizer.pkl` are present in the same directory as `app.py`.