# Thư viện
import random
import math
import matplotlib.pyplot as plt
import math
import Node

num_inf = math.inf
num_ninf = -math.inf

# Các cài đặt mặc định

MAX = 55
NumNode = 8
RadiusRatio = 0.35
C = 12
w = 2
w_ew = 3
DeBug = 1

ListMentor = []



def sortListPosition(m):
    return m.get_position_x()


def printList(_list):
    for i in _list:
        i.print()
    print()


def printList2D(_list):
    for i in _list:
        for j in i:
            print(j.get_name(), end=' ')
        print()
    print()


ListPosition = []

# Tạo các nút ở vị trí random và đưa vào danh sách, sắp xếp các nút theo thứ tự tọa độ x tăng dần
for i in range(NumNode):
    n = Node.Node()
    n.create_position(MAX)
    n.create_name(i + 1)
    ListPosition.append(n)
    ListPosition.sort(key=sortListPosition)

# Cập nhật vị trí theo đề bài

ListPosition[0].set_ew_pre('D', 30, 20, 0)
ListPosition[1].set_ew_pre('A', 0, 20, 1)
ListPosition[2].set_ew_pre('B', 10, 40, 1)
ListPosition[3].set_ew_pre('C', 40, 40, 2)
ListPosition[4].set_ew_pre('E', 50, 20, 1)
ListPosition[5].set_ew_pre('F', 50, 0, 2)
ListPosition[6].set_ew_pre('G', 40, 0, 1)
ListPosition[7].set_ew_pre('H', 10, 0, 1)

printList(ListPosition)

link_cost = [[num_inf] * NumNode for i in range(NumNode)]


def print_linkcostmatrix(_link_cost):
    for i in range(len(_link_cost)):
        for j in range(len(_link_cost[i])):
            print(_link_cost[i][j], end='\t')
        print()


def set_linkcost(_link, i, j, c):
    _link[i][j] = c
    _link[j][i] = c


# Xây dựng hàm cập nhật giá theo distance (cost = distance)

def calc_distance_2Dpoint(a,b):
    return math.sqrt((a.get_position_x()-b.get_position_x())**2+(a.get_position_y()-b.get_position_y())**2)

def link_cost_by_distance(_list,_link_cost):
    for i in range(len(_list)):
        for j in range(i+1,(len(_list))):
            set_linkcost(_link_cost,i,j,calc_distance_2Dpoint(_list[i],_list[j]))



# Cập nhật giá theo đề bài
'''
0:D
1:A
2:B
3:C
4:E
5:F
6:G
7:H
'''

set_linkcost(link_cost, 0, 1, 3)
set_linkcost(link_cost, 0, 2, 2)
set_linkcost(link_cost, 0, 3, 7)
set_linkcost(link_cost, 0, 4, 10)
set_linkcost(link_cost, 0, 5, 9)
set_linkcost(link_cost, 0, 6, 8)
set_linkcost(link_cost, 0, 7, 5)

set_linkcost(link_cost, 1, 2, 4)
set_linkcost(link_cost, 1, 6, 3)
set_linkcost(link_cost, 1, 7, 3)

set_linkcost(link_cost, 2, 3, 3)
set_linkcost(link_cost, 2, 7, 4)

set_linkcost(link_cost, 3, 4, 4)
set_linkcost(link_cost, 3, 6, 6)

set_linkcost(link_cost, 4, 5, 2)
set_linkcost(link_cost, 4, 6, 5)

set_linkcost(link_cost, 5, 6, 5)

set_linkcost(link_cost, 6, 7, 6)




print_linkcostmatrix(link_cost)

# Cập nhật thông số các nút

# weight_ew

ListPosition[1].set_weight_ew(1)
ListPosition[2].set_weight_ew(1)
ListPosition[3].set_weight_ew(2)
ListPosition[4].set_weight_ew(1)
ListPosition[5].set_weight_ew(2)
ListPosition[6].set_weight_ew(1)
ListPosition[7].set_weight_ew(1)

