from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


def summarise_code(code):
    python_splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON, chunk_size=1000, chunk_overlap=0
    )
    python_docs = python_splitter.create_documents([code])

    summary_chain = (
        {"code": lambda x: x.page_content}
        | ChatPromptTemplate.from_template(
            "Provide a short summary for the following python code in one line:\n\n{code}"
        )
        | ChatOpenAI(max_retries=0)
        | StrOutputParser()
    )
    summaries = summary_chain.batch(python_docs, {"max_concurrency": 5})

    return summaries
