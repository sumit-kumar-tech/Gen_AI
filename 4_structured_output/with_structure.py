from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict,Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI()

# Schema
class Review(TypedDict):
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[Literal["positive", "negative"], "Return sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

                      Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
""")

print(result)
print(result['summary'])
print(result['sentiment'])

{'key_themes': ['Snapdragon 8 Gen 3 processor', '5000mAh battery', '45W fast charging', 'S-Pen integration', '200MP camera', 'Weight and size', 'Bloatware', 'Price tag'], 
 'summary': "Nitish Singh's review of the Samsung Galaxy S24 Ultra highlights the device's powerful Snapdragon 8 Gen 3 processor, long-lasting battery with fast charging, impressive 200MP camera, and unique S-Pen support. However, Nitish mentions concerns about the weight and size of the phone, the presence of bloatware in Samsung's One UI, and the high price tag of $1,300.", 
 
 'sentiment': 'pos', 
 
 'pros': ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'], 
 
 'cons': ['Weight and size make it uncomfortable for one-handed use', "Presence of bloatware in Samsung's One UI", 'High price tag of $1,300'], 
 
 'name': 'Nitish Singh'}