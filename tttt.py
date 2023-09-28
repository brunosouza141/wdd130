from jose import jwk, jwt
import requests

def validate_token(token):
    # Obtém as informações do cabeçalho do token
    headers = jwt.get_unverified_header(token)

    # Obtém as chaves públicas do Azure AD
    jwks_url = 'https://login.microsoftonline.com/seu_tenant_id/discovery/v2.0/keys'
    response = requests.get(jwks_url)
    jwks = response.json()

    # Localiza a chave pública correspondente
    key = None
    if 'keys' in jwks:
        for jwk in jwks['keys']:
            if jwk['kid'] == headers['kid']:
                key = jwk
                break

    if key is None:
        # Chave pública não encontrada
        return False

    # Verifica a assinatura do token
    try:
        jwt.decode(token, key, algorithms=['RS256'], audience='19780c49-37ca-4381-9790-7a8527cb3755')
        # Token válido
        return True
    except jwt.JWTError:
        # Token inválido
        return False
    
print(validate_token("eyJ0eXAiOiJKV1QiLCJub25jZSI6ImlJV3I4ZXZaaHlkeG15ZzNsVW9qdWo0Q1hhZzlnUEhlaUp6QXhHMlMtOGciLCJhbGciOiJSUzI1NiIsIng1dCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyIsImtpZCI6Ii1LSTNROW5OUjdiUm9meG1lWm9YcWJIWkdldyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84NmRlZTBjZC1kMTY1LTRjNTYtODAxMi1mZjkyODUzZmYzNjEvIiwiaWF0IjoxNjg3ODk4Njc4LCJuYmYiOjE2ODc4OTg2NzgsImV4cCI6MTY4NzkwMjgzNiwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFYUUFpLzhUQUFBQUtYaDRjbVJhN0w4Y1A4NmduVzdjdFl0MS9JanMrSXAyWXZMdUxKOXgvRDBVdldYVkN4Vmp2cG1JMHFZblNKTjZVcmNWa2laTmxoT2tad2FWV2lUNGJrVVJ4NVh4aytmVU5nOUFrdk95WDJHM0p5eDlnQ3lhcDJBbkQrZ0RqRlR0djFuRCsxaVhDQ3ErZDNzR09VbnArdz09IiwiYW1yIjpbInB3ZCIsInJzYSIsIm1mYSJdLCJhcHBfZGlzcGxheW5hbWUiOiJjc2Mtc2VjdXJpdHktcG9ydGFsIiwiYXBwaWQiOiI5MTNmNTE5Yi1lOWQ5LTQ2ZmYtYmE2Yy1lODJlYTViZjlhNjQiLCJhcHBpZGFjciI6IjEiLCJkZXZpY2VpZCI6ImI2ODNjZmQ4LTI3MWEtNDU2OC1iYzc4LWM1Y2ZjNGQ1MDA3MSIsImZhbWlseV9uYW1lIjoiU291emEiLCJnaXZlbl9uYW1lIjoiQnJ1bm8iLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiI0NS4yMzcuMTEwLjE5OCIsIm5hbWUiOiJCcnVubyBTb3V6YSIsIm9pZCI6IjdiYTYzMGI1LWQ4ODYtNDYyYi1hY2ZiLTE4ZGI3NTlkYjAwNCIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzMjAwMTlFRjMxRTA5IiwicmgiOiIwLkFYa0F6ZURlaG1YUlZreUFFdi1TaFRfellRTUFBQUFBQUFBQXdBQUFBQUFBQUFCNUFOSS4iLCJzY3AiOiJlbWFpbCBvcGVuaWQgcHJvZmlsZSIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6IkwyR3NiZlBaS3FiaGVGMHQ0cDNuc09lR3kzZVB6aVVwVEM4YmF0N2FpdmciLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiRVUiLCJ0aWQiOiI4NmRlZTBjZC1kMTY1LTRjNTYtODAxMi1mZjkyODUzZmYzNjEiLCJ1bmlxdWVfbmFtZSI6IkJydW5vLlNvdXphQHNrYXlsaW5rLmNvbSIsInVwbiI6IkJydW5vLlNvdXphQHNrYXlsaW5rLmNvbSIsInV0aSI6IjVxN0otV0J2OVVheElDTkNEMUk0QUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfc3QiOnsic3ViIjoiY0RaQmQzb01JN3BHS2xEVmJDQUZHSHU5Rkh3ODhxVXpiSHk0Y1ItcnM5RSJ9LCJ4bXNfdGNkdCI6MTYxMTc2MzgxNSwieG1zX3RkYnIiOiJFVSJ9.DxOZCgWEsVFsjmfCsw0t0qiKM64otbfLqUIo3wGzF_eeUBJVP38R6jbKYbX1t4QBMkUBl7J6c-Ub86FRRM2Ms-kZhB0XvVj-yk9TNmETP2QEQETjpxS1vWdxCdmafn_5ErKv_LR-4_EKNpvl_DnBL7SpGwEOQdg7DRiKOPf-FrJ8wCmk3zd2diOfITfOjpTY_NOLcFtovUiS0fLsLIT8dvrgXLcOIh8gyMAYE-XwiUKjJu573_NumnMVj18aQhydQdlhKsyw8O_NUuqWYGBzMZUFLeRyARGauCNhFcBxjqwBFelZKoJpFg_WkAKZSanXjJf-uR6lrcPIYa71L8qEZQ")) 