import requests
import xmltodict
import json

from django.conf import settings

def get_redirect_code(data):
    data = {
        'email': settings.EMAIL,
        'token': settings.TOKEN_ACCOUNT,
        'currency': 'BRL',
        'itemId1': '0001',
        'itemDescription1': data['pacote'],
        'itemAmount1': data['orcamento'],
        'itemQuantity1': '1',
        'senderName': data['nome'],
        'senderAreaCode': '81',
        'senderPhone': data['contato'],
        'senderEmail': data['email']+'@sandbox.pagseguro.com.br',
        'senderCPF': data['cpf'],
        'shippingAddressRequired': 'false',
        'acceptPaymentMethodGroup': 'CREDIT_CARD,BOLETO,EFT',
        'extraAmount': format(0.03*float(data['orcamento']), '.2f'),
    }

    r = requests.post(settings.CHECKOUT, data = data)
    print(r.text)
    code = xmltodict.parse(r.text)['checkout']['code']

    return {'checkoutCode': code}

def get_notification(notificationCode):

    params = {
        'email': settings.EMAIL,
        'token': settings.TOKEN_ACCOUNT,
    }

    r = requests.get(settings.NOTIFICATIONS + notificationCode, params = params)
    transaction = xmltodict.parse(r.text)['transaction']

    print("Notification Code: %s" %notificationCode)

    notification = {
        'transactionCode': transaction['code'],
        'status': status_transaction[transaction['status']],
        'paymentMethod': {
            'type': payment_method['type'][transaction['paymentMethod']['type']],
            'code': payment_method['code'][transaction['paymentMethod']['code']]
        },
        'grossAmount': transaction['grossAmount'],
        'extraAmount': transaction['extraAmount'],
        'freight': '15.00',
        'amount': str(float(transaction['grossAmount']) - float(transaction['extraAmount']) - 15.0),
        'installmentCount': transaction['installmentCount'],
        'date': transaction['date'],
        'lastEventDate': transaction['lastEventDate']
    }

    return notification

status_transaction = {
    '1': 'Aguardando Pagamento',
    '2': 'Em análise',
    '3': 'Paga',
    '4': 'Disponivel',
    '5': 'Em disputa',
    '6': 'Devolvida',
    '7': 'Cancelada',
    '8': 'Debitado',
    '9': 'Retenção temporária',
    '10': 'Em devolução'
}

payment_method = {
    'type': {
        '1': 'Cartão de Crédito',
        '2': 'Boleto',
        '3': 'Debito online'
    },
    'code': {
        '101': 'Visa',
        '102': 'MasterCard',
        '103': 'American Express',
        '104': 'Diners',
        '105': 'Hipercard',
        '106': 'Aura',
        '107': 'Elo',
        '109': 'PersonalCard',
        '110': 'JCB',
        '111': 'Discover',
        '112': 'BrasilCard',
        '113': 'FORTBRASIL',
        '115': 'VALECARD',
        '116': 'Cabal',
        '117': 'Mais!',
        '118': 'Avista',
        '119': 'GRANDCARD',
        '120': 'Sorocred',
        '202': 'Boleto Santander',
        '301': 'Bradesco',
        '302': 'Itaú',
        '304': 'Banco do Brasil',
        '306': 'Banrisul',
        '307': 'HSBC'
    }
}
