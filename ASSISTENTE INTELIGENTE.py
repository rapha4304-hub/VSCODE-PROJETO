print('Olá, eu sou a sua assistente, L&R. O que você quer fazer?')

comando = input('Digite um comando: ').lower()

match comando:
    case'oi':
        print('Oi, como vai você?')
    case 'tchau':
        print('Tchau, foi bom conversar com você!')
    case 'piada':
        print('Sabe qual é o padroeiro das pessoas que trabalham com TI? O São LOgin')
    case 'clima':
        print('Muito quente! Passou dos 40 graus')
    case _:
        print('Desculpe não entendi o comando.')