
import json
import inference
import logging

infer = inference.Inference()


def predict(event, context):
    try:
        body = json.loads(event['body'])
        context.log(body)
        preds = infer.classify_image(body['image'])
        context.log(preds)
        logging.info(f"prediction: {preds}")

        return {
            "statusCode": 200,
            "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    "Access-Control-Allow-Credentials": True,
                    "X-test": "beket"
                },
            "body": json.dumps({"prediction": preds['class']})
        }
    except Exception as e:
        logging.error(e)
        return {
            "statusCode": 500,
            "headers": {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*',
                    "Access-Control-Allow-Credentials": True,
                    "X-test": "beket"
                },
            "body": json.dumps({"error": repr(e), "owner": "Beket Myr"})
        }