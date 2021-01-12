import torch
import torch.nn.functional as F

def dice_loss(pred, truth):

    truth = F.one_hot(truth, num_classes = pred.shape[1]).permute(0,3,1,2).contiguous()
    loss = 1-((2*truth*pred + 1) / (truth + pred + 1))

    return torch.mean(loss)
