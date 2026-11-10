"""Simulação: remover um nome não garante anonimização."""

def preparar_caso(texto, nome):
    return texto.replace(nome, "[PACIENTE]")

caso = "Ana, CPF fictício 000.000.000-00, relata dor no peito."
enviado = preparar_caso(caso, "Ana")
print(enviado)
print("Identificador restante?", "000.000.000-00" in enviado)
