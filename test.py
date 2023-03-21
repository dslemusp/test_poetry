import numpy as np
import pandas as pd
from loguru import logger

logger.info('this is a test')
df = pd.DataFrame(np.random.randn(10, 5))
print(df)