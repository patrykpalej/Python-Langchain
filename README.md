# Python Langchain Integrations
Python version of Langchain integrations.

Experimental approach.


### Contribution
1. Fork the repo
2. Copy .env.example to .env (ignored by Git) and insert your API keys
3. Create a virtual environment and install the requirements
4. To load `OPENAI_API_KEY` to environmental variables insert this to `venv/bin/activate` script:
```bash
OPENAI_API_KEY=<your key>
export OPENAI_API_KEY
```
5. Rewrite the code using Python applying the clean code standards. Check `01_langchain_init` and `02_langchain_format` for reference.
6. Don't remove the original .ts files
7. Create a PR. Commit messages and PR descriptions should indicate what has been done.

### Langchain tutorials
- https://www.youtube.com/watch?v=ekpnVh-l3YA&list=PL4HikwTaYE0GEs7lvlYJQcvKhq0QZGRVn

### Done
- [x] `01_langchain_init`
- [x] `02_langchain_format`
- [x] `04_tiktoken`