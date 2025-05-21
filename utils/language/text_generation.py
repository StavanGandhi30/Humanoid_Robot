import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from dotenv import load_dotenv
from openai import OpenAI
from utils import *

class TextGeneration:
    def __init__(self):
        load_dotenv()
        
        self.memory = ConversationMemory(max_turns=10)
        self.system_prompt = f"You are a friendly and curious assistant embedded in a humanoid robot. Respond naturally, concisely, and emotionally expressive."
    
    def generate_response(self, user_input):
        self.memory.add_user_input(user_input)

        try:
            client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

            response = client.chat.completions.create(
              model="gpt-4.1",
              prompt=[{"role": "system", "content": self.system_prompt}] + self.memory.get_message_history(),
              max_tokens=7,
              temperature=0
            )
            
            reply = response.choices[0].message['content'].strip()
            self.memory.add_ai_response(reply)
            return reply
        
        except Exception as e:
            return f"[Error generating response: {e}]"
        
    def interact(self, user_input):
        response = self.generate_response(user_input)
        return response
    
if __name__ == "__main__":
    robot = TextGeneration()
    while True:
        user_input = input("You: ")
        response = robot.interact(user_input)
        print("Robot:", response)
