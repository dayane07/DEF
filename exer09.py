def contar_vogais_simples(texto):

 texto_minusculo = texto.lower()

 vogais = "aeiouAEIOUáéíóúÁÉÍÓÚãõÃÕàèìòùÀÈÌÒÙâêîôûÂÊÎÔÛ"
 return sum (1 for caractere in texto_minusculo if caractere in vogais)

frase = "Estou aprendendo python"
print(f"\n '{frase}' tem {contar_vogais_simples(frase)} vogais.")

