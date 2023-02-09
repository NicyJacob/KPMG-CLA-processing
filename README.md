# KPMG-CLA-processing
The aim of the project is to utilize artificial intelligence and available metadata to extract crucial information from CLA documents, and present it in a structured format for seamless integration into the client's existing platforms or a new reporting tool. This approach leverages NLP technology to streamline the process and provide accurate, actionable insights.

# Description
The project is divided into four distinct stages, which are reflected in the folder structure of the repository. These stages are:

Document Classification: In this stage, the CLA documents are classified into different categories based on their themes. Through an exploratory process, the top four themes are identified among the provided CLAs.

PDF Splitting: The CLA documents are provided in PDF format and contain both Dutch and French languages. This stage involves splitting the PDFs into separate files based on language.

Information Extraction: The split PDFs are converted into text, from which key information such as the summary, erratums, and sentences containing specific keywords is extracted. This information is then added to the metadata in an Excel file and stored in a CSV file (final.csv).

Dashboard: The final.csv file from the information extraction stage is used to build a dashboard using Streamlit.


# Getting Started
Dependencies needed before running the program.
    
        pip install PyPDF2
        pip install nltk
        pip install sumy
        pip install streamlit
        pip install heapq

Executing program
How to run the program step-by-step.
1. pdf_classifier.ipynb
2. vert_pdf_splitter.ipynb
3. Summarization.ipynb
4. Erratum_finder.ipynb
5. getting_text.ipynb
6. Interactive_CLA_finder.py

# Output

![image](https://user-images.githubusercontent.com/113432231/208945417-75bc5e12-fa6d-448d-8d30-470345ec685b.png)


# Next Steps
The project has the potential for further improvement through the implementation of topic modeling techniques to cluster the CLA documents. Additionally, a scrapper can be developed to periodically scrape new CLA documents and update the metadata file, ensuring that it is always current with the latest published CLAs. These enhancements will enhance the functionality and usefulness of the project, providing more in-depth insights into the data.

# License
  
Free license


# Contact
Samuel Fooks: samuel.fooks@gmail.com
  
Nicy Jacob: nicy.ck@gmail.com


# Acknowledgments
BeCode Arai4 AI coaches (Chrysanthi and Louis)


