import gspread
from oauth2client.service_account import ServiceAccountCredentials


def addRows(row_values):
    print("START addRow()")
    print("row_values")
    print(row_values)
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name('static/data/data.json')
    client = gspread.authorize(credentials)    
    spreadsheet_list = client.list_spreadsheet_files()
    print("spreadsheet_list")
    print(spreadsheet_list)
    # client.create(title="iMatch products")
    
    sh = client.open_by_key('1FfmbtfQaFDflDk1BBSWIJMULc0f-5L63LbvPFdhczBc')
    # sh.share('idanbit80@gmail.com', perm_type='user', role='writer', with_link=True,)
    worksheet = sh.get_worksheet(0)

    if isinstance(row_values[0], list):
        # Multi rows
        worksheet.append_rows(row_values)
    else:
        worksheet.append_row(row_values)

