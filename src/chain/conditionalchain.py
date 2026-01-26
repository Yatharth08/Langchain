from transformers import pipeline

sentiment = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

print(sentiment("I didn't like this movie at all.")[0]["label"])
