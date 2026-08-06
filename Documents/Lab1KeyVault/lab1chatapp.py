from dotenv import load_dotenv
import os

from openai import AzureOpenAI


def main():

    # Clear console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:

        # Load environment variables
        load_dotenv()

        endpoint = os.getenv("FOUNDRY_ENDPOINT")
        deployment = os.getenv("MODEL_DEPLOYMENT_NAME")
        api_key = os.getenv("FOUNDRY_API_KEY")

        # Create Azure OpenAI client
        client = AzureOpenAI(
            api_key=api_key,
            azure_endpoint=endpoint,
            api_version="2025-01-01-preview"
        )

        # Conversation history
        prompt = [
            {
                "role": "system",
                "content": "Eres un asistente útil"
            }
        ]

        # Chat loop
        while True:

            input_text = input(
                "\nIngresa tu prompt (o escribe 'salir' para salir): "
            )

            if input_text.lower() == "salir":
                break

            if len(input_text.strip()) == 0:
                print("Please enter a prompt.")
                continue

            # Add user message
            prompt.append({
                "role": "user",
                "content": input_text
            })

            # Generate response
            response = client.chat.completions.create(
                model=deployment,
                messages=prompt,
                temperature=0.7,
                max_tokens=500
            )

            completion = response.choices[0].message.content

            print("\nAssistant:\n")
            print(completion)

            # Save assistant response
            prompt.append({
                "role": "assistant",
                "content": completion
            })

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
