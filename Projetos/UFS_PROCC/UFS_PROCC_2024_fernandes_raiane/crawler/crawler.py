import requests
from bs4 import BeautifulSoup
from links import links

def get_stackexchange_data(url):
    # Enviar uma requisição para o link
    response = requests.get(url)
    response.raise_for_status()  # Verifica se a requisição foi bem-sucedida

    # Analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extrair o título da pergunta
    title = soup.find('a', class_='question-hyperlink').get_text(strip=True).replace("\n", " ")

    # Extrair o conteúdo da pergunta
    question_content = soup.find('div', class_='s-prose js-post-body').get_text(strip=True).replace("\n", " ")

    # Encontrar a resposta com mais votos
    answers = soup.find_all('div', class_='answer')

    best_answer = max(answers, key=lambda answer: int(answer.find('div', class_='js-vote-count').get_text(strip=True)))

    # Extrair o conteúdo da melhor resposta
    best_answer_content = best_answer.find('div', class_='s-prose js-post-body').get_text(strip=True).replace("\n", " ")

    return title, question_content, best_answer_content


for link in links:
    # Exemplo de uso
    url = link
    title, question_content, best_answer_content = get_stackexchange_data(url)

    print(link + "vascodagama " + title + "vascodagama " + question_content + "vascodagama " + best_answer_content)
