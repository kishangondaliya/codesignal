def centuryFromYear(year):
   if year < 100:
      return 1
   year_l = int(str(year)[:2])
   year_r = str(year)[2:]
   if year_r == '00':
      return year_l
   if year_r == '0':
      return int(str(year_l)[:1])
   if len(str(year)) == 3:
      return int(str(year_l)[:1]) + 1
   return year_l + 1
