
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import dotenv

conversations = {}

dotenv.load_dotenv()

chat_model = ChatOpenAI()


def handle_chat_message(message):

    human_message = HumanMessage(content=message)

    model_kwargs = {
        "seed": 235,
    }

    response = chat_model.invoke([human_message], **model_kwargs)

    # Return the generated chat message
    return response.content


print(handle_chat_message("Hello, world!"))
