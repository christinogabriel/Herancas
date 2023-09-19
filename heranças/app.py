class Servidor:
    #função construtora
    def __init__ (self,serverName : str =  None, Ip: int=000):
        self.ServerName = serverName
        self.IpAdress = Ip
        self.Service= False

    #função comum

    def IniciarServicoServidor(self,Ip) -> bool:
        if(Ip == self.IpAdress):
            return self.Service == True
        else:
            raise ErroServidor("Ip invalido","A classe iniciou com um Ip que não existe") 
    
    #criando exceção customizada   
class ErroServidor(Exception):
    def __init__(self,Mensagem,Erro) -> None:
        super().__init__(Mensagem)             # o metodo super() ele sobrescreve e chama os métodos que a Exception possuem
        self.error = Erro
        print(self.error)

#-------------------------------------------------Criando Herança---------------------------------------#
class Rede(Servidor):
    #método construtor carregando os parametros do Servidor
    def __init__ (self,serverName : str =  None, Ip: int=000,NomeRede:str="Nenhum"):
        super().__init__(serverName,Ip)
        self.RedeNam:str=""

    def CriarConexaoRede(self,ServidorBase,ServidorCon):
        if(isinstance(ServidorBase,Servidor)): # isinstance verifica o tipo da variável
            ServidorBase.IpAdress = ServidorCon.IpAdress
            return ServidorBase.ServerName + ServidorCon.ServerName
            
    #criando objetos-teste

Server01 = Servidor("Google",500)
Server02 = Servidor("Amazon",300)
Server02.IniciarServicoServidor(300)
Conexao = Rede ("google",500,"Bridge")
print(Conexao.CriarConexaoRede(Server01,Server02))
