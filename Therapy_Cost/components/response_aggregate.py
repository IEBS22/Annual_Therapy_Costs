def aggregate_response(year, sub_llm_results, rag_prediction):
    response = f"Annual Therapy Cost Prediction for {year}:\n"
    response += f"Predicted Cost: ${rag_prediction:.2f}\n\n"
    response += "Factors considered:\n"
    for llm, value in sub_llm_results.items():
        response += f"- {llm}: {value:.4f}\n"
    return response