import os

from langchain.chains import LLMChain
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate

HUGGINGFACEHUB_API_TOKEN = os.environ.get("HUGGINGFACEHUB_API_TOKEN")
MODEL_TEMERATURE = 1
MODEL_MAX_LENGTH = 90

# See https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads
# AI_MODEL ="google/flan-t5-xxl"
# AI_MODEL ="databricks/dolly-v2-3b"
# AI_MODEL ="gpt2"
AI_MODEL = "Writer/camel-5b-hf"
# AI_MODEL = "mistralai/Mistral-7B-Instruct-v0.1"


def generate_movie_title(name: str = "Rob Zombie"):
    prompt_template_director = PromptTemplate(
        input_variables=["director_name"],
        template="Question: Generate 3 movie titles that would fit director's {director_name}'s next movie\n\nAnswer: ",
    )

    llm = HuggingFaceHub(
        repo_id=AI_MODEL,
        model_kwargs={"temperature": MODEL_TEMERATURE, "max_length": MODEL_MAX_LENGTH},
    )

    llm_chain = LLMChain(llm=llm, prompt=prompt_template_director)

    response = llm_chain({"director_name": name})

    return response


if __name__ == "__main__":
    print(generate_movie_title(name="Mark Stewartny"))
