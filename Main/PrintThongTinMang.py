import Node
import InitialTopo
import MENTOR
import EsauWilliam


import pandas as pd
import openpyxl
MAX = 1000
NumNode = 150
RadiusRatio = 0.3
C = 10
w = 2
w_ew = 10

def sortListPosition(m):
    return m.get_position_x()

def printList(_list):
    for i in _list:
        i.print()

def printList2D(_list):
    for i in _list:
        for j in i:
            print(j.get_name(), end=' ')
        print()

ListPosition = []


# Tạo các nút ở vị trí random và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
for i in range(NumNode):
    n = Node.Node()
    n.create_position(MAX)
    n.create_name(i+1)
    ListPosition.append(n)    
    # ListPosition.sort(key=sortListPosition)

for i in range(NumNode):
    if i == 2 or i == 11 or i == 28 :
        ListPosition[i].set_weight(27)
    elif i == 16 or i == 21 or i == 48 :
        ListPosition[i].set_weight(9)
    elif i == 36 or i == 41 or i == 46 :
        ListPosition[i].set_weight(3)
    elif i == 56 or i == 44 or i == 86 :
        ListPosition[i].set_weight(7)
    else:
        ListPosition[i].set_weight(1)
# Cài đặt lại vị trí các nút theo đề bài
# Nút 1 -> ListPosition[0]

ListPosition.sort(key=sortListPosition)
print("---------Kết quả topology mạng (sắp xếp theo trục tọa độ Ox)-------------")
import xlsxwriter
outWorkbook = xlsxwriter.Workbook("out3.xlsx")
outSheet = outWorkbook.add_worksheet()

outSheet.write("A1", "Name")
outSheet.write("B1", "x")
outSheet.write("C1", "y")
outSheet.write("D1", "traffic")
outSheet.write("E1", "weight")
outSheet.write("F1", "awarPoint")
outSheet.write("G1", "distanceToCenter")
#C:\Users\A\Documents\BTL Quy Hoạch\Thông Tin Mạng.txt
for i in range(NumNode):
    print("Name:",ListPosition[i].get_name(),"weight",ListPosition[i].get_weight())
    outSheet.write(i+1, 0, ListPosition[i].get_name())
    outSheet.write(i+1, 1, ListPosition[i].get_position_x())
    outSheet.write(i+1, 2, ListPosition[i].get_position_y())
    outSheet.write(i+1, 3, ListPosition[i].get_traffic())
    outSheet.write(i+1, 4, ListPosition[i].get_weight())
    outSheet.write(i+1, 5, ListPosition[i].get_award())
    outSheet.write(i+1, 6, ListPosition[i].get_distance())    

outWorkbook.close()
