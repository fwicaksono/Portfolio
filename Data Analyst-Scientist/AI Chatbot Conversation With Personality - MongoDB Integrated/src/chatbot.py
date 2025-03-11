from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain_google_vertexai import VertexAI

class Chatbot:
    def __init__(self, retriever, personality="friendly and helpful"):
        self.personality = personality
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.llm = VertexAI(temperature=0.7)
        
        # Custom prompt with personality
        prompt_template = (
            f"You are a chatbot with a {self.personality} personality. "
            "Use the following context to answer the question. If you don't know the answer, just say 'Sorry, I can't answer that because I don't have enough information.'\n\n"
            "Context: {context}\n\n"
            "Question: {question}\n\n"
            "Answer:"
        )
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        
        self.qa_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=retriever,
            memory=self.memory,
            combine_docs_chain_kwargs={"prompt": prompt}
        )
    
    def chat(self, question):
        """Generate a response to the user's question."""
        result = self.qa_chain({"question": question})
        return result["answer"] 