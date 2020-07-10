import argparse
import os
from collections import defaultdict
from pprint import pprint

import numpy as np
from tqdm import tqdm

from config import output_path, all_dataset_path, use_indexfile, user_setting
from utils.recorder import CurveDrawer, MetricRecorder, TxtRecorder
from utils.misc import (
    get_gt_pre_with_name,
    get_name_list_and_suffix,
    make_dir,
)

"""
Include: Fm Curve/PR Curves/MAE/(max/mean/weighted) Fmeasure/Smeasure/Emeasure

NOTE:
* Our method automatically calculates the intersection of `pre` and `gt`.
    But it needs to have uniform naming rules for `pre` and `gt`.
* The method to be tested needs to be given in the `config.py` file according to the format of the
    example, and the `user_setting` should be properly configured.
"""

my_parser = argparse.ArgumentParser(
    description="The code is created by Youwei Pang and Xiaoqi Zhao.",
    epilog="Enjoy the program! :)",
    allow_abbrev=False,
)
my_parser.version = "1.0.0"
my_parser.add_argument("-v", "--version", action="version")
my_parser.add_argument(
    "--mode",
    choices=["all", "pr", "fm"],
    required=True,
    type=str,
    help="The mode for running the script. "
    "`all`: Fm Curve/PR Curves/MAE/Fmeasure/Smeasure/Emeasure;"
    "`pr`: plot the pr curve;"
    "`fm`: plot the fm curve",
)
args = my_parser.parse_args()

make_dir(output_path)
record_path = user_setting["eval_all_setting"]["record_path"]
all_methods_info = user_setting["eval_all_setting"]["all_methods_info"]
data_mode = user_setting["data_mode"]
dataset_path_dict = all_dataset_path[data_mode]
save_npy = user_setting["eval_all_setting"]["save_npy"]
qualitative_npy_path = os.path.join(
    output_path,
    data_mode + "_" + user_setting["eval_all_setting"]["qualitative_npy_name"],
)
quantitative_npy_path = os.path.join(
    output_path,
    data_mode + "_" + user_setting["eval_all_setting"]["quantitative_npy_name"],
)
resume_record = user_setting["resume_record"]


def main():
    mode = args.mode
    if mode == "all":
        cal_all_metrics()
    elif mode == "pr":
        draw_pr_fm_curve(mode="pr")
    else:
        draw_pr_fm_curve(mode="fm")


