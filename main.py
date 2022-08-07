class pc:
    def __init__(self, marca, memoria, placa):
        self.marca = marca
        self.memoria = memoria
        self.placa = placa
    
    def ligar(self):
        print('ligando')

    def desligar(self):
        print('estou desligando')
    ''
    def configura(self):
        print(self.marca, self.memoria, self.placa)


pc1 = pc('samsung', '4gb', 'intel')
pc1.ligar()
pc1.desligar()
pc1.configura()


'''pc2 = pc('lenovo', '8gb', 'gtx')
pc3 = pc('dell', '8gb', 'gtx')
print(pc1.marca, pc1.memoria, pc1.placa)
print(pc2.marca, pc2.memoria, pc2.placa)
print(pc3.marca, pc3.memoria, pc3.placa)'''




