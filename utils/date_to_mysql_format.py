# dd/mm/yyyy  ->  yyyy-mm-dd
def date_to_mysql_format(date):
  return (
    date[6] + date[7] + date[8] + date[9] + '-' +
    date[3] + date[4] + '-' +
    date[1] + date[0]
  )