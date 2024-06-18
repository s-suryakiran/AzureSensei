# from models.chatbot import Query
import db
import time


from openai import AzureOpenAI
import var
# from .config import var as vars


# def query_create(qry: Query):
#     db.query.create(Query)
#     generate_embeddings(qry.query)


# def query_response_get(query_id):
#     db.query.response_get(query_id)

AOAI_client = AzureOpenAI(api_key=var.AZURE_OPENAI_KEY,azure_endpoint=var.AZURE_OPENAI_ENDPOINT,api_version=var.AZURE_OPENAI_VERSION)
collection = db.get_azure_collection()


def generate_embeddings(text):
    """
    Generate embeddings from string of text.
    This will be used to vectorize data and user input for interactions with Azure OpenAI.
    """
    response = AOAI_client.embeddings.create(input=text, model="text-embedding-ada-002")
    embeddings = response.model_dump()
    time.sleep(0.5)
    return embeddings["data"][0]["embedding"]


def vector_search(query, num_results=5):
    query_embedding = generate_embeddings(query)
    embeddings_list = []
    pipeline = [
        {
            '$search': {
                "cosmosSearch": {
                    "vector": query_embedding,
                    "path": "c_vector",
                    "k": num_results#, #, "efsearch": 40 # optional for HNSW only 
                    #"filter": {"title": {"$ne": "Azure Cosmos DB"}}
                },
                "returnStoredSource": True }},
        {'$project': { 'similarityScore': { '$meta': 'searchScore' }, 'document' : '$$ROOT' } }
    ]
    results = collection.aggregate(pipeline)
    return results


def generate_completion(vector_search_results, user_prompt):
    system_prompt = """
    You are an intelligent assistant for Microsoft Azure services.
    You are designed to provide helpful answers to user questions about Azure services given the information about to be provided.
        - Only answer questions related to the information provided below, provide at least 3 clear suggestions in a list format.
        - Write two lines of whitespace between each answer in the list.
        - If you're unsure of an answer, you can say ""I don't know"" or ""I'm not sure"" and recommend users search themselves."
        - Only provide answers that have products that are part of Microsoft Azure and part of these following prompts.
    """

    messages = [{"role": "system", "content": system_prompt}]
    for item in vector_search_results:
        messages.append({"role": "system", "content": item["document"]["content"]})
    messages.append({"role": "user", "content": user_prompt})
    response = AOAI_client.chat.completions.create(
        model="gpt-35-turbo", messages=messages, temperature=0
    )

    return response.dict()


def chat_completion(user_input):
    search_results = vector_search(user_input)
    completions_results = generate_completion(search_results, user_input)
    print("\n")
    return completions_results["choices"][0]["message"]["content"]
