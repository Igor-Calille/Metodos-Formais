import pytest
from datetime import datetime
from codigo import Investidor, Cadastro, Acao, Noticia, FonteNoticias, Portfolio, PrevisaoMercado, Modelos

def test_investidor():
    investidor = Investidor("Igor", 123456789, "Conservador")
    assert investidor.nome == "Igor"
    assert investidor.contato == 123456789
    assert investidor.perfil == "Conservador"

def test_cadastro():
    cadastro = Cadastro()
    investidor = cadastro.cadastrar_investidor("Igor", 123456789, "Conservador")
    assert investidor in cadastro.lista_investidores
    assert investidor.nome == "Igor"

def test_acao():
    acao = Acao("AZUL4", 50.0, "2024-05-24", 100)
    assert acao.nome == "AZUL4"
    assert acao.preco == 50.0
    assert acao.data == datetime(2024, 5, 24)
    assert acao.quantidade == 100

    acao.atualizar_preco(55.0)
    assert acao.preco == 55.0

def test_noticia():
    noticia = Noticia("A empresa AZUL4 apresentou crescimento no último trimestre.", "2024-05-24")
    assert noticia.conteudo == "A empresa AZUL4 apresentou crescimento no último trimestre."
    assert noticia.data == datetime(2024, 5, 24)

    sentimento = Noticia.analisar_sentimento(noticia)
    assert sentimento == "Positivo"

def test_fonte_noticias():
    fonte = FonteNoticias()
    noticia = Noticia("A empresa AZUL4 apresentou crescimento no último trimestre.", "2024-05-24")
    fonte.adicionar_noticia(noticia)
    assert noticia in fonte.lista_noticias

    noticia_obtida = fonte.obter_noticia("A empresa AZUL4 apresentou crescimento no último trimestre.", "2024-05-24")
    assert noticia_obtida == noticia

    todas_noticias = fonte.obter_noticias()
    assert len(todas_noticias) == 1
    assert todas_noticias[0] == noticia

def test_portfolio():
    portfolio = Portfolio()
    acao = Acao("AZUL4", 50.0, "2024-05-24", 100)
    portfolio.comprar_acao(acao, 100)
    assert any(a.nome == "AZUL4" and a.quantidade == 100 for a in portfolio.painel_invest.valor_acao)

    portfolio.vender_acao(acao, 50)
    assert any(a.nome == "AZUL4" and a.quantidade == 50 for a in portfolio.painel_invest.valor_acao)

def test_previsao_mercado():
    acao = Acao("AZUL4", 50.0, "2024-05-24", 100)
    modelos = Modelos()
    previsao = PrevisaoMercado([acao], modelos)
    
    previsao_valor = previsao.analisar_acao(acao)
    assert previsao_valor == 55.0  # 10% increase

    noticia = Noticia("A empresa AZUL4 apresentou crescimento no último trimestre.", "2024-05-24")
    tendencia = previsao.analisar_noticia(noticia)
    assert tendencia == "Alta"


# Run the tests
if __name__ == '__main__':
    pytest.main(["-v", "--tb=native", 'test.py'])