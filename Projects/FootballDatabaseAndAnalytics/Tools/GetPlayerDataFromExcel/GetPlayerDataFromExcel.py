from PlayerDefinitions.CareerInfo import CareerMode
from Tools.GetPlayerDataFromExcel.ExcelTooling import ExcelFileHandler, ExcelSheetParser
from Tools.GetPlayerDataFromExcel.WritePlayerPyFile import WritePlayerPyFileHandler

# Overwrite this file for importing another Excel file
input_excel_file = r"C:\Users\Martijn\Desktop\FIFA_Project\Careers\FIFA_12_Juventus.xlsx"
# Overwrite this value for another career mode object
career_mode = CareerMode.FIFA_12_JUVENTUS
# Output folder
output_folder = "player_output"


# Inspect the Excel Sheet and get all the player names from the sheet names
excel_file_handler = ExcelFileHandler(input_excel_file)
sheet_names = excel_file_handler.get_sheet_names()

for player in sheet_names:
    sheet_info = ExcelSheetParser(input_excel_file, player, career_mode).get_all_sheet_info()

    player_file_writer =  WritePlayerPyFileHandler(output_folder)
    player_file_writer.generate_player_file(sheet_info)

print(f"Generated {len(sheet_names)} player files!")