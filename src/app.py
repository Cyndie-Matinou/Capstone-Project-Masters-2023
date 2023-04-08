from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))  # loading my model


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Grabs the input values and uses them to make prediction"""


    bedrooms = int(request.form["bedrooms"])
    bathrooms = int(request.form["bathrooms"])
    condition = int(request.form["condition"])
    Zipcode = int(request.form["Zipcode"])
    output = "testing"

    try:
        #prediction = model.predict([[3,2,3,98052]])
        prediction = model.predict([[bedrooms, bathrooms, condition, Zipcode]])
        output = round(prediction[0])
    except Exception as inst:
        print(type(inst))
        print(inst.args)
        print(inst.args)
        output = "Error"
    #output = round(prediction[0] ,0, 2,  00000)

    return render_template('index.html', prediction_text=f'A house with the features you selected is ${output}')

if __name__ == "__main__":
    app.run()
