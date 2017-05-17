import boto3

from question import total_questions

dynamodb = boto3.resource('dynamodb','us-west-2')
table = dynamodb.Table('User_Data')

identify_key = 'Survey_Code'

def save_response(number,body):
    user = table.get_item(Key={identify_key: number, })
    user_item = user['Item']
    user_question_list = user_item['Questions']

    if len(user_question_list) < total_questions():
        user_question_list.append(body)
        table.update_item(Key={identify_key: number, }, UpdateExpression="set Questions = :m",
                          ExpressionAttributeValues={':m': user_question_list}, ReturnValues="UPDATED_NEW")
