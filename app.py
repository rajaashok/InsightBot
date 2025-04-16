import os
import json
from flask import Flask, request, jsonify, render_template



from pydantic import BaseModel, Field
from agents.growth_agent import GrowthAgent

import logging

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.DEBUG,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

logging.info("APPLICATION STARTED")

app = Flask(__name__)


# Load the knowledge base from the JSON file
def load_knowledge_base():
    with open("schema.json", "r") as f:
        return json.load(f)

class KBResponse(BaseModel):
    # answer: str = Field(description="The answer to the user's question.")
    sql: str = Field(description="The generated SQL query.")



@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask():
    schema = load_knowledge_base()
    
    user_message = request.json.get('message')
    
    logging.info('User Input is : %s', user_message)
    ga = GrowthAgent(schema)
    result = ga.analyze_strategy(user_message)
    logging.info('Pre Final Send : %s', result)
    
    # Format the results for user display
    if result is not None:
        formatted_results = {
            "message": "Query executed successfully.",
            "data": result
        }
    else:
        formatted_results = {
            "message": "No results found or an error occurred.",
            "data": result
        }

    logging.info('Final send is : %s', str(formatted_results))
    return formatted_results

if __name__ == '__main__':
    app.run(debug=True)
