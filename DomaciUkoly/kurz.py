import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")
rows = rows[2:-1]

data = {}
for r in rows:
    cols = r.split("|")
    amount = int(cols[-3])
    curr = cols[-2]
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)
    if(amount > 1):
        rate /= amount

    data[curr] = rate
pprint(data)

user_choice = input("CZK na cizi (napiste -> czk)/ cizi na CZK (napiste -> cizi): ")

if user_choice == "czk":
    user_amount = input("Zadejte částku v CZK: ")
    user_amount = float(user_amount)
    user_curr = input("Zadejte cílovou měnu: ")
    result = user_amount / data[user_curr]
    result = round(result, 2)
elif user_choice == "cizi":
    user_curr = input("Zadejte vaši měnu: ")
    user_amount = input("Zadejte částku: ")
    user_amount = float(user_amount)
    result = user_amount * data[user_curr]
    result = round(result, 2)
    user_curr = "CZK"
else:
    print("špatně zvolený převod")

print(f"Vysledna castka je {result} {user_curr}")