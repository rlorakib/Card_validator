from bottle import route, run, template, request, view, response

from card_validator.validator import get_issuer


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/')
@view('index')
def the_real_index():
    return {
        "message":request.query.get("message","There was no message")
    }

@route('/validate')
def validate():
    card_number = request.query.get('cardNumber','').strip()

    if card_number:
        try:
            issuer = get_issuer(card_number)
        except ValueError:
            response.status = 400
            return {"result": "The card is not valid a credit number!"}

        return {"issuer":issuer,"result": "It is a {} card".format(issuer)}
    response.status=400
    return {"result": "The cardNumber is a required as a query parameter"}

run(host='localhost', port=8080)