# Cập nhật giá về nút trung tâm ban đầu

for i in range(1, len(ListPosition)):
    ListPosition[i].set_cost_to_center(link_cost[0][i])

# Định nghĩa hàm tìm index của node khi biết tên node

def find_index_node(m):
    for i in range(0, len(ListPosition)):
        if ListPosition[i].get_name() == m:
            return i
    return 0

# Dựng ma trận quản lý trọng số

weightGroup = []


# Khởi tạo weightGroup
if DeBug:
    for i in weightGroup:
        for j in range(0, len(i)):
            print(i[j], end=' ')
        print()

def updateWG(des, src):
    index_des = find_index_node(des)
    index_src = find_index_node(src)
    node_des = ListPosition[index_des]
    node_src = ListPosition[index_src]
    sum_w = node_des.get_weight_of_group() + node_src.get_weight_of_group()
    node_des.set_weight_of_group(sum_w)

    def check_node_exist(father):
        for i in weightGroup:
            for j in range(0, len(i)):
                if i[j] == father:
                    return True
        return False

    def del_node(m_father,m_child):
        for i in weightGroup:
            tmp_a = False
            tmp_b = False
            for j in i:
                if j == m_child:
                    tmp_a = True
                if j == m_father:
                    tmp_b = True
            if tmp_a and (not tmp_b):
                weightGroup.remove(i)
    # Thêm group source vào group des



    def update_node(m_father, m_child):
        index_m_child = find_index_node(m_child)
        index_m_father = find_index_node(m_father)

        if DeBug:
            print('Check destination group exist: ', m_father, check_node_exist(m_father))
            print('Check source group exist: ', m_child, check_node_exist(m_child))
        if check_node_exist(m_father) == False:
            weightGroup.append([m_father])
            update_node(m_father, m_child)
        elif check_node_exist(m_child) == False:
            weightGroup.append([m_child])
            update_node(m_father, m_child)
        else:
            k = []

            for i in weightGroup:
                for j in range(0, len(i)):
                    # Thêm nút vào group mới
                    if i[j] == m_child:
                        k = i
            for i in weightGroup:
                for j in range(0, len(i)):
                    # Thêm nút vào group mới
                    if i[j] == m_father:
                        i.extend(k)
                        for a in i:
                            ListPosition[find_index_node(a)].set_weight_of_group(node_des.get_weight_of_group())
                            ListPosition[find_index_node(a)].set_cost_to_center(node_des.get_cost_to_center())
                            ListPosition[find_index_node(a)].set_group_node_to_center(node_des.get_group_node_to_center())
                            ListPosition[find_index_node(a)].printEW()

    update_node(des, src)
    del_node(des,src)
    if DeBug:
        for i in weightGroup:
            for j in range(0, len(i)):
                print(i[j], end=' ')
            print()

def check_limit_weight(next_connect, oneself):
    node_next_connect = ListPosition[find_index_node(next_connect)]
    node_oneself = ListPosition[find_index_node(oneself)]
    sum = node_next_connect.get_weight_of_group() + node_oneself.get_weight_of_group()
    return sum

# Định nghĩa hàm cập nhật thỏa hiệp

def cap_nhat_thoa_hiep(_list, _link_cost):
    def find_list(m_child,m_check):
        for i in weightGroup:
            for j in i:
                if j == m_child:
                    for k in i:
                        if k == m_check:
                            return True
                    return False

    for i in range(1, len(_list)):
        if _list[i].get_thoahiep() < 0:
            min_th = num_inf
            for j in range(1, len(_list)):
                if find_list(_list[i].get_name(),_list[j].get_name()):
                    continue

                subt = round(_link_cost[j][i] - _list[i].get_cost_to_center(), 4)
                if subt < min_th:
                    min_th = subt
                    _list[i].set_next_connect(ListPosition[j].get_name())
            _list[i].set_thoahiep(min_th)

