def encode(n: int, plain_text: str) -> str: # vraci ciphertext typu String
    chunks = [plain_text[i:i+n] for i in range(0, len(plain_text), n)]

    res = [i[::-1] for i in chunks]
    sentence=''
    for item in res:
        sentence+=item
    return sentence

def decode(n: int, cipher_text: str) -> str: # vraci plaintext typu String
    chunks = [cipher_text[i:i+n] for i in range(0, len(cipher_text), n)]
    reverse = [j[::-1]for j in chunks]
    sentence=''
    for item in reverse:
        sentence+=item
    return sentence

# Testy:
print(encode(3, "Ahoj")) # ohAj
print(encode(2, "Ahoj")) # hAjo
print(encode(10, "Ahoj")) # johA
print(encode(3, "12345")) # 32154
print(encode(5, "komunikace")) # numokecaki
print(decode(2, "hAjo")) # Ahoj
print(decode(5, "rgorpavomain")) # programovani
print(decode(3, encode(3, "Karlik a Los Karlos komunikuji sifrovane"))) # Karlik a Los Karlos komunikuji sifrovane
# na automaticke testy doporucuji assert

