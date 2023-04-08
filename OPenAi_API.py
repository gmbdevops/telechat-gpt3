import openai

openai.api_key = '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'
telegram aoi=6074720866:AAEOYJUkbsrK-Ux_PPTbMS9j2MRohUUq-MM

openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
)