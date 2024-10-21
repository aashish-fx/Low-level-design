from stack_overflow_engine import Engine
class StackOverFlowDemo:
    
    @staticmethod
    def run():
        engine = Engine()
        aashish = engine.create_user("Aashish", "ash569sharma@gmail.com")
        h_name = engine.create_user("H", "h@gmail.com")
        
        question = engine.post_question(aashish, "How are you?", "What is polymorphism in Java?", ["Java", "CS"])
        
        answer = engine.answer_questions(h_name, question, "Polymorphism in Java is the ability of an object to take on many forms..")
        engine.add_comment(aashish, answer, "Thanks...")
        
        engine.vote(h_name, question, "UP")
        
        
        
        
if __name__ == "__main__":
    StackOverFlowDemo.run()
        
        
        