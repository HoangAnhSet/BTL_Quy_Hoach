import Node
import InitialTopo
import MENTOR
import EsauWilliam
import xlsxwriter

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
outWorkbookOne = xlsxwriter.Workbook("out3.xlsx")
outSheetOne = outWorkbookOne.add_worksheet()

outSheetOne.write("A1", "Name")
outSheetOne.write("B1", "x")
outSheetOne.write("C1", "y")
outSheetOne.write("D1", "traffic")
outSheetOne.write("E1", "weight")
outSheetOne.write("F1", "awarPoint")
outSheetOne.write("G1", "distanceToCenter")
#C:\Users\A\Documents\BTL Quy Hoạch\Thông Tin Mạng.txt
for i in range(NumNode):
    print("Name:",ListPosition[i].get_name(),"weight",ListPosition[i].get_weight())
    outSheetOne.write(i+1, 0, ListPosition[i].get_name())
    outSheetOne.write(i+1, 1, ListPosition[i].get_position_x())
    outSheetOne.write(i+1, 2, ListPosition[i].get_position_y())
    outSheetOne.write(i+1, 3, ListPosition[i].get_traffic())
    outSheetOne.write(i+1, 4, ListPosition[i].get_weight())
    outSheetOne.write(i+1, 5, ListPosition[i].get_award())
    outSheetOne.write(i+1, 6, ListPosition[i].get_distance())    

outWorkbookOne.close()
ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,0,True)
outWorkbookTwo = xlsxwriter.Workbook("PrintNodeTruyNhap4.xlsx")
outSheet = outWorkbookTwo.add_worksheet()
indexRow = 0
indexCol = 0 
for i in ListMentor:
    indexCol = 0
    for j in i:
        outSheet.write(indexRow,indexCol, j.get_name())
        indexCol = indexCol + 1
        
    indexRow = indexRow + 1
ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,4,False)
outWorkbookTwo.close()


Node.printList2D(ListFinish)
Node.matplot_total(ListFinish,MAX)
Node.plt.show()





