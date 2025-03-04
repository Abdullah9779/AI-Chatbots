import pandas as pd
from difflib import get_close_matches

def load_data(path):
    data = pd.read_csv(path)
    return data

def get_match(user_question, questions):
    match = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return match[0] if match else None

def get_response(question, data):
    for i, q in enumerate(data['question']):
        if question == q:
            return data['answer'][i]
        
def chatbot(user_question, data):
    question = get_match(user_question, data['question'])
    if question:
        return get_response(question, data)
    else:
        return 'Sorry, I do not understand your question.'
    
if __name__ == '__main__':
    data = load_data('Intelligent Chatbot\\MyData.csv')
    while True:
        user_question = input('You: ')
        if user_question.lower() == 'exit':
            print('Chatbot: Goodbye!')
            break
        response = chatbot(user_question, data)
        print('Chatbot:', response)