
def importe_total_carro(request):
    carro = request.session.get("carro", {})  # Probee un diccionario vacio como valor por defecto
    importe_total = 0
    
    for key, value in carro.items():
        # Calculo importe total
        importe_total += float(value['precio']) * float(value['cantidad'])
    
    return {'importe_total_carro': importe_total}