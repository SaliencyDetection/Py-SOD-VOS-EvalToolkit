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
stereo797_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "STEREO-797", "Mask")
stereo1000_path = os.path.join(datasets_root, "Saliency/RGBDSOD", "STEREO-1000", "Mask")
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
            "STEREO797": stereo797_path,
            "STEREO1000": stereo1000_path,
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


HDFNet_VGG16_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_VGG16"
HDFNet_VGG16 = {
    "lfsd": os.path.join(HDFNet_VGG16_root, "lfsd"),
    "njud": os.path.join(HDFNet_VGG16_root, "njud"),
    "nlpr": os.path.join(HDFNet_VGG16_root, "nlpr"),
    "rgbd135": os.path.join(HDFNet_VGG16_root, "rgbd135"),
    "sip": os.path.join(HDFNet_VGG16_root, "sip"),
    "ssd": os.path.join(HDFNet_VGG16_root, "ssd"),
    "stereo797": os.path.join(HDFNet_VGG16_root, "stereo797"),
    "stereo1000": os.path.join(HDFNet_VGG16_root, "stereo1000"),
    "dutrgbd": os.path.join(HDFNet_VGG16_root, "dutrgbd"),
}

HDFNet_VGG19_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_VGG19"
HDFNet_VGG19 = {
    "lfsd": os.path.join(HDFNet_VGG19_root, "lfsd"),
    "njud": os.path.join(HDFNet_VGG19_root, "njud"),
    "nlpr": os.path.join(HDFNet_VGG19_root, "nlpr"),
    "rgbd135": os.path.join(HDFNet_VGG19_root, "rgbd135"),
    "sip": os.path.join(HDFNet_VGG19_root, "sip"),
    "ssd": os.path.join(HDFNet_VGG19_root, "ssd"),
    "stereo797": os.path.join(HDFNet_VGG19_root, "stereo797"),
    "stereo1000": os.path.join(HDFNet_VGG19_root, "stereo1000"),
    "dutrgbd": os.path.join(HDFNet_VGG19_root, "dutrgbd"),
}

HDFNet_Res50_root = "/home/lart/Coding/HDFFile/output/HDFNet/HDFNet_Res50"
HDFNet_Res50 = {
    "lfsd": os.path.join(HDFNet_Res50_root, "lfsd"),
    "njud": os.path.join(HDFNet_Res50_root, "njud"),
    "nlpr": os.path.join(HDFNet_Res50_root, "nlpr"),
    "rgbd135": os.path.join(HDFNet_Res50_root, "rgbd135"),
    "sip": os.path.join(HDFNet_Res50_root, "sip"),
    "ssd": os.path.join(HDFNet_Res50_root, "ssd"),
    "stereo797": os.path.join(HDFNet_Res50_root, "stereo797"),
    "stereo1000": os.path.join(HDFNet_Res50_root, "stereo1000"),
    "dutrgbd": os.path.join(HDFNet_Res50_root, "dutrgbd"),
}


UCNet_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/CVPR2020_UCNet"
)
UCNet = {
    "lfsd": os.path.join(UCNet_root, "LFSD"),
    "njud": os.path.join(UCNet_root, "NJU2K"),
    "nlpr": os.path.join(UCNet_root, "NLPR"),
    "rgbd135": os.path.join(UCNet_root, "DES"),
    "sip": os.path.join(UCNet_root, "SIP"),
    "ssd": None,
    "stereo797": None,
    "stereo1000": os.path.join(UCNet_root, "STERE"),
    "dutrgbd": None,
}

JLDCF_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/CVPR2020_JL-DCF"
)
JLDCF = {
    "lfsd": os.path.join(JLDCF_root, "LFSD"),
    "njud": os.path.join(JLDCF_root, "NJU2K"),
    "nlpr": os.path.join(JLDCF_root, "NLPR"),
    "rgbd135": os.path.join(JLDCF_root, "RGBD135"),
    "sip": os.path.join(JLDCF_root, "SIP"),
    "ssd": None,
    "stereo797": None,
    "stereo1000": os.path.join(JLDCF_root, "STERE"),
    "dutrgbd": os.path.join(JLDCF_root, "DUT-RGBD-testing"),
}

S2MA_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/CVPR2020_S2MA"
)
S2MA = {
    "lfsd": os.path.join(S2MA_root, "LFSD"),
    "njud": os.path.join(S2MA_root, "NJU2K"),
    "nlpr": os.path.join(S2MA_root, "NLPR"),
    "rgbd135": os.path.join(S2MA_root, "RGBD135"),
    "sip": None,
    "ssd": os.path.join(S2MA_root, "SSD100"),
    "stereo797": None,
    "stereo1000": os.path.join(S2MA_root, "STERE"),
    "dutrgbd": os.path.join(S2MA_root, "DUT-RGBD"),
}

