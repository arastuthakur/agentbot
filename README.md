# Flask Application with Google Generative AI and Agents

This project is a Flask-based web application that allows users to ask questions, process them through a series of agents, and receive solutions. The application integrates with Google Generative AI (Gemini API) for advanced language processing and includes custom agents for solution generation.

## Features

- Web interface to accept user input.
- Multiple agents to process user questions.
- Integration with Google Generative AI for language model responses.
- Logging for debugging and tracking.
- Environment variable management with `.env` file.

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Flask
- Google Generative AI SDK

## Installation

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variables by creating a `.env` file in the project root directory with your API key:

    ```plaintext
    GOOGLE_API_KEY=your-google-api-key
    ```

4. Ensure that the `logs/` directory exists for logging purposes. If not, the app will automatically create it.

## Running the Application

To run the application locally:

```bash
python main.py
```
The application will start in debug mode. Open your browser and navigate to:
```arduino
http://127.0.0.1:5000/
```
API Endpoints
POST /ask
Accepts a question from the user as a JSON payload.
Example request:
```json
{
    "question": "What is the impact of AI on healthcare?"
}
```
Example response:
```json
{
    "final_solution": "The final solution to the problem...",
    "formatted_result": "Formatted results from agents..."
}
```
Project Structure
```bash
├── agents/
│   ├── agent_factory.py
├── utils/
│   ├── user_input_handler.py
│   ├── result_formatter.py
├── logs/
│   └── system.log
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
└── .env
```
Logging
Logs are stored in the logs/system.log file. The logging level is set to INFO by default.

Contributing
Feel free to open a pull request if you'd like to contribute to this project.
