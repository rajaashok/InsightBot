# growth_agent.py
from chains.query_chain import query_chain
from db.postgres_connector import run_query
from langchain.llms import OpenAI  # Can also switch to ChatOpenAI for consistency
import json
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',  # Log file name
    level=logging.INFO,  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log message format
)

class GrowthAgent:
    def __init__(self, metadata):
        self.metadata = metadata
        self.llm = OpenAI(temperature=0.3)

    def analyze_strategy(self, strategy_goal):

        response = query_chain.invoke({
            "goal": strategy_goal,
            "metadata": self.metadata
        })

        print("Raw LLM Response:", repr(response.content))
        try:
            structured_subqueries = json.loads(response.content)
            logging.info(structured_subqueries)
        except json.JSONDecodeError as e:
            logging.error("Failed to parse JSON:", e)
            logging.error("Raw response was:", response.content)
            raise

        # subqueries = response.content.split("\n") if hasattr(response, "content") else response.split("\n")

        results = {}
        for sub in structured_subqueries:
            question = sub["question"]
            logging.info("Running sub-question:  \n \n %s", question)
            sql_query = self.llm(
                f"""
                    You are a senior SQL analytics expert working with a PostgreSQL database for a ride-sharing platform. You always write executable SQL queries.

                    You have access to the following tables and their schemas:
                    {self.metadata}

                    Your job is to write executable, aggregate-level SQL queries to answer analytical business questions.

                    Follow these rules strictly:
                    
                    - ✅ Always prefix all column names with their table alias (e.g., `du.country`, `dr.avg_ride_time`) — even in `GROUP BY`, `ORDER BY`, `SELECT`, and `JOIN` conditions.
                    - ✅ Always use table aliases (e.g., `du`, `dr`, `rev`) and prefix every column with the correct alias to avoid `psycopg2.errors.AmbiguousColumn` or column not found errors.
                    - ✅ JOIN tables only on matching keys — usually `country` and `date`.
                    - ✅ Always include `GROUP BY` on high-level dimensions (e.g., `country`, `date`) when aggregation is used.
                    - ✅ Use aggregation functions like `AVG`, `SUM`, `CORR`, etc., depending on the question.
                    - ✅ When using `INTERVAL` columns like `avg_ride_time`, use: `EXTRACT(EPOCH FROM alias.column)::INT` to convert to seconds.
                    - ✅ The query SHOULD NEVER return unaggregated data. Consider the result to be served to CEO/CFO

                    ❌ Avoid selecting raw unaggregated columns alongside aggregates unless they are in the GROUP BY clause.
                    ❌ Never select the same column multiple times or repeat alias names.
                    ❌ Never select all columns (no `SELECT *`).

                    -----------------------

                    Convert the following natural language business question into an optimized SQL query:
                    
                    Question: "{question}"
                    
                    Return only the Aggregated SQL query that is executable on metadata provided.
                """    
            )
            logging.info('Returned SQL Query: \n \n %s', sql_query)
            query_result = run_query(sql_query)
            if query_result is None or 'error' in str(query_result).lower():
                logging.error('Error executing query: %s', sql_query)
                results[question] = {
                    "purpose": sub["purpose"],
                    "query_result": "An error occurred while executing the query."
                }
            elif len(query_result) > 100:
                results[question] = {
                    "purpose": sub["purpose"],
                    "query_result": "The query returned too many results. Please refine the query."
                }
            else:
                results[question] = {
                    "purpose": sub["purpose"],
                    "query_result": run_query(sql_query)
                }

        return self.summarize_insights(strategy_goal, results)

    def summarize_insights(self, strategy_goal, data):
        joined_data = "\n".join([f"{q}:\n{r}" for q, r in data.items()])
        logging.info('In summarize Insights:  \n \n %s', joined_data)
        summary_prompt = (
            f"""Given the goal: "{strategy_goal}" and the following query results:\n
{joined_data}\n\nGenerate a strategic recommendation in bullet points and explain why you have provided the recommndation."""
        )
        return self.llm(summary_prompt)
