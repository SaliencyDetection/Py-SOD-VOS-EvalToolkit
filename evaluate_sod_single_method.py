# -*- coding: utf-8 -*-
# @Time    : 2020/7/8
# @Author  : Lart Pang
# @Email   : lartpang@163.com
# @File    : evaluate_single_method.py
# @Project : EvalToolBox
# @GitHub  : https://github.com/lartpang
from PIL import Image
from tqdm import tqdm

from config import (
    all_dataset_path,
    output_path,
    use_indexfile,
    user_setting,
)
from utils.recorder import XLSXRecoder, MetricRecorder, TxtRecorder
from utils.misc import (
    get_list_with_postfix,
    load_data,
    make_dir,
    normalize_pil,
)

make_dir(output_path)
pred_path_dict = user_setting["eval_single_setting"]["pred_path"]
record_path = user_setting["eval_single_setting"]["record_path"]
model_name = user_setting["eval_single_setting"]["model_name"]
gt_suffix = user_setting["suffix"]["gt"]
pre_suffix = user_setting["suffix"]["pre"]
data_mode = user_setting["data_mode"]
bit_num = user_setting["bit_num"]
dataset_path_dict = all_dataset_path[data_mode.lower()]
txt_recoder = TxtRecorder(txt_path=record_path, resume=user_setting["resume_record"])

results = {}
for dataset_name, pred_path in pred_path_dict.items():
    if not pred_path:
        print(f" ==>> {model_name} dose not results on {dataset_name}，(*^__^*)")
        continue

    dataset_name = dataset_name.upper()
    gt_path = (
        use_indexfile[dataset_name]
        if dataset_name in use_indexfile.keys()
        else dataset_path_dict[dataset_name]
    )

    name_list = get_list_with_postfix(dataset_path_dict[dataset_name], gt_suffix)
    print(f" ==>> {dataset_name}({len(name_list)}): {pred_path}")
    metric_recorder = MetricRecorder(eval_length_for_fm=len(name_list), beta_for_wfm=1)

    for i, name in tqdm(enumerate(name_list), total=len(name_list), leave=True):
        pre, gt = load_data(pred_path, gt_path, name, [pre_suffix, gt_suffix])
        if pre.size != gt.size:
            pre = pre.resize(gt.size, Image.BILINEAR)
        pre, gt = normalize_pil(pre=pre, gt=gt)

        metric_recorder.update(pre=pre, gt=gt)
    mae, (maxf, meanf, *_), sm, em, wfm = metric_recorder.show(bit_num=bit_num)
    print(
        f" ==>> {dataset_name}: MaxF {maxf}; MeanF {meanf}; MAE {mae}; Sm {sm}; Em {em}; WFm {wfm}\n"
    )

    results[dataset_name] = {
        "MaxF": maxf,
        "MeanF": meanf,
        "MAE": mae,
        "SM": sm,
        "EM": em,
        "WFM": wfm,
    }
    txt_recoder.add_method_results(
        data_dict=results[dataset_name], method_name=model_name
    )

print(f" ==>> all resutls:\n {results}")

if user_setting["eval_single_setting"]["export_xlsx"]:
    xlsx_path = user_setting["eval_single_setting"]["xlsx_path"]
    xlsx_recorder = XLSXRecoder(
        xlsx_path=xlsx_path, data_mode=user_setting["data_mode"]
    )
    xlsx_recorder.write_xlsx(model_name=model_name, data=results)
    print(f" ==>> all results have been written into the file {xlsx_path}")
