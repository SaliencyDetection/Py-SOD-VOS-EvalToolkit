import os
from collections import OrderedDict

__all__ = ["output_path", "all_dataset_path", "use_indexfile", "user_setting"]


# 数据集路径
datasets_root = "/home/lart/Datasets/"

## RGBD
lfsd_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "LFSD", "Mask")
njudte_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "njud_test_jw.lst")
nlprte_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "nlpr_test_jw.lst")
nlprfull_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "NLPR_FULL", "Mask")
njudfull_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "NJUD_FULL", "Mask")
rgbd135_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "RGBD135", "Mask")
dutrgbdte_path = os.path.join(
    datasets_root, "Saliency/RGBDSOD", "DUT-RGBD/Test", "Mask"
)
sip_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "SIP", "Mask")
ssd_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "SSD", "Mask")
stereo_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "STEREO-1000", "Mask")
rgbdtr_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "rgbd_train_jw.lst")


## RGB
ecssd_path = os.path.join(datasets_root, "Saliency/RGBSOD", "ECSSD/Mask")
dutomron_path = os.path.join(datasets_root, "Saliency/RGBSOD", "DUT-OMRON/Mask-5166")
hkuis_path = os.path.join(datasets_root, "Saliency/RGBSOD", "HKU-IS/Mask-1447")
pascals_path = os.path.join(datasets_root, "Saliency/RGBSOD", "PASCAL-S/Mask")
dutste_path = os.path.join(datasets_root, "Saliency/RGBSOD", "DUTS/Test/Mask")
socte_path = os.path.join(datasets_root, "Saliency/RGBSOD", "SOC/Mask")


all_dataset_path = {
    "rgbd": OrderedDict(
        {
            "LFSD": lfsd_path,
            "NJUD": njudte_path,
            "NLPR": nlprte_path,
            "RGBD135": rgbd135_path,
            "SIP": sip_path,
            "SSD": ssd_path,
            "STEREO": stereo_path,
            "DUTRGBD": dutrgbdte_path,
        }
    ),
    "rgb": OrderedDict(
        {
            "DUTS": dutste_path,
            "ECSSD": ecssd_path,
            "PASCAL-S": pascals_path,
            "DUT-OMRON": dutomron_path,
            "HKU-IS": hkuis_path,
            "SOC": socte_path,
        }
    ),
}

# 使用文件索引的数据集对应的图片路径，若是没有文件索引的数据集，可以置空
# 这里使用的数据keys必须是root_data中存在的
use_indexfile = {
    "NJUD": njudfull_path,
    "NLPR": nlprfull_path,
}


OURS_1_root = "/home/lart/Coding/HDFNet/output/HDFNet/pre"
OURS_1 = {
    "lfsd": os.path.join(OURS_1_root, "lfsd"),
    "njud": os.path.join(OURS_1_root, "njud"),
    "nlpr": os.path.join(OURS_1_root, "nlpr"),
    "rgbd135": os.path.join(OURS_1_root, "rgbd135"),
    "sip": os.path.join(OURS_1_root, "sip"),
    "ssd": os.path.join(OURS_1_root, "ssd"),
    "stereo": os.path.join(OURS_1_root, "stereo"),
    "dutrgbd": None,
}

OURS_2_root = "/home/lart/Coding/HDFNet/output/HDFNet/original_pre"
OURS_2 = {
    "lfsd": os.path.join(OURS_2_root, "lfsd"),
    "njud": os.path.join(OURS_2_root, "njud"),
    "nlpr": os.path.join(OURS_2_root, "nlpr"),
    "rgbd135": os.path.join(OURS_2_root, "rgbd135"),
    "sip": os.path.join(OURS_2_root, "sip"),
    "ssd": os.path.join(OURS_2_root, "ssd"),
    "stereo": os.path.join(OURS_2_root, "stereo"),
    "dutrgbd": None,
}

AFNet_root = "/home/lart/Datasets/SaliencyPaper/RGBD对比模型结果/TotalRGBD/AFNet"
AFNet = {
    "lfsd": os.path.join(AFNet_root, "LFSD"),
    "njud": os.path.join(AFNet_root, "NJU2K-TEST"),
    "nlpr": os.path.join(AFNet_root, "NLPR-TEST"),
    "rgbd135": os.path.join(AFNet_root, "DES"),
    "sip": os.path.join(AFNet_root, "SIP"),
    "ssd": os.path.join(AFNet_root, "SSD"),
    "stereo": os.path.join(AFNet_root, "STERE"),
    "dutrgbd": None,
}

