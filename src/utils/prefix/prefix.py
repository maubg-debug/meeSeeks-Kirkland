import json
from os import environ as env

def get_prefix(bot, message):
    """
    Tendremos que coger los prefijos cadavez que esta funcion se llame
    necesitamos pasar el mensage para ver el mensage del servidor

    Si el mensage es de un servidor:
    :return: El array con los prefijos ['?', '!', 'm.'] y con el prefijo personalizado
    
    Si es un mensage directo

    :return: @#~€ (Tiene que ser algo dificil)
    """
    if message.guild is not None:
        try:
            with open(env["JSON_DIR"] + 'prefix.json', 'r') as f:
                prefixes = json.load(f)
            base = [prefixes[str(message.guild.id)], '?', '!', 'm.']
            return base
        except:
            return ['$', '?', '!', 'm.']
    else:
        return "@#~€" # Retornar algo que sea imposible de activar como prefijo
