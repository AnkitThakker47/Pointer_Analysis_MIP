from tabula import read_pdf
df=read_pdf(r"./credits.pdf",encoding="utf-8",spreadsheet=True,pages="all")
print(df)
#print(df)