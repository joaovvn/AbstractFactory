from abc import ABCMeta, abstractmethod

class Estacionamento(metaclass = ABCMeta):

  @abstractmethod
  def ocuparVaga(self):
    pass
 
  @abstractmethod
  def desocuparVaga(self):
    pass

  @abstractmethod
  def vagasIndisponiveis(self):
    pass

  @abstractmethod
  def vagasDisponiveis(self):
    pass

class Vagas(Estacionamento):
  def factory(local):
    if local == 'EdificioGaragem':
      return EdificioGaragem()
    elif local == 'VagasExternas':
      return VagasExternas()

class EdificioGaragem(Estacionamento):
  def ocuparVaga(self):
    print('A vaga 32 do Edificio Garagem agora está ocupada.')
    
  def desocuparVaga(self):
    print('A vaga 27 do Edificio Garagem agora está desocupada.')
    
  def vagasIndisponiveis(self):
    print('Todas as vagas do Edificio Garagem estão ocupadas!')
    
  def vagasDisponiveis(self):
    print('23 vagas do Edificio Garagem estão disponiveis!')

class VagasExternas(Estacionamento):
  def ocuparVaga(self):
    print('A vaga externa 15 agora está ocupada.')
  
  def desocuparVaga(self):
    print('A vaga externa 43 agora está desocupada.')
  
  def vagasIndisponiveis(self):
    print('Todas as vagas externas estão ocupadas!')
  
  def vagasDisponiveis(self):
    print('73 vagas externas estão disponiveis!')