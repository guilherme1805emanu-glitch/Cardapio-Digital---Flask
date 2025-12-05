from veiculos import Veiculo, Carro, Moto, concessionaria

concessionariaTeste = concessionaria("Carros e Motos LTDA")
carro1 = Carro("Chevrolet","Onix",2023,90000.00,"Etanol",4)
moto1 = Moto("Yamaha","MT-09",2022,60000.00,890,"Elétrica")
concessionariaTeste.adicionarVeiculo(carro1)    
concessionariaTeste.adicionarVeiculo(moto1)
concessionariaTeste.listarVeiculos()