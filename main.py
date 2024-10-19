# main.py

import logging
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from agents.agent_factory import AgentFactory
from utils.user_input_handler import get_user_input
from utils.result_formatter import format_results
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Ensure logs directory exists
logs_dir = os.path.join(os.path.dirname(__file__), 'logs')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    filename='logs/system.log',
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configure the Gemini API using environment variable
api_key = os.environ.get("GOOGLE_API_KEY")
if api_key is None:
    logger.error("API key not found in environment variables.")
    raise ValueError("API key not found in environment variables.")
genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_problem = request.json.get('question')
    logger.info("User problem received: %s", user_problem)

    # Step 2: Sequential Processing through Agents
    agent_factory = AgentFactory()
    agents = agent_factory.create_agents()

    previous_solution = None
    all_solutions = []

    for agent in agents:
        solution = agent.get_solution(user_problem, previous_solution)
        all_solutions.append((agent.name, solution))
        previous_solution = solution

    # Final Output
    final_solution = previous_solution
    formatted_result = format_results(all_solutions, final_solution)

    return jsonify({
        'final_solution': final_solution,
        'formatted_result': formatted_result
    })

if __name__ == "__main__":
    app.run(debug=True)
