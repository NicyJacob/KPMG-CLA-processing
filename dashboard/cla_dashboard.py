import datetime
import numpy as np
import pandas as pd
import streamlit as st
import urllib
import base64 
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode,GridUpdateMode
now = int(datetime.datetime.now().timestamp())
start_ts = now - 3 * 30 * 24 * 60 * 60

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

df = df[['jc_number','Themes', 'Sub_Themes.1', 'validity_date', 'deposit_date', 'toepassing', 'loon', 'premie', 'Werkgever', 'werkloosheid', 'bonus', 'ERRATUM', 'filename', 'Summary']]

BtnCellRenderer1 = JsCode('''
class BtnCellRenderer {
    init(params) {
        this.params = params;
        this.eGui = document.createElement('div');
        this.eGui.innerHTML = `
         <span>
            <button id='click-button' 
                class='btn-simple' 
                style='color: ${this.params.color}; 
                background-color: ${this.params.background_color}'>Summarize</button>
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
            this.refreshTable('by');
            
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

gb = GridOptionsBuilder.from_dataframe(df, enableRowGroup=True, enableValue=True, enablePivot=True)
gb.configure_default_column(editable=True, surpressSizeToFit= 'false')
gb.configure_column(field='jc_number', header_name='JC Number', suppressSizeToFit = 'false')
gb.configure_column(field = 'Themes', header_name='Theme', suppressSizeToFit = 'false')
gb.configure_column(field = 'Sub_Themes.1', header_name='Sub Theme', suppressSizeToFit = 'false')
gb.configure_column(field = 'filename', header_name='File', susppressSizeToFit='false')
gb.configure_column(field = 'deposit_date', header_name= 'Deposit Date', suppressSizeToFit='false')
gb.configure_column(field = 'validity_date', header_name='Valid Until', suppressSizeToFit='false')
gb.configure_column(field = 'Summary', width = 400)
gb.configure_columns(column_names = ['toepassing', 'Summary', 'filename', 'loon', 'premie', 'Werkgever', 'werkloosheid', 'bonus', 'ERRATUM'], hide = 'true' )
# gb.configure_column(field='toepassing', header_name='Scope')
# gb.configure_column(field='loon', header_name='Salary')
# gb.configure_column(field='premie', header_name='Premiums')
# gb.configure_column(field='Werkgever', header_name='Employer')
# gb.configure_column(field='werkloosheid', header_name='Unemployment')
# gb.configure_column(field='ERRATUM', header_name='Correction' )

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

summary_container = st.empty()

try:
    summary_cell[response['data'].clicked == 'clicked'].values[summary_cell.index[0]]
    #
    #summary_container.write(summary_string, unsafe_allow_html=True)
    #summary_string = summary_cell[response['data'].clicked == 'clicked']
    btn = st.button("Empty")

    if btn:
        #response['data']['Summary'] = 
        summary_cell[response['data'].clicked == 'clicked']
        #summary_container.write(" ")
except:
    pass
