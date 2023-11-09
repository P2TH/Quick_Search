import os
import crop
import cv2
import opencv_ration_resize_class as resize

class img_controller:

    # 크롭 컨트롤러
    def crop_con(img_path, label_txt):
        crop_object = crop.crop(cv2.imread(img_path), label_txt)
        crop_object.crop()
        print("Crop success!")


    # 이미지 크기 변환 컨트롤러
    # cv2로 이미지를 읽고, 1.3배 200x200보다 작은 경우
    def resize_con(crop_folder):
        
        # 폴더 안의 내용 전부 resize하도록 반복
        for inner_folder in os.listdir(crop_folder):
            folder_path = os.path.join(crop_folder, inner_folder)
            for img_path in os.listdir(folder_path):
                img = cv2.imread(img_path, cv2.IMREAD_COLOR)
                height, width, channels = img.shape

        rs = resize.resize_img(cv2.imread("crop_dir/3/0.jpg"))
        new_image = rs.ration_resize(size = (200,200))
        cv2.imshow("new_image",new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()