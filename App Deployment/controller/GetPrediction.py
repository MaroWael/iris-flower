def GetPrediction(model, inputs: list):
    result = {
    0: "tris-setosa",
    1:"Iris-versicolor",
    2: "tris-virginica" }
    predction = model.predict([inputs])[0]
    return result[predction]
