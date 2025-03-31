import datetime

class DateManager():

    weekday_name = ['Понедельник', 'Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']

    @staticmethod
    def getWeekMonday(weeks_day: datetime) -> datetime:
        return weeks_day - datetime.timedelta(weeks_day.weekday())
    
    @staticmethod
    def getWeekDates(weeks_day: datetime) -> list:
        monday = DateManager.getWeekMonday(weeks_day)
        weekdates = []
        for i in range(7):
            weekdates.append((monday + datetime.timedelta(i)).date())
        return list(zip(DateManager.weekday_name, weekdates))
    
    @staticmethod
    def getDataFromStr(date_time_str: str) -> datetime:
        return datetime.datetime.strptime(date_time_str,'%Y-%m-%d')
    
    @staticmethod
    def getLastWeek(date_time: datetime) -> datetime:
        return date_time - datetime.timedelta(7)
    
    @staticmethod
    def getNextWeek(date_time: datetime) -> datetime:
        return date_time + datetime.timedelta(7)
    
    @staticmethod
    def getCurrentDateTime() -> datetime:
        return datetime.datetime.now()
    
    @staticmethod
    def getCurrentTime() -> datetime:
        return datetime.datetime.now().time()
    
    @staticmethod
    def getCurrentDate() -> datetime:
        return datetime.datetime.now().date()

    