MINet_root = "/home/lart/coding/Paper_Code/Other_Files/Out"
MINet = {
    "duts": os.path.join(MINet_root, "DUTS", "VGG16FCN_OctDeV1TransV1_2Loss"),
    "ecssd": os.path.join(MINet_root, "ECSSD", "VGG16FCN_OctDeV1TransV1_2Loss"),
    "pascal-s": os.path.join(MINet_root, "PASCAL-S", "VGG16FCN_OctDeV1TransV1_2Loss"),
    "dut-omron": os.path.join(MINet_root, "DUT-OMRON", "VGG16FCN_OctDeV1TransV1_2Loss"),
    "hku-is": os.path.join(MINet_root, "HKU-IS", "VGG16FCN_OctDeV1TransV1_2Loss"),
    "soc": os.path.join(MINet_root, "SOC", "VGG16FCN_OctDeV1TransV1_2Loss"),
}


SCRN_root = "/home/lart/Datasets/SaliencyPaper/SCRN/SCRN_SOD/saliency_maps"
SCRN = {
    "duts": os.path.join(SCRN_root, "DUTS-TEST"),
    "ecssd": os.path.join(SCRN_root, "ECSSD"),
    "pascal-s": os.path.join(SCRN_root, "PASCAL-S"),
    "dut-omron": os.path.join(SCRN_root, "DUT-OMRON"),
    "hku-is": os.path.join(SCRN_root, "HKU-IS"),
    "soc": os.path.join(SCRN_root, "SOC-TEST"),
}

CPD_root = "/home/lart/coding/Git/CPD/results/ResNet50"
CPD = {
    "duts": os.path.join(CPD_root, "DUTS-TEST"),
    "ecssd": os.path.join(CPD_root, "ECSSD"),
    "pascal-s": os.path.join(CPD_root, "PASCAL-S"),
    "dut-omron": os.path.join(CPD_root, "DUT-OMRON"),
    "hku-is": os.path.join(CPD_root, "HKU-IS"),
    "soc": os.path.join(CPD_root, "SOC/Test"),
}

all_methods_info = OrderedDict(
    {
        "OURS_1": {
            "path_dict": OURS_1,
            "curve_setting": {
                "line_color": "red",
                "line_style": "-",
                "line_label": "OURS_1$^{\dag}$",
                "line_width": 3,
            },
        },
        "OURS_2": {
            "path_dict": OURS_2,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "OURS_2$^{\dag}$",
                "line_width": 2,
            },
        },
    }
)

output_path = "./output"  # 存放输出文件的文件夹
user_setting = {
    "data_mode": "rgbd",  # 待评估数据的模式，可以设置为rgbd或rgb，这对应于本文件中`all_dataset_path`中的不同数据集路径
    "bit_num": 3,  # 评估结果保留的小数点后数据的位数
    "resume_record": False,  # 是否保留之前的评估记录（针对record_path文件有效）
    "suffix": {"pre": ".png", "gt": ".png"},  # 预测结果的扩展名和真值数据的扩展名
    "eval_single_setting": {  # 针对单个模型评估的设置
        "pred_path": OURS_1,  # 待评估的预测结果的路径
        "model_name": "OURS",  # 待评估的模型名字
        "record_path": os.path.join(output_path, "record.txt"),  # 用来保存测试结果的文件的路径
        "export_xlsx": False,  # 是否导出xlsx文件
        "xlsx_path": os.path.join(output_path, "rgbd_results.xlsx"),  # xlsx文件的路径
    },
    "eval_all_setting": {  # 针对多个模型评估比较的设置
        "all_methods_info": all_methods_info,  # 包含所有待比较模型结果的信息和绘图配置的字典
        "record_path": os.path.join(output_path, "all_record.txt"),  # 用来保存测试结果的文件的路径
        "save_npy": True,  # 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
        "npy_name": "all_methods_on_all_datasets.npy",  # 导出的npy文件的路径
        "axes_setting": {  # 不同曲线的绘图配置
            "pr": {  # pr曲线的配置
                "x_label": "Recall",  # 横坐标标签
                "y_label": "Precision",  # 纵坐标标签
                "x_lim": (0, 1),  # 横坐标显示范围
                "y_lim": (0, 1),  # 纵坐标显示范围
            },
            "fm": {  # fm曲线的配置
                "x_label": "Threshold",  # 横坐标标签
                "y_label": "F$_{0.3}$",  # 纵坐标标签
                "x_lim": (0, 1),  # 横坐标显示范围
                "y_lim": (0.1, 1),  # 纵坐标显示范围
            },
        },
    },
}
