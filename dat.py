'''
# Chọn tiết diện dây dẫn dựa trên dòng điện chạy qua dây dẫn
'''
# Nhập các giá trị dòng điện

i = float(input('Cường độ dòng điện là(A): I = '));
 
if (0 < i <= 8):
    print ("Tiết diện của dây dẫn là: S = 1","mm2");
elif(8 < i <= 12):
    print("Tiết diện của dây dẫn là: S = 1.5","mm2");
elif(12 < i <= 20):
    print("Tiết diện của dây dẫn là: S = 2.5","mm2");
elif(20 < i <= 25):
    print("Tiết diện của dây dẫn là: S = 4","mm2");
elif(25 < i <= 32):
    print("Tiết diện của dây dẫn là: S = 6","mm2");
elif(32 < i <= 50):
    print("Tiết diện của dây dẫn là: S = 10","mm2");
elif(50 < i <= 65):
    print("Tiết diện của dây dẫn là: S = 16","mm2");
elif(65 < i <= 85):
    print("Tiết diện của dây dẫn là: S = 25","mm2");
else:
    print("Tiết diện của dây dẫn là: S = 35","mm2");
