import decimal

def get_solary(names: list[str], stavka: list[int], prem: list[str]) -> dict[str:decimal.Decimal]:
    n = len(names)
    res = {}

    for i in range(n):
        res[names[i]] = stavka[i] + stavka[i]*decimal.Decimal(prem[i].replace('%', ''))/100
    return res

names = ['John', 'Garry', 'Tom']
stavka = [10000, 20000, 30000]
prem = ['10%', '20%', '30%']
print(get_solary(names, stavka, prem))