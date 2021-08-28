import logging
from pathlib import Path

import hydra
from omegaconf import DictConfig
from omegaconf import OmegaConf

logger = logging.getLogger(__name__)


@hydra.main(config_path="../configs", config_name="default")
def main(cfg: DictConfig):
    logger.info(OmegaConf.to_yaml(cfg=cfg))

    Path(hydra.utils.get_original_cwd())

    logger.info("Train model")

    logger.info("Evaluate model")

    logger.info("Plot result")

    logger.info("Save trained model")


if __name__ == "__main__":
    main()
