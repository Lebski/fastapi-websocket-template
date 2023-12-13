
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import dotenv

conversations = {}

dotenv.load_dotenv()

chat_model = ChatOpenAI()


def handle_chat_message(message, seed=400):

    human_message = HumanMessage(content=message)

    model_kwargs = {
        "seed": seed
    }

    response = chat_model.invoke([human_message], **model_kwargs)

    # Return the generated chat message
    return response.content


print(handle_chat_message("Hello there"))
