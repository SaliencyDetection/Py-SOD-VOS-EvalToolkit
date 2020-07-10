import os
import numpy as np
from PIL import Image


def get_ext(path_list):
    ext_list = list(set([os.path.splitext(p)[1] for p in path_list]))
    if len(ext_list) != 1:
        if ".png" in ext_list:
            ext = ".png"
        elif ".jpg" in ext_list:
            ext = ".jpg"
        elif ".bmp" in ext_list:
            ext = ".bmp"
        else:
            raise NotImplementedError
        print(f"预测文件夹中包含多种扩展名，这里仅使用{ext}")
    else:
        ext = ext_list[0]
    return ext


def get_name_list_and_suffix(data_path: str) -> (list, str):
    name_list = []
    if os.path.isfile(data_path):
        print(f" ++>> {data_path} is a file. <<++ ")
        with open(data_path, mode="r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                img_name = os.path.basename(line.split()[0])
                data_ext = os.path.splitext(img_name)[1]
                name_list.append(os.path.splitext(img_name)[0])
                line = file.readline()
        if data_ext == "":
            # 默认为png
            data_ext = ".png"
    else:
        print(f" ++>> {data_path} is a folder. <<++ ")
        data_list = os.listdir(data_path)
        data_ext = get_ext(data_list)
        name_list = [os.path.splitext(f)[0] for f in data_list if f.endswith(data_ext)]
    name_list = list(set(name_list))
    return name_list, data_ext


def get_list_with_postfix(dataset_path: str, postfix: str):
    name_list = []
    if os.path.isfile(dataset_path):
        print(f" ++>> {dataset_path} is a file. <<++ ")
        with open(dataset_path, mode="r", encoding="utf-8") as file:
            line = file.readline()
            while line:
                img_name = os.path.basename(line.split()[0])
                name_list.append(os.path.splitext(img_name)[0])
                line = file.readline()
    else:
        print(f" ++>> {dataset_path} is a folder. <<++ ")
        name_list = [
            os.path.splitext(f)[0]
            for f in os.listdir(dataset_path)
            if f.endswith(postfix)
        ]
    name_list = list(set(name_list))
    return name_list


def rgb_loader(path):
    with open(path, "rb") as f:
        img = Image.open(f)
        return img.convert("L")


def binary_loader(path):
    assert os.path.exists(path), f"`{path}` does not exist."
    with open(path, "rb") as f:
        img = Image.open(f)
        return img.convert("L")


def load_data(pre_root, gt_root, name, postfixs):
    pre = binary_loader(os.path.join(pre_root, name + postfixs[0]))
    gt = binary_loader(os.path.join(gt_root, name + postfixs[1]))
    return pre, gt


def normalize_pil(pre, gt):
    gt = np.asarray(gt)
    pre = np.asarray(pre)
    gt = gt / (gt.max() + 1e-8)
    gt = np.where(gt > 0.5, 1, 0)
    max_pre = pre.max()
    min_pre = pre.min()
    if max_pre == min_pre:
        pre = pre / 255
    else:
        pre = (pre - min_pre) / (max_pre - min_pre)
    return pre, gt


def make_dir(path):
    if not os.path.exists(path):
        print(f"`{path}` does not exist，we will create it.")
        os.makedirs(path)
    else:
        assert os.path.isdir(path), f"`{path}` should be a folder"
        print(f"`{path}`已存在")


def get_gt_pre_with_name(
    gt_root: str, pre_root: str, img_name: str, pre_ext: str, gt_ext: str = ".png"
):
    img_path = os.path.join(pre_root, img_name + pre_ext)
    gt_path = os.path.join(gt_root, img_name + gt_ext)
    pre = Image.open(img_path).convert("L")
    gt = Image.open(gt_path).convert("L")

    if pre.size != gt.size:
        pre = pre.resize(gt.size)

    gt = np.asarray(gt)
    pre = np.asarray(pre)

    gt = gt / (gt.max() + 1e-8)
    gt = np.where(gt > 0.5, 1, 0)
    if pre.max() == pre.min():
        pre = pre / 255
    else:
        pre = (pre - pre.min()) / (pre.max() - pre.min())
    return gt, pre
