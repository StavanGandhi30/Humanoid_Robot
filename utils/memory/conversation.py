class ConversationMemory:
    def __init__(self, max_turns=6):
        self.history = []
        self.max_turns = max_turns

    def add_user_input(self, text):
        self.history.append({"role": "user", "content": text})
        self._trim()

    def add_ai_response(self, text):
        self.history.append({"role": "assistant", "content": text})
        self._trim()

    def get_message_history(self):
        return self.history

    def _trim(self):
        if len(self.history) > self.max_turns * 2:
            self.history = self.history[-self.max_turns * 2:]