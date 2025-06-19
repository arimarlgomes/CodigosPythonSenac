print("----------------")
print("----------------")
print("Hamburgueria do Jorgin")
print("----------------")
print("NOSSAS OPÇÕES DE ENTRADAS!")
print("Entrada 1 - Batata Smile - R$ 13")
print("Entrada 2 - Batata com Calabresa - R$ 17")
print("Entrada 3 - Mini Tata - R$ 7")
print("Entrada 4 - Bacon Crispy - R$ 12")
print("Entrada 5 - Misto (Batata, Calabresa e Bacon) - R$ 25")
print("----------------")

valor1 = 0
nomeentrada1 = "x"
entrada1 = int(input("escolha sua entrada, digtando apenas o numero do pedido: "))
quant1 = int(input("quantidade: "))
valorfinal1 = 0

if entrada1 == 1:
    nomeentrada1 = "Batata Smile"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 13
    valorfinal1 = quant1 * valor1
    print(f"custando R$ {valorfinal1:.2f}")

elif entrada1 == 2:
    nomeentrada1 = "Batata com Calabresa"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 17
    valorfinal1 = quant1 * valor1
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada1 == 3:
    nomeentrada1 = "Mini Tata"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 7
    valorfinal1 = quant1 * valor1
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada1 == 4:
    nomeentrada1 = "Bacon Crispy"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 12
    valorfinal1 = quant1 * valor1
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada1 == 5:
    nomeentrada1 = "Misto (Batata, Calabresa e Bacon)"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 25
    valorfinal1 = quant1 * valor1
    print(f"custando R$ {valorfinal1:.2f}")

else:
    print("Nenhum lanche válido foi escolhido")
    nomeentrada1 = "Não Selecionado"
    print(f"você escolheu {nomeentrada1}")
    valor1 = 0
    valorfinal1 = 0
    print(f"custando R$ {valorfinal1:.2f}")
    print("----------------")

print(f"SUBTOTAL: {valorfinal1:.2f}")

    
print("----------------")
print("----------------")
print("----------------")
print("NOSSAS OPÇÕES PRINCIPAIS!")
print("Principal 1 - XTUDO - R$ 13")
print("Principal 2 - XEGG - R$ 17")
print("Principal 3 - XSALADA - R$ 7")
print("Principal 4 - XBURGER - R$ 12")
print("Principal 5 - XRATAO - R$ 25")
print("----------------")

valor2 = 0
nomeentrada2 = "x"
entrada2 = int(input("escolha seu principal, digtando apenas o numero do pedido: "))
quant2 = int(input("quantidade: "))
valorfinal2 = 0

if entrada2 == 1:
    nomeentrada2 = "XTUDO"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 13
    valorfinal2 = quant2 * valor2
    print(f"custando R$ {valorfinal1:.2f}")

elif entrada2 == 2:
    nomeentrada2 = "XEGG"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 17
    valorfinal2 = quant2 * valor2
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada2 == 3:
    nomeentrada2 = "XSALADA"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 7
    valorfinal2 = quant2 * valor2
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada2 == 4:
    nomeentrada2 = "XBURGUER"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 12
    valorfinal2 = quant2 * valor2
    print(f"custando R$ {valorfinal1:.2f}")
elif entrada2 == 5:
    nomeentrada2 = "XRATAO"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 25
    valorfinal2 = quant2 * valor2
    print(f"custando R$ {valorfinal1:.2f}")

else:
    print("Nenhum lanche válido foi escolhido")
    nomeentrada2 = "Não Selecionado"
    print(f"você escolheu {nomeentrada2}")
    valor2 = 0
    valorfinal2 = 0
    print(f"custando R$ {valorfinal2:.2f}")

    print("----------------")

print(f"SUBTOTAL: {valorfinal1 + valorfinal2:.2f}")
    
print("----------------")
print("----------------")
print("----------------")
print("----------------")
print("----------------")
print("NOSSAS OPÇÕES PRINCIPAIS!")
print("Bebida 1 - Coca Cola Lata - R$ 13")
print("Bebida 2 - Coca Cola Zero Lata - R$ 13")
print("Bebida 3 - Coca Cola Light Lata - R$ 13")
print("Bebida 4 - Coca Cola Café Lata - R$ 13")
print("Bebida 5 - Pepsi Lata - R$ 13")
print("Bebida 6 - Pepsi Zero Lata - R$ 13")
print("Bebida 7 - Pepsi Light Lata - R$ 13")
print("----------------")

valor3 = 0
nomeentrada3 = "x"
entrada3 = int(input("escolha sua bebida, digtando apenas o numero do pedido: "))
quant3 = int(input("quantidade: "))
valorfinal3 = 0

if entrada3 == 1:
    nomeentrada2 = "Coca Cola Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")

elif entrada3 == 2:
    nomeentrada2 = "Coca Cola Zero Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")
elif entrada3 == 3:
    nomeentrada3 = "Coca Cola Light Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")
elif entrada3 == 4:
    nomeentrada3 = "Coca Cola Café Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")
elif entrada3 == 5:
    nomeentrada3 = "Pepsi Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")
elif entrada3 == 6:
    nomeentrada3 = "Pepsi Zero Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")
elif entrada3 == 7:
    nomeentrada3 = "Pepsi Light Lata"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 13
    valorfinal3 = quant3 * valor3
    print(f"custando R$ {valorfinal3:.2f}")        

else:
    print("Nenhum lanche válido foi escolhido")
    nomeentrada3 = "Não Selecionado"
    print(f"você escolheu {nomeentrada3}")
    valor3 = 0
    valorfinal3 = 0
    print(f"custando R$ {valorfinal3:.2f}")

    print("----------------")

print(f"SUBTOTAL: {valorfinal1 + valorfinal2 + valorfinal3:.2f}")
    
print("----------------")
print("----------------")
print("----------------")
print("----------------")
print("----------------")
print("NOSSAS OPÇÕES DE SOBREMESA!")
print("Sobremesa 1 - PUDIM - R$ 12")
print("Sobremesa 2 - SORVETE - R$ 11")
print("Sobremesa 3 - SALADA DE FRUTAS - R$ 10")
print("----------------")

valor4 = 0
nomeentrada4 = "x"
entrada4 = int(input("escolha sua sobremesa, digtando apenas o numero do pedido: "))
quant4 = int(input("quantidade: "))
valorfinal4 = 0

if entrada4 == 1:
    nomeentrada4 = "PUDIM"
    print(f"você escolheu {nomeentrada4}")
    valor4 = 12
    valorfinal4 = quant4 * valor4
    print(f"custando R$ {valorfinal4:.2f}")

elif nomeentrada4 == 2:
    nomeentrada4 = "SORVETE"
    print(f"você escolheu {nomeentrada4}")
    valor4 = 11
    valorfinal4 = quant4 * valor4
    print(f"custando R$ {valorfinal4:.2f}")
elif entrada4 == 3:
    nomeentrada4 = "SALADA DE FRUTAS"
    print(f"você escolheu {nomeentrada4}")
    valor4 = 10
    valorfinal4 = quant4 * valor4
    print(f"custando R$ {valorfinal4:.2f}")
else:
    print("Nenhum lanche válido foi escolhido")
    nomeentrada4 = "Não Selecionado"
    print(f"você escolheu {nomeentrada4}")
    valor4 = 0
    valorfinal4 = 0
    print(f"custando R$ {valorfinal4:.2f}")

    print("----------------")

print(f"SUBTOTAL: {valorfinal1 + valorfinal2 + valorfinal3 + valorfinal4:.2f}")