from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .forms import apply_form
from .models import apply_inform
import xlwt

def index(request) :

    if request.method == "POST" :
        form = apply_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['customer_name']
            address= form.cleaned_data['customer_address']
            p = apply_inform(customer_name=name, customer_address=address)
            p.save()
            return HttpResponseRedirect('/success/')
    else:
        form = apply_form()

    return render(request, 'index2.html', {'form':form})



def download_excel_data(request):
    # content-type of response
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.xls"'

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = ['Column 1', 'Column 2', 'Column 3', 'Column 4', ]

	#write column headers in sheet
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheet body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	data = apply_inform() #dummy method to fetch data.
	for my_row in data:
		row_num = row_num + 1
		ws.write(row_num, 0, my_row.name, font_style)
		ws.write(row_num, 1, my_row.start_date_time, font_style)
		ws.write(row_num, 2, my_row.end_date_time, font_style)
		ws.write(row_num, 3, my_row.notes, font_style)

	wb.save(response)
	return response

# Create your views here.
