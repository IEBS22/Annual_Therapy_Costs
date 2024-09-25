def route_query(analyzed_query):
    if analyzed_query["is_valid"]:
        return {
            "sub_llm_1": {"attributes": ["drug_name", "resolution_year", "benefit"], "year": analyzed_query["year"]},
            "sub_llm_2": {"attributes": ["morbidity", "mortality", "comparative_therapy"], "year": analyzed_query["year"]},
            "sub_llm_3": {"attributes": ["age_group", "combined_therapy"], "year": analyzed_query["year"]},
            "sub_llm_4": {"attributes": ["other_relevant_attributes"], "year": analyzed_query["year"]}
        }
    else:
        return {"error": analyzed_query["error"]}