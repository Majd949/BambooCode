


# bamboo_store = [[0, 130, 260, 370, 480, 590], [0, 110, 220, 320, 410, 500]]
#
# bamboo_len = [[[130, 260, 370, 480, 590], [130, 240, 350, 460], [110, 220, 330], [110, 220], [110]], \
#               [[110, 220, 320, 410, 500], [110, 210, 300, 390], [100, 190, 280], [90, 180], [90]]]
#
# # print('First bamboo knotes:', bamboo_store[0])
# # print('First bamboo lengths:', bamboo_len[0])
#
# des_values = [130, 220, 100, 190, 210, 390, 310, 131, 256, 222, 435, 491]

class bamboo:

    def __init__(self, id, len, kPos):
        self.id = id
        self.len = len
        self.kPos = kPos

    def info(self):
        return "id: {}\nLength: {}\nKnots: {}".format(self.id, self.len, self.kPos)

    def messure(self):
        for i in range(len(self.kPos)):
            temp = []
            for j in range(len(self.kPos)):
                if j < len(self.kPos)-1-i:
                    temp.append(abs(self.kPos[i] - self.kPos[j+1+i]))

            if temp:
                dic["dist{}{}".format(self.id, i)] = distances(self.id, temp)


class distances:

    def __init__(self, id, dist):
        self.id = id
        self.dist = dist

    def messure_info(self):
        return self.id, self.dist



def find_index(id, sub_id, num):
    if num != "ALL":
        return dic["dist{}{}".format(id, sub_id)].messure_info()[1][num]
    else:
        return dic["dist{}{}".format(id, sub_id)].messure_info()[1]


dic = {}
#
# for i in range(2):
#     dic["bam{}".format(i)] = bamboo(i, 590, [0, 130, 260, 370, 480, 590])



bam01 = bamboo(0, 590, [0, 130, 260, 370, 480, 590])
bam02 = bamboo(1, 500, [0, 110, 220, 320, 410, 500])

bam01.messure()
bam02.messure()

# print(dic["dist00"].messure_info())
# print(dic["dist10"].messure_info())

# print(dic["dist{}{}".format(0,1)].messure_info()[0])

# print(find_index(0,0,"ALL"))
# print(find_index(0,0,2))



des_values = [130, 220, 100, 190, 210, 390, 310, 370, 131, 256, 222, 435, 491]

for i in range(len(dic)):
    for j in range(len(dic)):
        try:
            ac = dic["dist{}{}".format(i,j)].messure_info()
            # [print([i,j, ac[1].index(item)], item) for item in des_values if item in ac[1]]
            for item in des_values:
                if item in ac[1]:
                    val_ind = ac[1].index(item)
                    print([i, j], item)
                    if val_ind > 0:
                        [ac[1].pop(item) for item in range(0,val_ind)]
        except:
            pass

