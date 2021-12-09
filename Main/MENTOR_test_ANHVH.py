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
    if i == 16 | i == 21 | i == 48 :
        ListPosition[i].set_weight(9)
    if i == 36 | i == 41 | i == 46 :
        ListPosition[i].set_weight(3)
    if i == 56 | i == 44 | i == 86 :
        ListPosition[i].set_weight(7)
    else:
        ListPosition[i].set_weight(1)
# Cài đặt lại vị trí các nút theo đề bài
# Nút 1 -> ListPosition[0]

ListPosition.sort(key=sortListPosition)
print("---------Kết quả topology mạng (sắp xếp theo trục tọa độ Ox)-------------")



ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,4,True)
ListFinish = EsauWilliam.Esau_William(ListMentor,w_ew,MAX,4,False)



Node.printList2D(ListFinish)
Node.matplot_total(ListFinish,MAX)
Node.plt.show()





