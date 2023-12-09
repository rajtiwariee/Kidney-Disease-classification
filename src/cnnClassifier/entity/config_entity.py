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
    