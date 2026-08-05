from dotenv import load_dotenv
import os

from openai import AzureOpenAI

from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential


def main():

    try:
        # Load environment variables
        load_dotenv()

        foundry_endpoint = os.getenv("FOUNDRY_ENDPOINT")
        deployment_name = os.getenv("MODEL_DEPLOYMENT_NAME")

        key_vault_name = os.getenv("KEY_VAULT")
        app_tenant = os.getenv("TENANT_ID")
        app_id = os.getenv("APP_ID")
        app_password = os.getenv("APP_PASSWORD")

        # Connect to Key Vault
        key_vault_uri = f"https://{key_vault_name}.vault.azure.net/"

        credential = ClientSecretCredential(
            tenant_id=app_tenant,
            client_id=app_id,
            client_secret=app_password
        )

        keyvault_client = SecretClient(
            vault_url=key_vault_uri,
            credential=credential
        )

        # Get Foundry / Azure OpenAI key
        secret_key = keyvault_client.get_secret("AI-Services-Key")
        foundry_key = secret_key.value

        # Create Azure OpenAI client
        client = AzureOpenAI(
            api_key=foundry_key,
            api_version="2024-02-15-preview",
            azure_endpoint=foundry_endpoint
        )

        # Chat loop
        user_text = ""

        while user_text.lower() != "quit":

            user_text = input("\nIngresa tu prompt (o escribe 'salir' para salir): ")

            if user_text.lower() != "salir":

                response = client.chat.completions.create(
                    model=deployment_name,
                    messages=[
                        {
                            "role": "system",
                            "content": "Eres un asistente útil."
                        },
                        {
                            "role": "user",
                            "content": user_text
                        }
                    ],
                    temperature=0.7,
                    max_tokens=500
                )

                print("\nAI Response:\n")
                print(response.choices[0].message.content)

    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()
