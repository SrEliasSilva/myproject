from googleapiclient.discovery import build
from googleapiclient.discovery import build

# Build the Forms API service
forms_service = build('forms', 'v1', credentials=creds)

# Get the form information using the URL
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSfTt9BOzCTa4GeBQ5RA6lUSMmIU9xYsQ6Vel22bMnF-uxC0TQ/viewform?usp=sf_link'
form_id = form_url.split('/')[-2]
form = forms_service.forms().get(formId=form_id).execute()



# Build the Forms API service
forms_service = build('forms', 'v1', credentials=creds)

# Get the responses to the form
response = forms_service.responses().list(formId=form_id).execute()
items = response.get('responses', [])

# Print the responses
for item in items:
    print(f'Response ID: {item["responseId"]}')
    for answer in item['answers']:
        print(f'Question: {answer["question"]}')
        print(f'Answer: {answer["answer"]}')
        print('---')
