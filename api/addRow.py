import gspread
from oauth2client.service_account import ServiceAccountCredentials


def addRow(row_values):
    print("START addRow()")
    print("row_values")
    print(row_values)
    
    credentials = ServiceAccountCredentials.from_json_keyfile_name('../credentials.json')
    client = gspread.authorize(credentials)    
    spreadsheet_list = client.list_spreadsheet_files()
    print("spreadsheet_list")
    print(spreadsheet_list)
    # client.create(title="iMatch products")
    
    sh = client.open_by_key('1FfmbtfQaFDflDk1BBSWIJMULc0f-5L63LbvPFdhczBc')
    # sh.share('idanbit80@gmail.com', perm_type='user', role='writer', with_link=True,)
    worksheet = sh.get_worksheet(0)
    worksheet.append_row(row_values)

