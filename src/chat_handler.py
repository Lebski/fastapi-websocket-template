
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import dotenv

conversations = {}

dotenv.load_dotenv()

chat_model = ChatOpenAI()


def handle_chat_message(message, user_id):

    human_message = HumanMessage(content=message)

    store_conversation(user_id, human_message)

    conversation = get_conversation(user_id)

    response = chat_model.invoke(conversation)

    # Store the conversation
    store_conversation(user_id, human_message)
    store_conversation(user_id, response)

    # Return the generated chat message
    return response.content


def store_conversation(user, message):
    if user not in conversations:
        conversations[user] = []

    conversations[user].append(message)


def get_conversation(user):
    if user not in conversations:
        return []

    return conversations[user]
