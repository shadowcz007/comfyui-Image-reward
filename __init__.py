
from .nodes.Score import ImageRewardScoreNode,ImageBatchToList_

# 要导出的所有节点及其名称的字典
# 注意：名称应全局唯一
NODE_CLASS_MAPPINGS = {
    "ImageBatchToList_":ImageBatchToList_,
    "ImageRewardScore_":ImageRewardScoreNode
 
}

# 一个包含节点友好/可读的标题的字典
NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageBatchToList_":"Image Batch To List",
    "ImageRewardScore_":"Image Reward"
}