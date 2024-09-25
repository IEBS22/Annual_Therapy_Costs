from components.query_analyzer import analyze_query
from components.re_router import route_query
from components.sub_llm import process_sub_llms
from components.rag import RAGSystem
from components.response_aggregate import aggregate_response

def main():
    user_query = input("Enter the year for drug cost prediction: ")
    
    analyzed_query = analyze_query(user_query)
    if not analyzed_query["is_valid"]:
        print(f"Error: {analyzed_query['error']}")
        return

    routed_query = route_query(analyzed_query)
    sub_llm_results = process_sub_llms(routed_query)
    
    rag = RAGSystem()
    historical_data = rag.retrieve_relevant_data(analyzed_query["year"])
    rag_prediction = rag.generate_prediction(sub_llm_results, historical_data)
    
    final_response = aggregate_response(analyzed_query["year"], sub_llm_results, rag_prediction)
    print(final_response)

if __name__ == "__main__":
    main()