CoNet_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/ECCV2020_CoNet"
)
CoNet = {
    "lfsd": os.path.join(CoNet_root, "LFSD"),
    "njud": os.path.join(CoNet_root, "NJUD"),
    "nlpr": os.path.join(CoNet_root, "NLPR"),
    "rgbd135": os.path.join(CoNet_root, "RGBD135"),
    "sip": os.path.join(CoNet_root, "SIP"),
    "ssd": os.path.join(CoNet_root, "SSD"),
    "stereo797": os.path.join(CoNet_root, "STEREO"),
    "stereo1000": None,
    "dutrgbd": os.path.join(CoNet_root, "DUT-RGBD"),
}

BBSNet_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/ECCV2020_BBSNet"
)
BBSNet = {
    "lfsd": os.path.join(BBSNet_root, "LFSD"),
    "njud": os.path.join(BBSNet_root, "NJU2K"),
    "nlpr": os.path.join(BBSNet_root, "NLPR"),
    "rgbd135": os.path.join(BBSNet_root, "DES"),
    "sip": os.path.join(BBSNet_root, "SIP"),
    "ssd": os.path.join(BBSNet_root, "SSD"),
    "stereo797": None,
    "stereo1000": os.path.join(BBSNet_root, "STERE"),
    "dutrgbd": os.path.join(BBSNet_root, "DUT"),
}

CMWNet_root = (
    "/home/lart/Datasets/Saliency/PaperResults/RGBDSODPaperResults/ECCV2020_CMWNet"
)
CMWNet = {
    "lfsd": os.path.join(CMWNet_root, "LFSD"),
    "njud": os.path.join(CMWNet_root, "NJU2K"),
    "nlpr": os.path.join(CMWNet_root, "NLPR"),
    "rgbd135": os.path.join(CMWNet_root, "DES"),
    "sip": os.path.join(CMWNet_root, "SIP"),
    "ssd": os.path.join(CMWNet_root, "SSD"),
    "stereo797": None,
    "stereo1000": os.path.join(CMWNet_root, "STEREO"),
    "dutrgbd": os.path.join(CMWNet_root, "DUT-RGBD"),
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
        "HDFNet_VGG16": {
            "path_dict": HDFNet_VGG16,
            "curve_setting": {
                "line_color": "red",
                "line_style": "-",
                "line_label": "HDFNet$_{VGG16}$",
                "line_width": 3,
            },
        },
        "HDFNet_VGG19": {
            "path_dict": HDFNet_VGG19,
            "curve_setting": {
                "line_color": "red",
                "line_style": "-",
                "line_label": "HDFNet$_{VGG19}$",
                "line_width": 3,
            },
        },
        "HDFNet_Res50": {
            "path_dict": HDFNet_Res50,
            "curve_setting": {
                "line_color": "red",
                "line_style": "-",
                "line_label": "HDFNet$_{Res50}$",
                "line_width": 3,
            },
        },
        "UCNet": {
            "path_dict": UCNet,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "UCNet",
                "line_width": 2,
            },
        },
        "JLDCF": {
            "path_dict": JLDCF,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "JLDCF",
                "line_width": 2,
            },
        },
        "S2MA": {
            "path_dict": S2MA,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "S2MA",
                "line_width": 2,
            },
        },
        "CoNet": {
            "path_dict": CoNet,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "CoNet",
                "line_width": 2,
            },
        },
        "BBSNet": {
            "path_dict": BBSNet,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "BBSNet",
                "line_width": 2,
            },
        },
        "CMWNet": {
            "path_dict": CMWNet,
            "curve_setting": {
                "line_color": "seagreen",
                "line_style": "--",
                "line_label": "CMWNet",
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
        "pred_path": HDFNet_VGG16,  # 待评估的预测结果的路径
        "model_name": "HDFNet_VGG16",  # 待评估的模型名字
        "record_path": os.path.join(output_path, "record.txt"),  # 用来保存测试结果的文件的路径
        "export_xlsx": False,  # 是否导出xlsx文件
        "xlsx_path": os.path.join(output_path, "rgbd_results.xlsx"),  # xlsx文件的路径
    },
    "eval_all_setting": {  # 针对多个模型评估比较的设置
        "all_methods_info": all_methods_info,  # 包含所有待比较模型结果的信息和绘图配置的字典
        "record_path": os.path.join(output_path, "all_record.txt"),  # 用来保存测试结果的文件的路径
        "save_npy": True,  # 是否将评估结果到npy文件中，该文件可用来绘制pr和fm曲线
        "qualitative_npy_name": "all_qualitative_results.npy",  # 保存曲线指标数据的文件路径
        "quantitative_npy_name": "all_quantitative_results.npy",  # 保存曲线指标数据的文件路径
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
