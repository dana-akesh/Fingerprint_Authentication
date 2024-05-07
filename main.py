import os
import cv2
import sys
import numpy as np


def read_image(image_path):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        img_resized = cv2.resize(image, (100, 100))

        # convert the image to numpy array
        image_np = np.array(img_resized)
        return image, image_np
    except Exception as e:
        print("Error:", e)
        return None, None


def prepare_data(path):
    dataset_list = []
    for filename in os.listdir(path):
        if filename.endswith(".BMP"):
            filepath = os.path.join(path, filename)
            img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            img_resized = cv2.resize(img, (100, 100))
            dataset_list.append(img_resized)
    dataset_list = np.array(dataset_list)
    # print("Shape of dataset_list:", dataset_list.shape)
    return dataset_list


def match_image(image1, image2):
    # calculate the similarity score based on the euclidean distance
    similarity_score = np.sqrt(np.sum((image1 - image2) ** 2))
    return similarity_score


def get_user_number(image_path):
    return image_path.split("/")[-1].split("_")[0]


def plot_roc_curve(tps_array, fps_array):
    import matplotlib.pyplot as plt
    plt.plot(fps_array, tps_array)
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("ROC Curve")
    plt.show()


def main():
    # prepare the datasets
    global tps, fps
    real_datalist = prepare_data("../Fingerprint_Authentication/dataset/real")
    # altered_datalist = prepare_data("../Fingerprint_Authentication/dataset/altered")
    # hacker_datalist = prepare_data("../Fingerprint_Authentication/dataset/hacker")

    # while input is not 3
    false_rejection = 0
    false_acceptance = 0
    true_positive = 0
    false_positive = 0
    trials = 0
    tps_array = []
    fps_array = []
    while True:
        print_menu()
        choice = input("-> Enter your choice: ")
        if choice == "1":
            user_number = input("-> Enter the user number(1-9): ")
            image_path = input("-> Enter the path of the image ☺: ")
            image, image_np = read_image(image_path)
            get_user_number(image_path)
            if image is None:
                print("Error: Image not read successfully !!")
                continue

            trials += 1
            score_list = []
            i = 1
            # loop the input image with the real dataset and save the similarity score in a list
            for real_data in real_datalist:
                score = match_image(image_np, real_data)
                score_list.append(score)
                print("User number:", i, "|| Score:", score)
                i += 1

            # calculate the mean
            mean_score = np.mean(score_list)
            print("Mean score:", mean_score)

            # calculate the standard deviation
            std_dev = np.std(score_list)
            std_dev = std_dev * 7
            std_dev = std_dev - mean_score
            print("Standard deviation:", std_dev)

            if score_list[int(user_number) - 1] < std_dev:
                if ((get_user_number(image_path))[0] != "p") and (user_number != (get_user_number(image_path))[6]):
                    false_acceptance += 1
                    print("Approved")
                elif ((get_user_number(image_path))[0] == "p") and (user_number != (get_user_number(image_path))[6]):
                    false_acceptance += 1
                    print("Approved")
                else:
                    true_positive += 1
                    print("Hello user, Approved")
            else:
                if ((get_user_number(image_path))[0] == "h"):
                    false_positive += 1
                    print("Hacker!! Rejected")
                else:
                    false_rejection += 1
                    print("Rejected")

            tps = true_positive / trials
            fps = false_positive / trials
            # store the tps and fps in arrays            fps_array = []
            tps_array.append(tps)
            fps_array.append(fps)

        elif choice == "2":
            # calculate_fmr_fnmr(real_datalist)
            fmr = false_acceptance / trials
            fnmr = false_rejection / trials
            eer = (fmr + fnmr) / 2
            print("FMR:", fmr)
            print("FNMR:", fnmr)
            print("EER:", eer)
            plot_roc_curve(tps_array, fps_array)



        elif choice == "3":
            print("Exiting the system...")
            sys.exit()
        else:
            print("Invalid. Please enter a valid choice!!")


def print_menu():
    print("-----------------Fingerprint Authentication System-----------------")
    print("1. Match the image (Log in the system)")
    print("2. Calculate the fmr, fnmr, eer, plot roc curve")
    print("2. Exit")


if __name__ == "__main__":
    #  ../Fingerprint_Authentication/dataset/altered/person6_v1.bmp
    # if ((get_user_number(image_path))[0] == "p") and (user_number == (get_user_number(image_path))[6]):
    #     false_rejection += 1
    #     print("Rejected")
    main()
