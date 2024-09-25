import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

class SubLLM:
    def __init__(self, attributes):
        self.attributes = attributes
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.label_encoders = {}
        self.load_and_train_model()
    
    def load_and_train_model(self):
        # Load the data
        data = pd.read_csv('data/drug_data.csv')
        
        # Prepare the features and target
        X = data[self.attributes]
        y = data['annual_therapy_cost']
        
        # Encode categorical variables
        for column in X.select_dtypes(include=['object']):
            le = LabelEncoder()
            X[column] = le.fit_transform(X[column])
            self.label_encoders[column] = le
        
        # Train the model
        self.model.fit(X, y)
    
    def process(self, data):
        # Prepare the input data
        input_data = pd.DataFrame([data])
        
        # Encode categorical variables
        for column, le in self.label_encoders.items():
            if column in input_data.columns:
                input_data[column] = le.transform(input_data[column])
        
        # Make prediction
        prediction = self.model.predict(input_data[self.attributes])[0]
        return prediction

def process_sub_llms(routed_query):
    sub_llm_outputs = {}
    for llm, data in routed_query.items():
        sub_llm = SubLLM(data["attributes"])
        sub_llm_outputs[llm] = sub_llm.process(data)
    return sub_llm_outputs
