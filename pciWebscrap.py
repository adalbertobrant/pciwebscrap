import requests as rq
import json
import os
from bs4 import BeautifulSoup

# variables
urlheader = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}

base_url = "https://www.pciconcursos.com.br/provas/engenheiro-civil/"

url_aux = "https://www.pciconcursos.com.br/provas/engenheiro-civil/"

# list of all links that must be follow
new_url_proxima = []
new_url_proxima.append(base_url)

# list of links to a próxima page 
new_url_table = []
filtered_links = []

# list of json files with cargo, ano, órgão, instituição, nível, prova, gabarito
json_final_list_links = []

# contador
url_counter = 0

# first create a list with all the list to other pages in the engenheiro civil subject

while(True):
  response = rq.get(url_aux, headers=urlheader)
  
  soup = BeautifulSoup(response.content, "html.parser")

  proxima_link = soup.find('a', string="Próxima ->>")

  if proxima_link is None:
    print("Todas as páginas encontradas")
    break
 
  aux = proxima_link['href']
  new_url_proxima.append(proxima_link["href"])

  url_aux = base_url + aux.split("/")[-1]
  url_counter += 1

print(f"Links Encontrados para provas -{url_counter+1}")

# list of all the tables links

for link in new_url_proxima:
  response = rq.get(link, headers=urlheader)
  soup = BeautifulSoup(response.content, "lxml")
  table = soup.find('table', id="lista_provas")
  for a in table.findAll('a'):
    text = a.text
    aux_url = a.get('href')
    new_url_table.append(aux_url)

filtered_links = [eng_civil for eng_civil in new_url_table if "engenheiro-civil" in eng_civil]

print("Listas ")
print('==============')
print(f"Quantidade de links {len(filtered_links)}")
print("")
# create the final list with gabarito and questions links format [{prova:link}, {gabarito:link}]
contador = 0
data = {}
for link in filtered_links:
  response = rq.get(link, headers=urlheader)
  soup = BeautifulSoup(response.content, "lxml")
  ul = soup.find('ul',{'class':'pdf_download'})
  
  for i, li in enumerate(ul.findAll('li')):
    if i == 0:
      data['prova'] = li.a['href']
    if i == 1:
      data['gabarito'] = li.a['href']
    json_final_list_links.append(data)

print('')    
print(f"Quantidade de provas e gabaritos {len(json_final_list_links)}")
print('')  
# dump the json_final_list_links to a txt file.
json_string = json.dumps(json_final_list_links)

with open('provas_gabaritos_engenheiro_civil.txt', 'w') as file:
  file.write(json_string)





  


