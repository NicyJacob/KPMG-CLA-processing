# KPMG---CLA-processing
The objective of the project is to extract relevant information from CLA documents using available meta-data and artificial intelligence(NLP). The information is to be presented in a structured way so that it can be integrated into existing platforms or a new reporting tool of the client.

# Description
The project is divided into 4 steps represented in the folder structure of this repository. 
1. Document Classification - CLA can be classified into different types based on its theme. This is the exploratory stage of this project. It identifies the top 4 themes in the CLAs provided. 

2. PDF Splitter - CLA provide are in pdf format and contained 2 languages (Dutch and French). The pdf has to be split based on language into different pdfs.

3. Info Extraction - The split pdf is converted into text. This text is used to extract the summary, erratums and sentences with the keywords respectively. The output of extraction is added to the metadata (EXCEL file). The output is stored into a csv file(final.csv).

4. Insights - The csv file from Info extraction is used to build the dashboard using Power BI / Streamlite.


# Getting Started
Dependencies
Libraries needed before installing program.
PyPDF2
nltk
heapq
sumy.summarizers.luhn
Streamlite

Executing program
How to run the program
1. pdf_classifier.ipynb
2. pdf_splitter.ipynb <Check the name>
3. Summarization.ipynb
4. Erratum_finder.ipynb
5. getting_text.ipynb
6. Dashboard <Check the name>


#Authors
Contributors names and contact info

ex. Dominique Pizzie
ex. @DomPizzie


Initial Release
License
This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

Acknowledgments
Inspiration, code snippets, etc.

