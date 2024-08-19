from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai

app = Flask(__name__)

# Set your OpenAI API key here
openai.api_key = "org-c2J5ESDVkcVwP52RsMY92qeY"  # Replace this with your actual API key

def get_openai_response(prompt):
    response = openai.Completion.create(
        model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo", whichever is applicable
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    msg = resp.message()

    # Generate response using OpenAI API
    openai_response = get_openai_response(incoming_msg)

    msg.body(openai_response)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
