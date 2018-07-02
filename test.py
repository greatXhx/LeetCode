# row = ['F13','F14','J0','G0','J2','J1','J3','F11','E7','E8','E9','E10','D11','E11','E12','G5','E14','E15','G4','B10','E13','H6','B11','B14','B15','H8','H10','H7','H9','G2','H11','J5','H12','D9','D8','B13','D10','G7','G6','G8','G11','D5','B8','J14','G15','G10','E0','G12','E1','K6','G14','B9','E2','G13','E3','J15','G9','K3','K4','I6','I10','I7','I9','K7','E4','E6','I4','E5','I8','Z0','I5','F0','I12','C13','I11','F1','I13','I14','H4','H5']
#
# row1 = [[],[],[]]
# for item in range(len(row)):
#     row1[0].append(row[item][0])
#     row1[1].append(ord(row[item][0])-65)
#     row1[2].append(int(row[item][-1]))
# for item in range(len(row1)):
#     print(len(row1[item]))
#     print(row1[item])
#
# print(row1[1][1:27])
# print(row1[1][40:67])
# print(row1[2][1:27])
# print(row1[2][40:67])
c = [[1,2,3], [4,5,6], [7,8,9]]
cc = [n for a in c for n in a]
ccc = [n for a in c for n in a]
print(ccc)