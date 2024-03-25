# comfyui-Image-reward

![1711282071529](https://github.com/shadowcz007/comfyui-Image-reward/assets/12645064/8a604c1d-66c2-43d2-a1a4-f2c28c02f3cb)
![1711282130123](https://github.com/shadowcz007/comfyui-Image-reward/assets/12645064/1eb11f53-ac9c-406d-a16b-a672e0ea0787)


### [workflow example](./example/image-reward-workflow.json)

Collaborate with [mixlab-nodes](https://github.com/shadowcz007/comfyui-mixlab-nodes) to convert the workflow into an app.

配合[mixlab-nodes](https://github.com/shadowcz007/comfyui-mixlab-nodes)，把workflow转为app使用。



#### [ImageReward](https://github.com/THUDM/ImageReward?tab=readme-ov-file#example-use)

![image](https://github.com/shadowcz007/comfyui-Image-reward/assets/12645064/3c438a17-d57d-4ca4-960a-312cfafd7d7f)

Human preference learning in text-to-image generation. This is a paper for NeurIPS 2023, trained using the professional large-scale dataset ImageRewardDB: approximately 137,000 comparison pairs.

文本到图像生成中的人类偏好学习。这是NeurIPS 2023的一篇论文，训练使用专业的大规模数据集ImageRewardDB：约13.7万个⽐较pairs。

#### install
requirement.txt

#### models

[ImageReward](https://huggingface.co/THUDM/ImageReward/tree/main) 放到 
ComfyUI/models/image_reward/ImageReward.pt
ComfyUI/models/image_reward/med_config.json


[bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased/tree/main) 放到 ComfyUI/models/image_reward/bert-base-uncased/


