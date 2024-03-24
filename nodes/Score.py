import ImageReward as RM
import numpy as np
from PIL import Image
import folder_paths
import os

model_path=os.path.join(folder_paths.models_dir, "image_reward")

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
                "score":("FLOAT",{
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 1, #Maximum value
                    "step": 0.01, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),
                "images": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("STRING","IMAGE",)
    RETURN_NAMES = ("SCORE_STRING","IMAGE",)
    OUTPUT_NODE = True
    CATEGORY = "♾️Mixlab/Image"
    FUNCTION = "run"

    def run(self, prompt,score, images):
        model=RM.load(
            os.path.join(model_path,'ImageReward.pt'),
            med_config=os.path.join(model_path,'med_config.json'),
            bert_pretrained_model_name_or_path=os.path.join(model_path,'bert')
            )

        images_r=[]
        score_sum = 0.0
        for image in images:
          # convert to PIL image
          i = 255.0 * image.cpu().numpy()
          img = Image.fromarray(np.clip(i, 0, 255).astype(np.uint8))
          s=model.score(prompt, [img])
          score_sum += s
          if s>score:
              images_r.append(image)
              
        score_sum /= len(images)
        return (str(score_sum),images_r,)

