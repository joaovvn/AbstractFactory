import vagas

class Main():
  def __init__(self):
    pass
  
  vagasEG = vagas.Vagas.factory('EdificioGaragem')
  vagasExt = vagas.Vagas.factory('VagasExternas')

  vagasEG.ocuparVaga()
  vagasExt.desocuparVaga()
  vagasExt.vagasIndisponiveis()
  vagasEG.vagasDisponiveis()