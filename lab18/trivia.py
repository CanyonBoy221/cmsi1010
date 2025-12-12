import requests
from urllib.parse import unquote


def fetch_trivia_question(count):
    url = f"https://opentdb.com/api.php?amount={count}&type=multiple&encode=url3986"
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError(f'API error: {response.status_code}')
    return response.json()


def check_response(body):
    if body['response_code'] != 0:
        raise ValueError(f'OpenTDB error: {body["response_code"]}')


def extract_question(body):
    question = body['results'][0]
    question['category'] = unquote(question['category'])
    question['question'] = unquote(question['question'])
    question['correct_answer'] = unquote(question['correct_answer'])
    question['incorrect_answers'] = [
        unquote(ans) for ans in question['incorrect_answers']]
    return question


def play_game():
    body = fetch_trivia_question(1)
    check_response(body)
    question = extract_question(body)
    print(question)


play_game()
