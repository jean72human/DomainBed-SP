import os
import time
import argparse

import warnings

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser(description="Domain generalization")

parser.add_argument("--device", type=str, default="cuda:0")
parser.add_argument("--seed", type=int, default=1)

args = parser.parse_args()

data_dir = "/home/gbetondji/Documents/ood_benchmark/data/spawrious224"
batch_size = 128

hparams_dict = {
    "SpawriousO2O_easy": {
        "ERM": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06}""",
        "LLR": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06}""",
        "FLR": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06}""",
        "GroupDRO": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06,
                "groupdro_eta": 0.0053050580120662895} """,
        "IRM": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06,
                "irm_lambda": 1.8838285530562104,
                "irm_penalty_anneal_iters": 247} """,
        "MMD": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06,
                "mmd_gamma": 7.289784897124338} """,
        "CORAL": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06,
                "mmd_gamma": 6.9018246989615895} """,
        "CausIRL_CORAL": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.00016629177873519647, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 1.1975155295174919e-06,
                "mmd_gamma": 3.5146823420446407} """,
    },
    "SpawriousM2M_hard": {
        "ERM": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05}""",
        "LLR": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05}""",
        "FLR": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05}""",
        "GroupDRO": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05,
                "groupdro_eta": 0.013378423587817576} """,
        "IRM": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05,
                "irm_lambda": 29.3676220201571,
                "irm_penalty_anneal_iters": 3001} """,
        "MMD": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05,
                "mmd_gamma": 1.0215072228839979} """,
        "CORAL": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05,
                "mmd_gamma": 0.5870292457165399} """,
        "CausIRL_CORAL": """{"batch_size": batchsize, 
                "class_balanced": false, 
                "data_augmentation": true, 
                "lr": 0.0001653813153854724, 
                "nonlinear_classifier": false, 
                "arch": "archused", 
                "resnet_dropout": 0.1,
                "weight_decay": 2.7643974709171963e-05,
                "mmd_gamma": 0.5870292457165399} """,
    },
}

hparams_dict["SpawriousO2O_medium"] = hparams_dict["SpawriousO2O_easy"]
hparams_dict["SpawriousO2O_hard"] = hparams_dict["SpawriousO2O_easy"]

hparams_dict["SpawriousM2M_easy"] = hparams_dict["SpawriousM2M_hard"]
hparams_dict["SpawriousM2M_medium"] = hparams_dict["SpawriousM2M_hard"]

for arch in ["resnet50"]:
    for algo in ["LLR"]:
        for dataset in [
            "SpawriousO2O_easy",
            "SpawriousO2O_medium",
            "SpawriousO2O_hard",
        #     "SpawriousM2M_hard",
        #     "SpawriousM2M_easy",
        #     "SpawriousM2M_medium",
        ]:
            hparams = (
                hparams_dict[dataset][algo]
                .replace("batchsize", str(batch_size))
                .replace("archused", arch)
            )
            hparams = hparams.replace("\n", "").replace(" ", "")
            print(f"Train {algo} on {dataset}")
            os.system(
                f"""python3 -m domainbed.scripts.train_n --task domain_adaptation --data_dir={data_dir}  --algorithm {algo} --test_env 0 --retrain_steps 500 --dataset {dataset} --hparams='{hparams}' --seed {args.seed} --output_dir retraining_exp_output --device {args.device} --n_iter 3"""
            )
