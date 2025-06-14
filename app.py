GROQ_API_KEY = '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'

from groq import Groq

client = Groq(
    api_key=GROQ_API_KEY,
)

while True:
    chat_completion = client.chat.completions.create(
        messages=[     
            {
                'role': 'user',
                'content': 'I am pritam'
            },
            {
                'role': 'user',
                'content': input('Enter your msg:')
            }
        ],
        model="llama-3.3-70b-versatile",
        stream=False,
    )
    print(chat_completion.choices[0].message.content)
