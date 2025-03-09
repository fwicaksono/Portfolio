from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import VertexAI

class Chatbot:
    def __init__(self, personality="friendly and helpful"):
        self.llm = VertexAI(model_name="text-bison@001")
        self.memory = ConversationBufferMemory()
        self.conversation = ConversationChain(llm=self.llm, memory=self.memory)
        self.personality = personality

    def respond(self, user_input):
        if not user_input:
            return "Sorry, I didn't understand that."
        
        try:
            response = self.conversation.run(f"{self.personality}. {user_input}")
            return response
        except Exception as e:
            print("Error in chatbot.respond():", str(e))  # Log the exception
            return "Sorry, something went wrong. Please try again."