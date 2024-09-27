import json


def hello(event, context):
    body = {
        "message": "Carmen Juliana Marin Velez, el arbol de navidad ha sido generado correctamente."
    }

    punto = "*"
    height = 40
    tallo = 5
    for i in range(1,height,2):
        print ((punto*i).center(height))
            
    for j in range(tallo):
        print ((punto + " " +punto).center(height))

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
