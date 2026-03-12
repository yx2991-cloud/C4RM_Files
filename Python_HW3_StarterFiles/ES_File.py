import numpy as np

def ES(losses, confidence=None, VaR=None, use_PnL=False):

        VaR = np.percentile(losses, 100 * confidence)
    
    losses_exceeding_var = losses[losses > VaR]
    
    if len(losses_exceeding_var) == 0:
        return 0.0
    
    es_value = np.mean(losses_exceeding_var)
    return es_value
