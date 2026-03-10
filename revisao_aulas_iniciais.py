senhas = ["1234", "9876", "a1b2", "1111"]

for s in senhas:
    if s.isdigit(): # Verifica se é só número
        print(f"A senha {s} é numérica e perigosa.")
