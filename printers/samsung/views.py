#from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
import os

printers = {1: 'floor1', 2: 'floor2', 3: 'hr'}
printers_ips = {1: '172.25.120.32', 2: '172.25.120.33', 3: '172.25.120.35'}

def index(request):
    if request.method == "GET":
        return render(request, 'samsung/index.html')
    elif request.method == "POST":
        printer = int(request.POST['printer'])
        page_number = int(request.POST['page_number'])
        deadline_page_counter = str(int(getPageCounter(printer)) + page_number)
        response = "Data sent for " + str(printers[printer]) + " | current page counter: " + str(getPageCounter(printer)) + " | deadline page counter: " + deadline_page_counter
        response_bad = "Problem with sending data to zabbix!!!"
        result = os.system("zabbix_sender -z 172.25.30.34 -s 'Printer " + printers[printer] + "' -k deadline.page.counter." + printers[printer] + f" -o {deadline_page_counter}")

        if result == 0:
            return render(request, 'samsung/index.html', {'response':response})
        else:
            return render(request, 'samsung/index.html', {'response':response_bad})



def getPageCounter(number):
    current_page_counter = os.popen("snmpwalk -v 2c -c public " + printers_ips[number] + " | grep 'iso.3.6.1.2.1.43.10.2.1.4.1.1' | awk '{print $4}'").read()
    return current_page_counter



