import logging

from constants.constants import SPEECH_TO_TEXT_MODEL

from openai import OpenAI

class Assistant:
    def __init__(self):
        self.visitor_input = ""
        self.query = ""

    def get_response(self, user_input):
        """This function attempts to get a response for the visitor's query."""
        # Process visitor input
        self.process_visitor_input(user_input)

        # Generate Model Response for User
        model_response = generate_model_response(db_response, self.problem_statement, client, self.response_dialect)
        logging.info(f"Model Response: {model_response}")

        return model_response
    
    def process_visitor_input(self, user_input):
        """This function processes the visitor's input which may be either text or voice input."""
        self.visitor_input = user_input.get("visitor_input")
        self.process_text_input()
        self.process_voice_input()
        return
    
    def process_text_input(self):
        """This function processes any text input (if provided)."""
        self.query = self.visitor_input.get("text_input")
        return
    
    def process_voice_input(self):
        """This function processes any voice input (if provided)."""
        client = OpenAI()
        file_path = self.visitor_input.get("voice_input")
        with open(file_path.get('audio_url'), 'rb') as audio_file:
            transcription = client.audio.transcriptions.create(model=SPEECH_TO_TEXT_MODEL, file=audio_file)
        return transcription.text
    