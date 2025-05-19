import json
import boto3
import base64
import datetime
import uuid

client_bedrock = boto3.client('bedrock-runtime')
client_s3 = boto3.client('s3')
dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
    input_prompt = event['prompt']
    print(input_prompt)

    prompt_id = str(uuid.uuid4())

    try:
        response_bedrock = client_bedrock.invoke_model(
            body=json.dumps({
                "text_prompts": [{"text": input_prompt}],
                "cfg_scale": 5,
                "seed": 0,
                "steps": 50
            }),
            modelId='stability.stable-diffusion-xl-v1',
            accept="application/json",
            contentType="application/json"
        )

        response_body = json.loads(response_bedrock['body'].read())
        output_image = response_body['artifacts'][0]['base64']
        image_data = base64.b64decode(output_image)

        poster_name = 'poster_' + datetime.datetime.today().strftime("%Y%m%d%H%M%S") + '.png'

        client_s3.put_object(
            Bucket='posterdesign0555',
            Key=poster_name,
            Body=image_data,
            ContentType='image/png'
        )

        url = client_s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={'Bucket': 'posterdesign0555', 'Key': poster_name},
            ExpiresIn=3600
        )

        dynamodb.put_item(
            TableName='PromptStatus',
            Item={
                'prompt_id': {'S': prompt_id},
                'prompt': {'S': input_prompt},
                'status': {'S': 'success'},
                'timestamp': {'S': datetime.datetime.utcnow().isoformat()},
                'url': {'S': url}
            }
        )

        return {'statusCode': 200, 'body': url}

    except Exception as e:
        print(f"Error: {str(e)}")

        dynamodb.put_item(
            TableName='PromptStatus',
            Item={
                'prompt_id': {'S': prompt_id},
                'prompt': {'S': input_prompt},
                'status': {'S': 'failure'},
                'timestamp': {'S': datetime.datetime.utcnow().isoformat()},
                'error_message': {'S': str(e)}
            }
        )

        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while processing the request.',
                'error': str(e)
            })
        }
