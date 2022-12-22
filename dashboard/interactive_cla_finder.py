import datetime
import numpy as np
import pandas as pd
import streamlit as st
import urllib
import base64 
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode,GridUpdateMode
now = int(datetime.datetime.now().timestamp())
start_ts = now - 3 * 30 * 24 * 60 * 60
# @st.cache(allow_output_mutation=True)
# def make_data():
#     df = pd.DataFrame(
#         {
#             "timestamp": np.random.randint(start_ts, now, 20),
#             "side": [np.random.choice(["buy", "sell"]) for i in range(20)],
#             "base": [np.random.choice(["JPY", "GBP", "CAD"]) for i in range(20)],
#             "quote": [np.random.choice(["EUR", "USD"]) for i in range(20)],
#             "amount": list(
#                 map(
#                     lambda a: round(a, 2),
#                     np.random.rand(20) * np.random.randint(1, 1000, 20),
#                     )
#             ),
#             "price": list(
#                 map(
#                     lambda p: round(p, 5),
#                     np.random.rand(20) * np.random.randint(1, 10, 20),
#                     )
#             ),
#             "clicked": [""]*20,
#         }
#     )
#     df["cost"] = round(df.amount * df.price, 2)
#     df.insert(
#         0,
#         "datetime",
#         df.timestamp.apply(lambda ts: datetime.datetime.fromtimestamp(ts)),
#     )
#     return df.sort_values("timestamp").drop("timestamp", axis=1)

df = pd.read_csv(
   # "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
   "./csv_data/final2.csv"
   #"./dashboard/csv_data/final2.csv"
)
#pd.set_option('display.max_colwidth', -1)
def make_link(filename):
    link_base = 'https://public-search.werk.belgie.be/website-download-service/joint-work-convention/'
    JC_num=str(filename)[0:3] + '/'
    full_link = link_base + str(JC_num)+ str(filename)
    return full_link

df = df[['jc_number','Themes', 'Sub_Themes.1', 'validity_date', 'deposit_date', 'toepassing', 'filename', 'Summary']]
#df['link'] = df.apply(lambda x : make_link(x['filename']), axis=1 )

# def make_clickable(link):
#     # target _blank to open new window
#     # extract clickable text to display for your link
#     text = link[-10:]
#     return f'<a target="_blank" href="{link}">{text}</a>'
#    # return st.markdown(f'<a href="{url}" rel="noopener noreferrer" target="_blank">{name}</a>',unsafe_allow_html=True)

# df['hyperlink'] = df.apply(lambda x : make_clickable(x['link']), axis=1)

BtnCellRenderer1 = JsCode('''
class BtnCellRenderer {
    init(params) {
        this.params = params;
        this.eGui = document.createElement('div');
        this.eGui.innerHTML = `
         <span>
            <button id='click-button' 
                class='btn-simple' 
                style='color: ${this.params.color}; background-color: ${this.params.background_color}'>Summarize</button>
         </span>
      `;
        this.eButton = this.eGui.querySelector('#click-button');
        this.btnClickedHandler = this.btnClickedHandler.bind(this);
        this.eButton.addEventListener('click', this.btnClickedHandler);
    }
    getGui() {
        return this.eGui;
    }
    refresh() {
        return true;
    }
    destroy() {
        if (this.eButton) {
            this.eGui.removeEventListener('click', this.btnClickedHandler);
        }
    }
    btnClickedHandler(event) {
        if(this.params.getValue() == 'clicked') {
            this.refreshTable('');
        } else {
            this.refreshTable('clicked');
        }
            console.log(this.params);
            console.log(this.params.getValue());
        }
    refreshTable(value) {
        this.params.setValue(value);
    }
};
''')
# BtnCellRenderer2 = JsCode('''
# class BtnCellRenderer {
#     init(params) {
#         this.params = params;
#         this.eGui = document.createElement('div');
#         this.eGui.innerHTML = `
#          <span>
#             <button id='click-button' 
#                 class='btn-simple' 
#                 style='color: ${this.params.color}; background-color: ${this.params.background_color}'>PDF</button>
#          </span>
#       `;
#         this.eButton = this.eGui.querySelector('#click-button');
#         this.btnClickedHandler = this.btnClickedHandler.bind(this);
#         this.eButton.addEventListener('click', this.btnClickedHandler);
#     }
#     getGui() {
#         return this.eGui;
#     }
#     refresh() {
#         return true;
#     }
#     destroy() {
#         if (this.eButton) {
#             this.eGui.removeEventListener('click', this.btnClickedHandler);
#         }
#     }
#     btnClickedHandler(event) {
#         if(this.params.getValue() == 'clicked') {
#             this.refreshTable('');
#         } else {
#             this.refreshTable('clicked');
#         }
#             console.log(this.params);
#             console.log(this.params.getValue());
#         }
#     refreshTable(value) {
#         this.params.setValue(value);
#     }
# };
# ''')

