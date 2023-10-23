
## Usage

* `cp .env.example .env` - copy environment file
* `docker network create network_te` - create Docker network
* `docker build -t te/langchain .` - build Docker image
* `docker run -ti --rm --name te-langchain --network network_te --env-file=.env -v $(pwd)/app:/app te/langchain bash --login` - run Docker container, you will be in the container's shell
* `python -m venv .venv` - create virtual environment
* `source .venvenv/bin/activate` - activate virtual environment
* `streamlit run app/main.py` - run Streamlit app (and open it in the browser)

### VS Code

We use .devcontainer to run the project in VS Code. So you can just open the project in VS Code and it will ask you to open it in a container.

## Papers

* https://arxiv.org/pdf/2204.00498.pdf - Evaluating the Text-to-SQL Capabilities of Large Language Models

## Documentation

* https://python.langchain.com/docs/use_cases/qa_structured/sql
* https://blog.langchain.dev/llms-and-sql/
