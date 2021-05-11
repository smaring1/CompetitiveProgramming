class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10, "Nov":11, "Dec":12}
        date = date.split()
        sol = date[2]
        if len(str(months[date[1]])) < 2:
            sol += "-0" + str(months[date[1]])
        else:
            sol += "-" + str(months[date[1]])
        if len(date[0][:-2]) < 2:
            sol += "-0" + date[0][:-2]
        else:
            sol += "-" + date[0][:-2]
        return sol