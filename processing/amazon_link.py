import fileinput

file = fileinput.input("teadata.csv")
file.readline() # skip header

for line in file:
    line = line.strip().split(",")[0].replace(" ", "+")
    base_url = "https://www.amazon.com/s?k=" + line + "+Tea&s=review-rank&tag=wmchance-20"
    print(base_url)