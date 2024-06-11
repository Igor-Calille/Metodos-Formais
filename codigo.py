from datetime import datetime
from typing import List, Dict, Union

class Investidor:
    def __init__(self, nome: str, contato: int, perfil: str):
        self.nome = nome
        self.contato = contato
        self.perfil = perfil

class Cadastro:
    def __init__(self):
        self.lista_investidores: List[Investidor] = []

    def  cadastrar_investidor(self, nome: str, contato: int, perfil: str) -> Investidor:
        investidor = Investidor(nome, contato, perfil)
        self.lista_investidores.append(investidor)
        return investidor

class Acao:
    def __init__(self, nome: str, preco: float, data: str, quantidade: int):
        self.nome = nome
        self.preco = preco
        self.data = datetime.strptime(data, "%Y-%m-%d")
        self.quantidade = quantidade

    def atualizar_preco(self, novo_preco: float):
        self.preco = novo_preco

class Noticia:
    def __init__(self, conteudo: str, data: str):
        self.conteudo = conteudo
        self.data = datetime.strptime(data, "%Y-%m-%d")

    @staticmethod
    def analisar_sentimento(noticia: 'Noticia') -> str:
        # Simulacao se houver a palavra crescimento
        sentimento = "Positivo" if "crescimento" in noticia.conteudo else "Negativo"
        return sentimento

class FonteNoticias:
    def __init__(self):
        self.lista_noticias: List[Noticia] = []
        self.analise_fundamentalista: List = []

    def adicionar_noticia(self, noticia: Noticia):
        self.lista_noticias.append(noticia)

    def obter_noticia(self, conteudo: str, data: str) -> Union[Noticia, None]:
        data_formatada = datetime.strptime(data, "%Y-%m-%d")
        for noticia in self.lista_noticias:
            if noticia.conteudo == conteudo and noticia.data == data_formatada:
                return noticia
        return None

    def obter_noticias(self) -> List[Noticia]:
        return self.lista_noticias

class BolsaDeValores:
    def __init__(self):
        self.lista_valor_acoes: List[Acao] = []

class Painel:
    def __init__(self):
        self.valor_acao: List[Acao] = []
        self.principais_noticias: List[Noticia] = []
        self.sugestoes: List = []

class Portfolio:
    def __init__(self):
        self.painel_invest = Painel()

    def comprar_acao(self, acao: Acao, quantidade: int):
        for a in self.painel_invest.valor_acao:
            if a.nome == acao.nome:
                a.quantidade += quantidade
                return
        self.painel_invest.valor_acao.append(Acao(acao.nome, acao.preco, acao.data.strftime("%Y-%m-%d"), quantidade))

    def vender_acao(self, acao: Acao, quantidade: int):
        for a in self.painel_invest.valor_acao:
            if a.nome == acao.nome:
                if a.quantidade >= quantidade:
                    a.quantidade -= quantidade
                    if a.quantidade == 0:
                        self.painel_invest.valor_acao.remove(a)
                return

class Modelos:
    def __init__(self):
        self.modelos_treinados: List = []

class ModeloAnaliseSentimento:
    def __init__(self):
        self.modelo = None
        self.lista_analise_sentimento_noticias: List = []
        self.tendencias_mercado: int = 0

class ModeloAnalisePrevisaoValores:
    def __init__(self):
        self.modelo = None
        self.lista_predicao_acoes: List = []

class PrevisaoMercado:
    def __init__(self, dados: List[Acao], modelos: Modelos):
        self.dados = dados
        self.modelos = modelos

    def analisar_acao(self, acao: Acao) -> float:
        previsao_valor = acao.preco * 1.1  # Simulacao (Apenas 10% aumento)
        return previsao_valor
    
    def analisar_noticia(self, noticia: Noticia) -> str:
        # Simulated market trend analysis logic
        tendencia_mercado = "Alta" if "crescimento" in noticia.conteudo else "Baixa"
        return tendencia_mercado

cadastro = Cadastro()
investidor = Investidor("", 0, "")
portfolio = Portfolio()
acao = Acao("", 0.0, "1970-01-01", 0)
noticia = Noticia("", "1970-01-01")
fonteNoticias = FonteNoticias()
bolsaDeValores = BolsaDeValores()
modelos = Modelos()
modeloAnaliseSentimento = ModeloAnaliseSentimento()

# Simulação

# Adicionar um novo investidor
novo_investidor = cadastro.cadastrar_investidor("Igor", 123456789, "Conservador")

# Comprar uma ação
acao_comprada = Acao("AZUL4", 50.0, "2024-05-24", 100)
portfolio.comprar_acao(acao_comprada, 100)

# Vender uma ação
portfolio.vender_acao(acao_comprada, 50)

# Analisar sentimento de uma notícia
nova_noticia = Noticia("A empresa AZUL4 apresentou crescimento no último trimestre.", "2024-05-24")
sentimento = Noticia.analisar_sentimento(nova_noticia)
print(f"Sentimento da notícia: {sentimento}")

# Atualizar preço de uma ação
acao_comprada.atualizar_preco(55.0)
print(f"Novo preço da ação {acao_comprada.nome}: {acao_comprada.preco}")

# Adicionar uma notícia
fonteNoticias.adicionar_noticia(nova_noticia)

# Obter notícias de uma fonte
noticias = fonteNoticias.obter_noticias()
for noticia in noticias:
    print(f"Notícia: {noticia.conteudo}, Data: {noticia.data}")

# Gerar previsão de mercado
dados = [acao_comprada]
previsao_mercado = PrevisaoMercado(dados, modelos)
previsao_valor = previsao_mercado.analisar_acao(acao_comprada)
print(f"Previsão de valor da ação {acao_comprada.nome}: {previsao_valor}")

tendencia_mercado = previsao_mercado.analisar_noticia(nova_noticia)
print(f"Tendência de mercado para a notícia: {tendencia_mercado}")
