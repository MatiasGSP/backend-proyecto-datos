""" class PredictionModelObject:
    def __init__(self):
        self.model="model-roadsign.pkl"
        self.learn = load_learner(path='../prediction_model', file=self.model)
        self.classes = self.learn.data.classes


    def predict_single(self,img_file):
        'function to take image and return prediction'
        prediction = self.learn.predict(open_image(img_file))
        probs_list = prediction[2].numpy()
        return {
            'category': self.classes[prediction[1].item()],
            'probs': {c: round(float(probs_list[i]), 5) for (i, c) in enumerate(self.classes)}
        } """