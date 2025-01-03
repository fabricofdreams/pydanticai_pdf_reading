## Setup

1. Clone the repository.
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Copy `.env.example` to `.env` and fill in your OpenAI API key and Logfire token:
   ```sh
   cp .env.example .env
   ```

## Usage

1. Place your medical PDF files in a directory.
2. Update the [directory_path](http://_vscodecontentref_/2) variable in [main.py](http://_vscodecontentref_/3) to point to your directory containing the PDF files.
3. Run the script:
   ```sh
   python main.py
   ```

## Files

- **main.py**: The main script that processes the PDF files and extracts structured data.
- **.env**: Environment variables file (not included in version control).
- **.env.example**: Example environment variables file.
- **.gitignore**: Git ignore file to exclude certain files from version control.

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key.
- `LOGFIRE_TOKEN`: Your Logfire token.

## Dependencies

- [icecream](http://_vscodecontentref_/4)
- [pydantic_ai](http://_vscodecontentref_/5)
- [PyPDF2](http://_vscodecontentref_/6)
- `python-dotenv`
- [logfire](http://_vscodecontentref_/7)

## License

This project is licensed under the MIT License.
