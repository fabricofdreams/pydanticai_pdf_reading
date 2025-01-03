from icecream import ic
from pydantic_ai.models.openai import OpenAIModel
from PyPDF2 import PdfReader
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
import os
from pydantic import BaseModel
import logfire


load_dotenv()

logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))
model = OpenAIModel('gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY"))


class PatientInfo(BaseModel):
    name: str
    date: str
    diagnosis: str
    medication: str


# Define the PydanticAI Agent
pdf_agent = Agent(
    model=model,
    deps_type=None,
    result_type=PatientInfo,
    retries=3,
    system_prompt=(
        "You are a medical data extractor. Use the `extract_patient_info` function to extract structured data such as:"
        "patient name, age, diagnosis, and medication from unstructured medical text."
        "If you cannot find the information, return None for the field."
    ),
)

# Define the tool for structured data extraction


@pdf_agent.tool
def extract_patient_info(ctx: RunContext[None], text: str) -> PatientInfo:
    """
    Extracts structured data from unstructured medical text.
    Args:
        text: The unstructured text from the PDF file.

    Returns:
        A dictionary containing patient's name, date of consultation, diagnosis, and medication.
    """
    # This would rely on the AI model's ability to parse and extract information
    # from the provided text.
    return {
        'name': None,  # Extracted patient name
        'date': None,  # Extracted patient date of consultation
        'diagnosis': None,  # Extracted diagnosis
        'medication': None,  # Extracted medications
    }

# Function to read the PDF file and extract text


def read_pdf(file_path):
    """Reads a PDF file and extracts text."""
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

# Extracting PDF file names from a directory


def get_pdf_list(directory_path):
    """
    Creates a list of all PDF file names in a given directory.

    Parameters:
    - directory_path (str): Path to the directory containing the PDF files.

    Returns:
    - list: A list of PDF file names.
    """
    pdf_list = []
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_list.append(file)
    return pdf_list

# Main workflow


def process_medical_pdf(file_path):
    """
    Process a medical PDF file to extract structured data.

    Args:
        file_path: Path to the medical PDF file.

    Returns:
        Extracted structured data.
    """
    # Extract text from the PDF
    pdf_text = read_pdf(file_path)

    # Run the agent with the extracted text
    try:
        result = pdf_agent.run_sync(pdf_text)

    except Exception as e:
        ic(f"Error during agent execution: {e}")
        raise

    # Return the structured data
    return result.data


# Example Usage
if __name__ == "__main__":
    # Replace with your directory path
    directory_path = "/Users/fernandorobledo/Documents/Dev/pydai"
    pdf_list = get_pdf_list(directory_path)
    ic(pdf_list)
    # Loop through the PDF files and process them
    for pdf_file_path in pdf_list:
        ic(pdf_file_path)
        structured_data = process_medical_pdf(pdf_file_path)
        ic(structured_data)
