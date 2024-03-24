
import numpy as np
from PIL import Image
import folder_paths
import os,sys
import torch 
import comfy.utils

sys.path.append(os.path.join(__file__,'../../'))

import ImageReward as RM

model_path=os.path.join(folder_paths.models_dir, "image_reward")


# Tensor to PIL
def tensor2pil(image):
    return Image.fromarray(np.clip(255. * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))

# Convert PIL to Tensor
def pil2tensor(image):
    return torch.from_numpy(np.array(image).astype(np.float32) / 255.0).unsqueeze(0)


class ImageBatchToList_:
    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"image_batch": ("IMAGE",), }}

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image_list",)
    OUTPUT_IS_LIST = (True,)
    FUNCTION = "run"

    CATEGORY = "♾️Mixlab/Image"

    def run(self, image_batch):
        images = [image_batch[i:i + 1, ...] for i in range(image_batch.shape[0])]
        return (images, )
    

class ImageRewardScoreNode:
    
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                # "model": ("IMAGEREWARD_MODEL",),
                "prompt": ("STRING", {
                    "multiline": True
                }),
                "topK":("INT",{
                    "default": 3, 
                    "min": 1, #Minimum value
                    "max": 500, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING","IMAGE",)
    RETURN_NAMES = ("score","images",)
    OUTPUT_NODE = True
    CATEGORY = "♾️Mixlab/Image"
    FUNCTION = "run"

    INPUT_IS_LIST = True
    OUTPUT_IS_LIST = (False,True,)

    global ir_model
    ir_model = None

    def run(self, prompt, topK , images):
        prompt=prompt[0]
        topK=topK[0]

        # print(len(images))
        global ir_model
        if ir_model==None:
            ir_model=RM.load(
                os.path.join(model_path,'ImageReward.pt'),
                med_config=os.path.join(model_path,'med_config.json'),
                bert_pretrained_model_name_or_path=os.path.join(model_path,'bert-base-uncased')
                )
        else:
            ir_model=ir_model.to("cuda" if torch.cuda.is_available() else "cpu")

        
        score_sum = []

        # 进度条
        pbar = comfy.utils.ProgressBar(len(images))

        for image in images:
          # convert to PIL image
        #   i = 255.0 * image.cpu().numpy()
        #   img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
             
            s=ir_model.score(prompt, [tensor2pil(image)])
        
            score_sum.append({
                "score":s,
                "image":image
            })
            pbar.update(1)
             
        # score_sum /= len(images)

        ir_model=ir_model.to('cpu')

        score_sum = sorted(score_sum, key=lambda x: x['score'], reverse=True)

        images_r=[]
        for x in score_sum:
            if topK>0:
                topK=topK-1
                images_r.append(x['image'])
        
        score_sum="\n".join([str(x['score']) for x in score_sum])
        # if s>score:
        #     images_r.append(image)

        return (score_sum,images_r,)

