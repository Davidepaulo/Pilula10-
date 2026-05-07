def acao_semaforo(cor: str):
    cor = cor. lower()
    if cor == 'vermelho':
        return 'pare'
    elif cor == 'amarelo1':
        return 'atenção'
    elif cor == 'verde':
        return 'siga'
    return 'cor inváida'
    