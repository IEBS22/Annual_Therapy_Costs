import random

class RAGSystem:
    def __init__(self):
        #vector db?
        pass
    
    def retrieve_relevant_data(self, year):
        # retrieve of historical data
        return {"historical_avg_cost": random.uniform(1000, 10000)}
    
    def generate_prediction(self, sub_llm_outputs, historical_data):
        # sub-LLM outputs + historical data
        prediction = sum(sub_llm_outputs.values()) * historical_data["historical_avg_cost"] / len(sub_llm_outputs)
        return prediction