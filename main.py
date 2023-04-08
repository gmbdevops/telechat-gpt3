import openai
# Provide your key in python
openai.api_key = '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'
engine="text-davinci-003"
# Запрос
prompt = 'Назови лучшую Python библиотеку по машинному обучению'
# Модель
completion = openai.Completion.create(engine=engine,
                                      prompt=prompt,
                                      temperature=0.5,
                                      max_tokens=1000)
