import pickle

def LoadModel(file_path: str):

    with open('model/iris_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    return loaded_model