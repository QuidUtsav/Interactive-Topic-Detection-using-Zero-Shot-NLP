from transformers import pipeline

# facebook/bart-large-mnli is the standard model for this task
classifier = pipeline(
    task="zero-shot-classification",
    model="facebook/bart-large-mnli"
)


labels = TOPICS = [
    "Technology",
    "Programming and Software Development",
    "Artificial Intelligence and Machine Learning",
    "Education and Learning",
    "Science and Research",
    "Business and Careers",
    "Health and Fitness",
    "Personal Life and Relationships",
    "Entertainment and Media",
    "Politics and Society",
    "Current Events and News",
    "Philosophy and Personal Thoughts",
    "Food and Cooking"
]

while(True):
  text = input("Enter your text to classify")
  result = classifier(text, candidate_labels=labels)
  labels = result["labels"]
  scores = result["scores"]

  topic_scores = dict(zip(labels, scores))

  top_topic, top_score = max(
      topic_scores.items(),
      key=lambda item: item[1]
  )

  print(f'Your text has similarity to {top_topic} with {top_score:.2%} confidence.')

  print("enter 1 to stop and press anything else to continue")
  if(input() == "1"):
    break
