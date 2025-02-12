import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']
    nombre_carpeta = event['body']['carpeta']

    # Proceso    
    s3 = boto3.client('s3')
    response = s3.put_object(Bucket=nombre_bucket, Key=(nombre_carpeta+'/'))
    return {
        'statusCode': 201,
        'bucket': response
    }
