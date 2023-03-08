import argparse
from optimization.run_optimization import main
import torchvision
import os
from argparse import Namespace
import GetGUIData

args = {
    "description": 'A person with purple hair',
    "ckpt": "stylegan2-ffhq-config-f.pt",
    "stylegan_size": 512,
    "lr_rampup": 0.05,
    "lr": 0.1,
    "step": 300,
    "mode": "edit",
    "l2_lambda": 0.008,
    "id_lambda": 0.005,
    'work_in_stylespace': True,
    "latent_path": None,
    "truncation": 0.7,
    "save_intermediate_image_every": 0,
    "results_dir": "./data/ffhq/",
    "ir_se50_weights": "model_ir_se50.pth"
}








result_image = main(Namespace(**args))

torchvision.utils.save_image(result_image.detach().cpu(), os.path.join(args["results_dir"], "0.jpg"),
                                normalize=True, scale_each=True, range=(-1, 1))
args2 = {

    "dataset_name":"ffhq"

}
ex = Namespace(real=True, dataset_name="ffhq")
GetGUIData.main(ex)
