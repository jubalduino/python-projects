import random

tabela_bicho = {
    "avestruz": ["01", "02", "03", "04"],
    "aguia": ["05", "06", "07", "08"],
    "burro": ["09", "10", "11", "12"],
    "borboleta": ["13", "14", "15", "16"],
    "cachorro": ["17", "18", "19", "20"],
    "coelho": ["21", "22", "23", "24"],
    "cavalo": ["25", "26", "27", "28"],
    "elefante": ["29", "30", "31", "32"],
    "cobra": ["33", "34", "35", "36"],
    "galo": ["37", "38", "39", "40"],
    "gato": ["41", "42", "43", "44"],
    "jacare": ["45", "46", "47", "48"],
    "lebre": ["49", "50", "51", "52"],
    "urso": ["53", "54", "55", "56"],
    "touro": ["57", "58", "59", "60"],
    "leao": ["61", "62", "63", "64"],
    "macaco": ["65", "66", "67", "68"],
    "javali": ["69", "70", "71", "72"],
    "porco": ["73", "74", "75", "76"],
    "pavao": ["77", "78", "79", "80"],
    "peru": ["81", "82", "83", "84"],
    "tucano": ["85", "86", "87", "88"],
    "urso": ["89", "90", "91", "92"],
    "veado": ["93", "94", "95", "96"],
    "vaca": ["97", "98", "99", "00"]
}

print(" BEM-VINDO AO JOGO DO BICHO NO PYTHON \n")
print("Sonhou com o que hoje? :", ", ".join(tabela_bicho.keys()).title())

bicho_apostado = ""

while True:
    aposta = input("\nQue bicho vai dar hoje? ").lower().strip()

    
    if aposta in tabela_bicho:
        bicho_apostado = aposta
        print(f"\n Hoje é {bicho_apostado.upper()} na cabeça! {tabela_bicho[bicho_apostado]}")
        print("Será que hoje é seu dia ... ")
        break

    
    elif aposta.isdigit():
        dezena_digitada = aposta.zfill(2)
        
        
        for bicho, dezenas in tabela_bicho.items():
            if dezena_digitada in dezenas:
                bicho_apostado = bicho
                break
        
        if bicho_apostado:
            print(f"\n Você apostou na dezena {dezena_digitada}, que pertence ao {bicho_apostado.upper()}!")
            break
        else:
            print("❌ Essa dezena não vale. Tente outra!")
            continue

    
    print("❌ Deu Ruim! Tente de novo!")



numero_sorteado = str(random.randint(0, 9999)).zfill(4)
dezena_sorteada = numero_sorteado[-2:]

print("\n" + "-" * 40)
print(f" NÚMERO SORTEADO: {numero_sorteado} (Dezena final: {dezena_sorteada})")
print("-" * 40)


bicho_vencedor = "Nenhum (bicho não cadastrado)"
for bicho, dezenas in tabela_bicho.items():
    if dezena_sorteada in dezenas:
        bicho_vencedor = bicho
        break

if bicho_apostado == bicho_vencedor:
    print(f" DEU {bicho_vencedor.upper()}! Parabéns, você ganhou o prêmio máximo! Diversão! \n")
else:
    print(f" DEU {bicho_vencedor.upper()}... Não foi dessa vez! Mais sorte na próxima.\n")