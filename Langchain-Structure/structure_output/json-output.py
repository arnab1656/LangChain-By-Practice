from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI()

# schema
json_schema = {
  "title": "Review",
  "type": "object",
  "properties": {
    "key_themes": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Write down all the key themes discussed in the review in a list"
    },
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["pos", "neg"],
      "description": "Return sentiment of the review either negative, positive or neutral"
    },
    "pros": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the pros inside a list"
    },
    "cons": {
      "type": ["array", "null"],
      "items": {
        "type": "string"
      },
      "description": "Write down all the cons inside a list"
    },
    "name": {
      "type": ["string", "null"],
      "description": "Write the name of the reviewer"
    }
  },
  "required": ["key_themes", "summary", "sentiment"]
}


structured_model = model.with_structured_output(json_schema)

result = structured_model.invoke("""Lionel Messi is widely regarded as one of the greatest footballers of all time, a player whose artistry has redefined the modern game. Born in Rosario, Argentina, Messi’s journey from a shy, undersized boy with a growth hormone deficiency to a global superstar is the stuff of legend. His left foot is like a paintbrush, crafting goals and assists with unmatched precision and flair. At FC Barcelona, he became the club’s all-time top scorer, winning numerous La Liga and Champions League titles while dazzling the world with his vision, dribbling, and playmaking. His transfer to Paris Saint-Germain marked a new chapter, yet his magic on the ball never faded. In 2022, he completed the one dream that eluded him — lifting the FIFA World Cup for Argentina, cementing his place alongside the greatest icons of the sport. Messi’s game is defined by balance, intelligence, and humility, a rare combination in a star of his magnitude. Fans across the globe celebrate not just his statistics but the joy he brings whenever he touches the ball. Beyond the pitch, Messi remains a symbol of dedication, resilience, and loyalty. In the story of football, his name will forever shine like gold.
""")

print("result ---> \n",result)