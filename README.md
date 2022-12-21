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
1. PyPDF2
2. nltk
3. heapq
4. sumy
5. streamlit

Executing program
How to run the program step-by-step.
1. pdf_classifier.ipynb
2. vert_pdf_splitter.ipynb
3. Summarization.ipynb
4. Erratum_finder.ipynb
5. getting_text.ipynb
6. Interactive_CLA_finder.py

Output
![image](https://user-images.githubusercontent.com/113432231/208945417-75bc5e12-fa6d-448d-8d30-470345ec685b.png)



# License
  
Free license


# Contact
Samuel Fooks: samuel.fooks@gmail.com
  
Nicy Jacob: nicy.ck@gmail.com


# Acknowledgments
BeCode Arai4 AI coaches(Chrysanthi and Louis)


