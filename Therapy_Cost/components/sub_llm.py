import numpy as np

class SubLLM:
    def __init__(self, attributes):
        self.attributes = attributes
        # load a trained model
    
    def process(self, data):
        # processing with a random output
        return np.random.rand()

def process_sub_llms(routed_query):
    sub_llm_outputs = {}
    for llm, data in routed_query.items():
        sub_llm = SubLLM(data["attributes"])
        sub_llm_outputs[llm] = sub_llm.process(data)
    return sub_llm_outputs