# Cập nhật hàm thỏa hiệp lần đầu

for i in range(1, len(ListPosition)):
    ListPosition[i].set_connect(ListPosition[0].get_name())
    ListPosition[0].set_connect(ListPosition[i].get_name())



Node.printEWList(ListPosition)

if DeBug:
    print("Node list to backbone:", ListPosition[0].get_list_connect())

cap_nhat_thoa_hiep(ListPosition, link_cost)

if DeBug:
    print("{:-<100}".format(''))

    print("Cập nhật thỏa hiệp lần đầu")

#Node.printEWList(ListPosition)


'''

        Vòng lặp cập nhật thỏa hiệp

'''

# Định nghĩa hàm kiểm tra thỏa hiệp âm

def check_neg_thoa_hiep(_list):
    for i in range(1, len(_list)):
        if _list[i].get_thoahiep() < 0:
            return True
    return False

if DeBug:
    print(ListPosition[0].get_list_connect())

    print("------ Vào vòng lặp cập nhật thỏa hiệp ----------")

ew_loop = 1
while check_neg_thoa_hiep(ListPosition):
    if DeBug:
        print("Vòng lặp lần", ew_loop)
    ew_loop = ew_loop + 1
    # Tìm thỏa hiệp âm nhất
    min_thoa_hiep_index = 0
    min_thoa_hiep = 0
    for i in range(1, len(ListPosition)):
        if ListPosition[i].get_thoahiep() < min_thoa_hiep:
            min_thoa_hiep = ListPosition[i].get_thoahiep()
            min_thoa_hiep_index = i

    minthoahiep_node = ListPosition[min_thoa_hiep_index]
    minthoahiep_next_connect_index = find_index_node(minthoahiep_node.get_next_connect())
    minthoahiep_next_connect_node = ListPosition[minthoahiep_next_connect_index]

    if DeBug:
        print("Thỏa hiệp âm nhất tại nút", minthoahiep_node.get_name(), "bằng",
            minthoahiep_node.get_thoahiep())

    # Kiểm tra điều kiện tổng trọng số

    if check_limit_weight(minthoahiep_next_connect_node.get_name(), minthoahiep_node.get_name()) <= w_ew:
        if DeBug:
            print("Thỏa hiệp tại nút", minthoahiep_node.get_name(), "chấp nhận được. Ghép liên kết",
              minthoahiep_node.get_name(),
              minthoahiep_next_connect_node.get_name())


        # Cập nhật tổng trọng số của nhánh và node nối trung tâm của nhánh

        ListPosition[find_index_node(minthoahiep_node.get_group_node_to_center())].remove_connect(ListPosition[0].get_name())

        minthoahiep_node.set_connect(minthoahiep_next_connect_node.get_name())
        minthoahiep_next_connect_node.set_connect(minthoahiep_node.get_name())

        updateWG(minthoahiep_next_connect_node.get_name(),minthoahiep_node.get_name())

        # Cập nhật neighbor node và đường dẫn nối về trung tâm




    else:
        if DeBug:
            print("Thỏa hiệp tại nút", minthoahiep_node.get_name(), "không chấp nhận được.",
              check_limit_weight(minthoahiep_next_connect_node.get_name(), minthoahiep_node.get_name()), ">", w_ew,
              "Bỏ liên kết",
              minthoahiep_node.get_name(),
              minthoahiep_next_connect_node.get_name())
        set_linkcost(link_cost,find_index_node(minthoahiep_node.get_name()),find_index_node(minthoahiep_next_connect_node.get_name()),num_inf)



    # Cập nhật thỏa hiệp
    if DeBug:
        print("Cập nhật thỏa hiệp")
    cap_nhat_thoa_hiep(ListPosition, link_cost)
    #if DeBug:
    #    Node.printEWList(ListPosition)
    if DeBug:
        for i in weightGroup:
            for j in i:
                print(j, end=' ')
            print()

Node.matplot_esau_william(ListPosition, MAX)
Node.plt.show()