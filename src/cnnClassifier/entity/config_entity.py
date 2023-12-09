from dataclasses import dataclass
from pathlib import Path

#using dataclass we're creating our custom entity
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_URL: str
    local_data_file : Path
    unzip_dir: Path
    #this class will basically return all the file type stored in config.yaml This will be my entity
    #this will be my return type 

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int