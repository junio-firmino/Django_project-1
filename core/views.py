from django.shortcuts import render


def index(request):
    exemplo = {
        'informação': 'Teste de informação na página.',
        'endereço': 'Rua c lote 52, quadra 968'
    }

    return render(request, 'index.html', exemplo)


def contato(request):
    exemplo_1 = {
        'contato':'Teste para o EXEMPLO'
    }
    return render(request, 'contato.html', exemplo_1)


