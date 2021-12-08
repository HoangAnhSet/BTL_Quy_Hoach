import Node

import MENTOR



MAX = 7
NumNode = 8
RadiusRatio = 0.3
C = 2
w = 3.2


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
    ListPosition.append(n)
    ListPosition.sort(key=sortListPosition)

# Cài đặt lại vị trí các nút theo đề bài
# Nút 1 -> ListPosition[0]

ListPosition[0].create_name(1)
ListPosition[0].set_position(1,1)
ListPosition[1].create_name(2)
ListPosition[1].set_position(0,0)
ListPosition[2].create_name(3)
ListPosition[2].set_position(2,3)
ListPosition[3].create_name(4)
ListPosition[3].set_position(2,0)
ListPosition[4].create_name(5)
ListPosition[4].set_position(4,2)
ListPosition[5].create_name(6)
ListPosition[5].set_position(5,0)
ListPosition[6].create_name(7)
ListPosition[6].set_position(5,3)
ListPosition[7].create_name(8)
ListPosition[7].set_position(6,1)


# Đưa thông tin bằng điểm cố định

ListPosition[0].set_traffic(7)
ListPosition[1].set_traffic(3)
ListPosition[2].set_traffic(2)
ListPosition[3].set_traffic(5)
ListPosition[4].set_traffic(4)
ListPosition[5].set_traffic(4)
ListPosition[6].set_traffic(2)
ListPosition[7].set_traffic(6)

ListPosition.sort(key=sortListPosition)
print("---------Kết quả topology mạng (sắp xếp theo trục tọa độ Ox)-------------")



ListMentor = MENTOR.MenTor(ListPosition,MAX,C,w,RadiusRatio,0,True)









