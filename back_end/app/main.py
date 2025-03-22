import google.generativeai as genai
from constants.constants import ASSISTANT_MODEL
from config import Config

def configure_genai():
    """
    Configures the Google Generative AI client with the API key from the configuration.
    """
    try:
        config = Config()
        genai.configure(api_key=config.GENAI_API_KEY)
    except ValueError as e:
        raise RuntimeError(f"Configuration error: {e}") from None

def generate_problem_statement(audio_text, model_name):
    """
    Generates a problem statement for a given audio query using the specified AI model.
    """
    try:
        prompt = f"For the provided customer query, produce a problem statement to be forwarded to the respective department: '{audio_text}'"
        
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error during content generation: {e}") from None

def main():
    """
    Main function to generate a problem statement for a sample audio query.
    """
    audio_text = "How many years have you spent in the industry?"
    configure_genai()
    try:
        result = generate_problem_statement(audio_text, ASSISTANT_MODEL)
        print(result)
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
