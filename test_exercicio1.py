from exercicio1 import acao_semaforo
def test_cor_vermelho():
    assert acao_semaforo('vermelho') == 'pare'

def test_cor_amarelo():
    assert acao_semaforo('amarelo') == 'atenção'

    def test_cor_verde():
        assert acao_semaforo('verde') == 'siga'

        def test_cor_errada():
            assert acao_semaforo('roso') ==