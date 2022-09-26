# Oppgaven er å lese inn spm og svar fra fila, og gjøre til en quiz
# Legg inn spm som nøkkelverdi, og svar som innholdsverdi

# din kode for å lese inn her:



score = 0
for q in ordbok:
    svar = input(f"{q}?\n")
    if svar.lower() == ordbok[q]:
        score += 1
        print("Riktig!\n")
    else:
        print("Feil..\n")

print(f"Du fikk {score}/{len(ordbok)} riktige!")
