from .models import Cliente

def user_context(request):
    """
    Adiciona informações do cliente ao contexto global.
    """
    cliente_id = request.session.get('cliente_id')
    if cliente_id:
        try:
            cliente = Cliente.objects.get(id=cliente_id)
            return {
                'user_name': cliente.nome,
                'cliente': cliente,
            }
        except Cliente.DoesNotExist:
            pass
    return {
        'user_name': None,
        'cliente': None,
    }