gb = GridOptionsBuilder.from_dataframe(df, enableRowGroup=True, enableValue=True, enablePivot=True)
gb.configure_default_column(editable=True, surpressSizeToFit= 'false')
gb.configure_column(field='jc_number', header_name='JC Number', supressSizeToFit = 'false')
gb.configure_column(field = 'Themes', header_name='Theme', surpressSizeToFit = 'false')
gb.configure_column(field = 'Sub_Themes.1', header_name='Sub Theme', surpressSizeToFit = 'false')
gb.configure_column(field = 'filename', header_name='File', surpressSizeToFit='false')
gb.configure_column(field = 'deposit_date', header_name= 'Deposit Date', surpressSizeToFit='false')
gb.configure_column(field = 'Summary', width = 400)
gb.configure_column(field='toepassing', header_name='Scope' )
gb.configure_columns(column_names = ['toepassing', 'Summary', 'filename'], hide = 'true' )
gb.configure_side_bar()
gb.configure_selection(header_checkbox=True)
grid_options = gb.build()

grid_options['columnDefs'].append({
    #field = column header
    "field": "clicked",
    "header": "Summarize",
    "cellRenderer": BtnCellRenderer1,
    "cellRendererParams": {
        "color": "black",
        "background_color": "white",
    }
}
)
# grid_options['columnDefs'].append({
#     #field = column header
#     "field": "clicked2",
#     "header": "ViewPDF",
#     "cellRenderer": BtnCellRenderer2,
#     "cellRendererParams": {
#         "color": "white",
#         "background_color": "red",
#     }
# }
# )

st.title("Interactive CLA Finder")
# df['hyperlink'] = df['hyperlink'].to_html(escape=False)
response = AgGrid(df,
                  theme="streamlit",
                  key='table1',
                  enable_enterprise_modules=True,
                  gridOptions=grid_options,
                  allow_unsafe_jscode=True,
                  fit_columns_on_grid_load=True,
                  update_mode="GRID_CHANGED",
                  reload_data=False,
                  try_to_convert_back_to_original_types=False,
                  width = '100%',
                            
                  )
summary_cell = response['data']['Summary']


#print(response)

summary_container = st.empty()

try:

    summary_string = summary_cell[response['data'].clicked == 'clicked'].iloc[-1].values
    print(summary_string)
    summary_container.write(summary_string, unsafe_allow_html=True)
    
except:
    pass


#summary_container.write("summary here")

    #st.title("Empty")
btn = st.button("Empty")

if btn:
    summary_cell = response['data']['Summary']
    summary_container.empty()
    
    




#extra code
#if (confirm('Are you sure you want to CLICK?') == true) {
#     }
#function to display the PDF of a given file 


# def displayPDF(file):
#     # Opening file from file path. this is used to open the file from a website rather than local
#     with urllib.request.urlopen(file) as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display = F'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="950" type="application/pdf"></iframe>'

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)

from bokeh.models.widgets import Div

if st.button('Go to Streamlit'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    #js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)