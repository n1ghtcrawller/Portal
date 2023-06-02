from bs4 import BeautifulSoup

with open("list3.xml") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
