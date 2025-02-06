import string

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app.google_api_auth import get_credentials
from app.models.day import Day
from app.models.exercise import Exercise

class SheetsService:
    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id
        self.credentials = get_credentials()
        self.service = build("sheets", "v4", credentials=self.credentials)

    def column_number_to_letter(self, n):
        """Convert a column number (1-based) to a column letter (e.g., 1 -> A, 27 -> AA)."""
        result = []
        while n > 0:
            n, remainder = divmod(n - 1, 26)
            result.append(string.ascii_uppercase[remainder])
        return ''.join(result[::-1])

    def get_day(self, mesocycle, week, day):
        try:
            sheet = self.service.spreadsheets()

            start_row = 20 + 29 * day
            end_row = 20 + 29 * day + 28

            start_col = self.column_number_to_letter(12*(week) + 2)
            end_col = self.column_number_to_letter(12*(week+1) + 3)
            range_name = f"{mesocycle}!{start_col}{start_row}:{end_col}{end_row}"

            result = (
                sheet.values()
                .get(spreadsheetId=self.spreadsheet_id, range=range_name)
                .execute()
            )
            print(result)
            exercises = []
            values = result.get("values")
            for i in range(7, 22):
                if values[i][0] != "":
                    exercise = Exercise(
                        location=i-7,
                        name=values[i][0],
                        sets=values[i][1],
                        reps=values[i][2],
                        rpe=values[i][3],
                        suggested_load=values[i][4],
                        actual_load=values[i][5],
                        actual_rpe=values[i][6],
                        notes=values[i][7],
                        actual_per=values[i][11]
                    )
                    exercises.append(exercise)
            day = Day(
                date=values[2][0],
                coach_notes=values[22][1],
                # client_feedback=values[23][0],
                exercises=exercises,
                sleep=None,
                daily_steps=None,
                cal_bef_training=None,
                daily_protein_intake=None,
                hydration=None,
                caffeine=None,
                stress=None,
                external_fatigue=None,
                training_time=None,
                training_duration=None,
                client_feedback=None
            )
            return day
        except HttpError as err:
            print(err)
            return None 

    def get_week(self, mesocycle, week):
        days = []
        for day in range(7):
            days.append(self.get_day(mesocycle, week, day))
        return days
    
    def update_exercise(self, mesocycle, week, day, exercise):
        try:
            sheet = self.service.spreadsheets()

            start_row = 20 + 29 * day
            end_row = 20 + 29 * day + 1
            exercise_location = int(exercise.location) + 7

            start_col = self.column_number_to_letter(12*(week) + 2 + 5)
            end_col = self.column_number_to_letter(12*(week+1) + 2 + 6)
            range_name = f"{mesocycle}!{start_col}{start_row+exercise_location}:{end_col}{end_row+exercise_location}"

            values = [
                [exercise.actual_load, exercise.actual_rpe]
            ]

            print(range_name)

            result = (
                sheet.values()
                .update(spreadsheetId=self.spreadsheet_id, range=range_name, valueInputOption="USER_ENTERED", body={"values": values})
                .execute()
            )
            print(result)
            return result
        except HttpError as err:
            print(err)
            return None