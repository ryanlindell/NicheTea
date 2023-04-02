import fileinput
from Bio import Entrez # pip install biopython
from time import sleep

file = fileinput.input("teadata.csv")
file.readline() # skip header
Entrez.email = ''
pubmed_txt = open("pubmed.txt", "a")
i = 0

def get_store_pubmed():
    for line in file:
        tea = line.strip().split(",")[0] + " Tea"
        # print(tea)
        record = Entrez.read(Entrez.esearch(db="pubmed", term=tea, sort="pub_date", reldate=100, retmax=4))['IdList']
        # print(record)

        tea_papers_list = []
        for idNum in record:
            pub_tea_dict = Entrez.read(Entrez.esummary(db="pubmed", id=idNum))[0]
            title = pub_tea_dict["Title"]
            url = "https://pubmed.ncbi.nlm.nih.gov/" + pub_tea_dict["Id"]
            tea_papers_list.append([title, url])
            sleep(0.5)

        pubmed_txt.write(str(tea_papers_list))
        tea_papers_list.clear()
        print(i)
        i += 1
        sleep(2)

def search_pubmed_link():
    for line in file:
        tea = line.strip().split(",")[0].replace(" ", "+") + "+Tea"
        link = "https://pubmed.ncbi.nlm.nih.gov/?term=" + tea
        print(link)

search_pubmed_link()