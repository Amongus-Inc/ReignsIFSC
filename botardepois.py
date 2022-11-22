    if msg.content.startswith('$jogu tchubaron'):
        mensagem = msg.content.strip()[16:]
        if mensagem == 'status':
            fatos[autor]['status']['Sanidade'] = 50
            fatos[autor]['status']['Popularidade'] = 50
            fatos[autor]['status']['Notas'] = 50
            fatos[autor]['status']['Inteligência'] = 50
            return
        if mensagem == 'morte':
            fatos[autor]['status']['Sanidade'] = 1
            fatos[autor]['status']['Popularidade'] = 1
            fatos[autor]['status']['Notas'] = 1
            fatos[autor]['status']['Inteligência'] = 1
            return
        if mensagem.startswith('Sanidade'):
            mensagem = msg.content.strip()[25:]
            fatos[autor]['status']['Sanidade'] = int(mensagem)
            return
        if mensagem.startswith('Popularidade'):
            mensagem = msg.content.strip()[29:]
            fatos[autor]['status']['Popularidade'] = int(mensagem)
            return
        if mensagem.startswith('Notas'):
            mensagem = msg.content.strip()[22:]
            fatos[autor]['status']['Notas'] = int(mensagem)
            return
        if mensagem.startswith('Inteligência'):
            mensagem = msg.content.strip()[29:]
            fatos[autor]['status']['Inteligência'] = int(mensagem)
            return
        if mensagem.startswith('appender'):
            mensagem = msg.content.strip()[25:]
            if int(mensagem) not in senarios and int(mensagem) in estados:
                senarios.append(int(mensagem))
            return
        if mensagem.startswith('remover'):
            mensagem = msg.content.strip()[24:]
            if int(mensagem) in senarios: #and int(mensagem) in estados(?)
                senarios.remove(int(mensagem))
            return
        if int(mensagem) in estados:
            fatos[autor]['partida'] = int(mensagem)
            return