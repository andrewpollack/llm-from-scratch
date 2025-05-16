"""Environment verification module for LLM-from-scratch project.

This module prints information about the Python environment,
including Python version, PyTorch version, CUDA availability,
and platform details.
"""

# Standard library imports
import sys
import platform
from typing import NoReturn

# Third-party library imports
import torch


def set_seeds(seed: int = 42) -> None:
    """Set seeds for reproducibility.

    Args:
        seed: The seed value to use for random number generators
    """
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    import numpy as np
    import random

    np.random.seed(seed)
    random.seed(seed)


def main() -> NoReturn:
    """Print environment information.

    Displays Python version, PyTorch version, CUDA availability,
    and platform information.
    """
    print("Python:", sys.version)
    print("PyTorch:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("Platform:", platform.platform())


if __name__ == "__main__":
    main()