def cal_all_metrics():
    """
    Save the results of all models on different datasets in a `npy` file in the form of a dictionary.
    {
      dataset1:{
        method1:[(ps, rs), fs],
        method2:[(ps, rs), fs],
        .....
      },
      dataset2:{
        method1:[(ps, rs), fs],
        method2:[(ps, rs), fs],
        .....
      },
      ....
    }"""
    all_qualitative_results_dict = defaultdict(dict)  # Two curve metrics
    all_quantitative_results_dict = defaultdict(dict)  # Six numerical metrics

    txt_recoder = TxtRecorder(txt_path=record_path, resume=resume_record)

    for dataset_name, dataset_path in dataset_path_dict.items():
        txt_recoder.add_row(row_name="Dataset", row_data=dataset_name)

        # 获取图片根目录
        gt_root = (
            use_indexfile[dataset_name]
            if dataset_name in use_indexfile.keys()
            else dataset_path
        )

        # ==>> test the intersection between pre and gt for each method <<==
        for method_name, method_info in all_methods_info.items():
            method_result_path_dict = method_info["path_dict"]
            dataset_name = get_valid_key_name(
                data_dict=method_result_path_dict, key_name=dataset_name
            )
            if method_result_path_dict[dataset_name] is None:
                print(
                    f" ==>> {method_name} does not have results on {dataset_name} <<== "
                )
                continue

            # 预测结果存放路径下的图片文件名字
            pre_list, pre_ext = get_name_list_and_suffix(
                method_result_path_dict[dataset_name]
            )
            # 真值名字列表
            gt_list, gt_ext = get_name_list_and_suffix(gt_root)
            # get the intersection
            eval_list = list(set(gt_list).intersection(set(pre_list)))
            print(
                f" ==>> It is evaluating {method_name} with {len(eval_list)} images <<== "
            )

            metric_recoder = MetricRecorder(
                eval_length_for_fm=len(eval_list), beta_for_wfm=1
            )
            for img_name in tqdm(eval_list, total=len(eval_list), leave=False):
                gt, pre = get_gt_pre_with_name(
                    gt_root=gt_root,
                    pre_root=method_result_path_dict[dataset_name],
                    img_name=img_name,
                    pre_ext=pre_ext,
                    gt_ext=".png",
                )
                metric_recoder.update(pre=pre, gt=gt)

            mae, (maxf, meanf, fs, ps, rs), sm, em, wfm = metric_recoder.show(
                bit_num=user_setting["bit_num"]
            )

            all_qualitative_results_dict[dataset_name.lower()].update(
                {method_name: {"prs": (ps, rs), "fs": fs}}
            )

            all_quantitative_results_dict[dataset_name.lower()].update(
                {
                    method_name: {
                        "MaxF": maxf,
                        "MeanF": meanf,
                        "WFM": wfm,
                        "MAE": mae,
                        "SM": sm,
                        "EM": em,
                    }
                }
            )

        txt_recoder.add_method_results(
            data_dict=all_quantitative_results_dict[dataset_name.lower()],
            method_name=dataset_name,
        )

    if save_npy:
        np.save(
            qualitative_npy_path, all_qualitative_results_dict,
        )
        np.save(
            quantitative_npy_path, all_quantitative_results_dict,
        )
        print(
            f" ==>> all methods have been saved in {qualitative_npy_path} and {quantitative_npy_path} <<== "
        )

    print(f" ==>> all methods have been tested:")
    pprint(all_quantitative_results_dict)


def draw_pr_fm_curve(mode: str):
    mode_axes_setting = user_setting["eval_all_setting"]["axes_setting"][mode]
    x_label, y_label = mode_axes_setting["x_label"], mode_axes_setting["y_label"]
    x_lim, y_lim = mode_axes_setting["x_lim"], mode_axes_setting["y_lim"]

    all_qualitative_results_dict = np.load(
        os.path.join(qualitative_npy_path), allow_pickle=True,
    ).item()

    curve_drawer = CurveDrawer(
        row_num=2, col_num=(len(dataset_path_dict.keys()) + 1) // 2
    )

    for idx, (dataset_name, dataset_path) in enumerate(dataset_path_dict.items()):
        dataset_name = get_valid_key_name(
            data_dict=all_qualitative_results_dict, key_name=dataset_name
        )
        dataset_results = all_qualitative_results_dict[dataset_name]

        for method_name, method_info in all_methods_info.items():
            method_name = get_valid_key_name(
                data_dict=dataset_results, key_name=method_name
            )
            method_results = dataset_results.get(method_name, None)
            if method_results:
                curve_drawer.add_subplot(idx + 1)
            else:
                print(
                    f" ==>> {method_name} does not have results on {dataset_name} <<== "
                )
                continue

            if mode == "pr":
                assert isinstance(method_results["prs"], (list, tuple))
                y_data, x_data = method_results["prs"]
            else:
                y_data, x_data = method_results["fs"], np.linspace(1, 0, 255)

            curve_drawer.draw_method_curve(
                dataset_name=dataset_name,
                method_curve_setting=method_info["curve_setting"],
                x_label=x_label,
                y_label=y_label,
                x_data=x_data,
                y_data=y_data,
                x_lim=x_lim,
                y_lim=y_lim,
            )
    curve_drawer.show()


def get_valid_key_name(data_dict: dict, key_name: str) -> str:
    if data_dict.get(key_name.lower(), "keyerror") == "keyerror":
        key_name = key_name.upper()
    else:
        key_name = key_name.lower()
    return key_name


if __name__ == "__main__":
    main()
