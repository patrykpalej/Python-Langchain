from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


system_template = """
# Q: 2015 is coming in 36 hours. What is the date one week from today in MM/DD/YYYY?
# If 2015 is coming in 36 hours, then today is 36 hours before.
from datetime import datetime, timedelta
today = datetime(2015, 1, 1) - timedelta(hours=36)
one_week_from_today = today + timedelta(days=7)
print(one_week_from_today.strftime('%m/%d/%Y'))

# Q: The first day of 2019 is a Tuesday, and today is the first Monday of 2019. What is the date today in MM/DD/YYYY?
from datetime import datetime, timedelta
today = datetime(2019, 1, 1) + timedelta(days=6)
print(today.strftime('%m/%d/%Y'))

# Q: The concert was scheduled to be on 06/01/1943, but was delayed by one day to today. What is the date 10 days ago in MM/DD/YYYY?
from datetime import datetime, timedelta
today = datetime(1943, 6, 1) + timedelta(days=1)
ten_days_ago = today - timedelta(days=10)
print(ten_days_ago.strftime('%m/%d/%Y'))

# Q: It is 4/19/1969 today. What is the date 24 hours later in MM/DD/YYYY?
from datetime import datetime, timedelta
today = datetime(1969, 4, 19)
later = today + timedelta(days=1)
print(later.strftime('%m/%d/%Y'))

# Q: Jane thought today is 3/11/2002, but today is in fact Mar 12, which is 1 day later. What is the date 24 hours later in MM/DD/YYYY?
from datetime import datetime, timedelta
today = datetime(2002, 3, 12)
later = today + timedelta(days=1)
print(later.strftime('%m/%d/%Y'))

# Q: Jane was born on the last day of February in 2001. Today is her 16-year-old birthday. What is the date yesterday in MM/DD/YYYY?
from datetime import datetime, timedelta
today = datetime(2001, 2, 28) + timedelta(years=16)
yesterday = today - timedelta(days=1)
print(yesterday.strftime('%m/%d/%Y'))
"""

human_template = "Q: {question}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", human_template)
])

formatted_chat_prompt = chat_prompt.format_messages(
    question="Today is October 13, 2023. What will the date after 193 days from now in the format MM/DD/YYYY?"
)

chat = ChatOpenAI(model_name="gpt-4")
content = chat.invoke(formatted_chat_prompt).content

if isinstance(content, str):
    print("Actual Date: ", end="")
    exec(content)
