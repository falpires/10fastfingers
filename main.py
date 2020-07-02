from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
from os import environ

def main():

    # Pegar o HOMEPATH (Windows)
    home_dir = environ.get("USERPROFILE")

    # PATH Completo para o WebDriver
    webdriver_path = f"{home_dir}\\Desktop\\EdgeDriver\\msedgedriver"

    driver = webdriver.Edge(executable_path=webdriver_path)
    driver.get("https://10fastfingers.com/typing-test/portuguese")

    # Verifica se estamos na pagina certa
    assert "Teste de Digitação Portuguese" in driver.title

    # Pegar o array de palavras utilizado no testes
    word_array = driver.find_elements_by_css_selector("#row1 span")
    print("Word array found")

    # Pegar o elemento de input das palavras
    input_field = driver.find_element_by_css_selector("#inputfield")
    print("Input field found")

    # Loop pelas palavras do array
    for word in word_array:
        print(word.text)
        write(word.text, input_field)
    sleep(120)



def write(word, input_field, wait_time=0.01):
    """
    Escreve a palavra no inputfield, letra por letra, com tempo entre as letras.
    """
    for letter in word:
        input_field.send_keys(letter)
        sleep(wait_time)
    input_field.send_keys(Keys.SPACE)


if __name__ == "__main__":
    main()