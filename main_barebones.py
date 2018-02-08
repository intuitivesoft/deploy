from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/test_endpoint', methods=['GET'])
def test_function():
    print("I made my own web app!")
    return "I'm tired"

@app.route('/train', methods=['POST'])
def train():
    df = pd.DataFrame(request.json)
    df.head()
    # We use a global here so we can modify the model and list of column names
    # global model
    # model = model_utils.train(df)
    # joblib.dump(model, model_utils.MODEL_FILE_NAME)

    return 'Success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
