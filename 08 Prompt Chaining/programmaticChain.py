
def analysis_chain(document): 
	# Step 1: Summarize summary = call_ai(f""" 
				Summarize the key points of this document in 5 bullets: 
				{document} 
				""") 

	# Step 2: Extract entities entities = call_ai(f""" 
				Extract named entities (people, organizations, locations) from this summary. Return as JSON. {summary} 
				""") 

	# Step 3: Generate insights insights = call_ai(f""" 
				Based on this summary and entities, generate 3 actionable insights for a business analyst. Summary: {summary} Entities: {entities} 
				""") 

	return { 
			"summary": summary,
			"entities": json.loads(entities), 
			"insights": insights 
		}
		
