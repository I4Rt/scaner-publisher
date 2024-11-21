class TableNameAssist:
    @staticmethod
    def pullYearMonthFromTablename(taablename):
        _, _, m, y = taablename.split('_')
        return y, m
    
    @staticmethod
    def tableOneIsGreaterOrEqualThanTableTwo(n1, n2):
        y1, m1 = TableNameAssist.pullYearMonthFromTablename(n1)
        y2, m2 = TableNameAssist.pullYearMonthFromTablename(n2)
        if y1 > y2:
            return True
        elif y1 == y2:
            return m1 >= m2
        return False