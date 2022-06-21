import logging
import azure.functions as func
import json
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    data = req.get_json().get('data')
    filename = req.get_json().get('filename')

    all_objs = []

    base_obj = {'filename': filename}

    data['documentResults'][0]['fields'].keys()

    for k in data['documentResults'][0]['fields'].keys():
        if k!='Items':
            base_obj[k] = data['documentResults'][0]['fields'][k]['text']

    for el in data['documentResults'][0]['fields']['Items']['valueArray']:
        new_obj = base_obj.copy()
        for k in el['valueObject'].keys():
            new_obj[k] = el['valueObject'][k]['text']
        new_obj['full_text']=el['text']
        new_obj['id'] = uuid.uuid4().hex
        all_objs.append(new_obj)

    return func.HttpResponse(
            json.dumps(all_objs),
            status_code=200
    )
