import requests
content  = ""
headers = {"Authorization": "Basic cmtfbGl2ZV81MUw5c3JLQ29GamtETjR4UGtvdEs2V0dHUHFmd2tnd3RFNkkxcTFURTlrdktzZ0s3SlQ5Mk5oaUFHeGpKeDQ0ejdHZnBzU1hZNmtpTVkyTTFWWkhFajJZVjAwbjRPS3pUSlg6"}
result = requests.get("https://api.stripe.com/v1/customers", headers=headers).json()
license_code = [customer['metadata'].get('license_code', 'No license code') for customer in result['data']]
for code in license_code:
    content = content + code + "\n"
with open("activities.txt", "w") as file:
    file.write(content)
