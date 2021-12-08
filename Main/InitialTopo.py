# Thư viện
import random
import math
import matplotlib.pyplot as plt
import Node

def sortListPosition(m):
    return m.get_position_x()

def Global_Init_Topo(MAX,NumNode,DeBug):
    '''

    Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng

    '''
    print("{:*<100}".format(''))
    print("Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng")
    print("{:*<100}".format(''))
    ListPosition = []


    # Tạo các nút ở vị trí random và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
    for i in range(NumNode):
        n = Node.Node()
        n.create_position(MAX)
        n.create_name(i + 1)
        ListPosition.append(n)
      #  ListPosition.sort(key=sortListPosition)

    # Cài đặt lại vị trí các nút theo đề bài
    # Nút 1 -> ListPosition[0]

    # Tạo ma trận lưu trữ thông tin về lưu lượng giữa các nút.

    TrafficMatrix = [[0] * NumNode for i in range(NumNode)]

    # for i in TrafficMatrix:
    #     for j in i:
    #         print(j,end=' ')
    #     print()

    # Đưa thông tin lưu lượng vào ma trận

    # Đưa thông tin bằng điểm cố định

    def set_traffic(m, n, value):
        TrafficMatrix[m - 1][n - 1] = value
        TrafficMatrix[n - 1][m - 1] = value

    # Đưa thông tin về mối quan hệ
    def set_traffic0(m, n, value):
        TrafficMatrix[m][n] = value
        TrafficMatrix[n][m] = value

    for i in range(NumNode):

        if i + 3 < NumNode:
            set_traffic0(i, i + 3, 1)
        if i + 4 < NumNode:
            set_traffic0(i, i + 4, 3)
        if i + 6 < NumNode:
            set_traffic0(i, i + 6, 2)

    set_traffic(10, 34, 10)
    set_traffic(35, 67, 14)
    set_traffic(48, 70, 14)
    set_traffic(18, 76, 10)
    set_traffic(25, 73, 14)

    # for i in TrafficMatrix:
    #     for j in i:
    #         print(j,end=' ')
    #     print()

    # Sau khi có ma trận lưu lượng, Tiến hành tính lưu lượng của mỗi nút và cập nhật vào nút

    for i in range(len(ListPosition)):
        ListPosition[i].set_traffic(sum(TrafficMatrix[ListPosition[i].get_name() - 1]))
        # ListPosition[i].print()

    # Cập nhật giá EsauWilliam của các nút

    # Danh sách các nút có w = 2
    weightes2 = []
    for i in range(1,11):
        weightes2.append(i*8)
    print(weightes2);
    for i in ListPosition:
        if (i.get_name()) in weightes2:
            i.set_weight_ew(2)
        else:
            i.set_weight_ew(1)

    if DeBug:

        print("---------Topology mạng-------------")
        Node.printInitialList(ListPosition)

        print("----------Kết thúc tạo topology-------------")

    Node.matplotList(ListPosition, MAX)
    Node.plt.show()
    return ListPosition

def Global_Init_Topo_Fix_Position(MAX,NumNode,DeBug):
    '''

    Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng

    '''
    print("{:*<100}".format(''))
    print("Bước 1: Dựng Topology mạng và tính toán lưu lượng tại từng nút mạng")
    print("{:*<100}".format(''))
    ListPosition = []

    ListXY = []

    for i in range(NumNode):
        ListXY.append([(i%10)*0.1*MAX,(i//10)*0.1*MAX])


    # Tạo các nút ở vị trí xác định và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
    for i in range(NumNode):
        n = Node.Node()
        n.set_position(ListXY[i][0],ListXY[i][1])
        n.create_name(i + 1)
        ListPosition.append(n)
      #  ListPosition.sort(key=sortListPosition)

    # Cài đặt lại vị trí các nút theo đề bài
    # Nút 1 -> ListPosition[0]

    # Tạo ma trận lưu trữ thông tin về lưu lượng giữa các nút.

    TrafficMatrix = [[0] * NumNode for i in range(NumNode)]

    # for i in TrafficMatrix:
    #     for j in i:
    #         print(j,end=' ')
    #     print()

    # Đưa thông tin lưu lượng vào ma trận

    # Đưa thông tin bằng điểm cố định

    def set_traffic(m, n, value):
        TrafficMatrix[m - 1][n - 1] = value
        TrafficMatrix[n - 1][m - 1] = value

    # Đưa thông tin về mối quan hệ
    def set_traffic0(m, n, value):
        TrafficMatrix[m][n] = value
        TrafficMatrix[n][m] = value

###


###    Cấu hình mạng


###

    for i in range(NumNode):
        if i + 3 < NumNode:
            set_traffic0(i, i + 3, 1)
        if i + 4 < NumNode:
            set_traffic0(i, i + 4, 3)
        if i + 6 < NumNode:
            set_traffic0(i, i + 6, 2)

    set_traffic(10, 34, 10)
    set_traffic(35, 67, 14)
    set_traffic(48, 70, 14)
    set_traffic(18, 76, 10)
    set_traffic(25, 73, 14)

###

###    Kết Thúc Cấu hình mạng

###

    # Sau khi có ma trận lưu lượng, Tiến hành tính lưu lượng của mỗi nút và cập nhật vào nút

    for i in range(len(ListPosition)):
        ListPosition[i].set_traffic(sum(TrafficMatrix[ListPosition[i].get_name() - 1]))
        # ListPosition[i].print()

    # Cập nhật giá EsauWilliam của các nút

    # Danh sách các nút có w = 2
    weightes2 = []
    for i in range(1,11):
        weightes2.append(i*8)
    print(weightes2);
    for i in ListPosition:
        if (i.get_name()) in weightes2:
            i.set_weight_ew(2)
        else:
            i.set_weight_ew(1)

    if DeBug:

        print("---------Topology mạng-------------")
        Node.printInitialList(ListPosition)

        print("----------Kết thúc tạo topology-------------")
    Node.matplotList(ListPosition, MAX)
    Node.plt.show()
    return ListPosition