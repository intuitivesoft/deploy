import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier as rf

# inputs
#MODEL_DIRECTORY = 'model'
#MODEL_FILE_NAME = '%s/model.pkl' % MODEL_DIRECTORY

def train(df):

    #df_ = df[include]
    print("Training data sample:\n", df.head())
    

    # capture a list of columns that will be used for prediction
    model_columns = list(x.columns)
    print("Model columns are", model_columns)

    model = rf()
    start = time.time()
    model.fit(x, y)
    print('Trained in %.1f seconds' % (time.time() - start))
    print('Model training score: %s' % model.score(x, y))

    return model_columns, model


# def predict(input_df, model, columns):
#     print("Input data frame is...\n")
#     print("-----------")
#     print(input_df)
#     print("-----------")
#     query = pd.get_dummies(input_df)
#
#     # Give all missing values a value of 0
#     query = query.reindex(columns=columns, fill_value=0)
#
#     predictions = model.predict(query).tolist()
#     predictions = [int(prediction) for prediction in predictions]
#
#     return {'predictions': predictions}
