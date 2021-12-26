import Node
import InitialTopo
import MENTOR
import EsauWilliam


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
    if i == 2 | i == 11 | i == 28 :
        ListPosition[i].set_weight(27)
    elif i == 16 | i == 21 | i == 48 :
        ListPosition[i].set_weight(9)
    elif i == 36 | i == 41 | i == 46 :
        ListPosition[i].set_weight(3)
    elif i == 56 | i == 44 | i == 86 :
        ListPosition[i].set_weight(7)
    else:
        ListPosition[i].set_weight(1)
# Cài đặt lại vị trí các nút theo đề bài
# Nút 1 -> ListPosition[0]

ListPosition.sort(key=sortListPosition)
print("---------Kết quả topology mạng (sắp xếp theo trục tọa độ Ox)-------------")



ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,4,True)
import xlsxwriter
outWorkbook = xlsxwriter.Workbook("PrintNodeTruyNhap4.xlsx")
outSheet = outWorkbook.add_worksheet()
indexRow = 0
indexCol = 0 
for i in ListMentor:
    indexCol = 0
    for j in i:
        outSheet.write(indexRow,indexCol, j.get_name())
        indexCol = indexCol + 1
        
    indexRow = indexRow + 1
   
    
# for i in ListMentor:
#     outSheet.write(i+1, 0, ListPosition[i].get_name())
#         for j in i:                           
#             outSheet.write(i+1, j+1, j.get_name())
outWorkbook.close()            
# ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,4,False)



# Node.printList2D(ListFinish)
# Node.matplot_total(ListFinish,MAX)
# Node.plt.show()





