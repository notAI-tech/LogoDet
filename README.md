# LogoDet
Neural Nets for logo detection


# As a service (recommended)
```bash
# Start service
(sudo) docker run --name logodet -p 8080:8080 notaitech/fastdeploy-recipe:logodet

# Running predictions
wget https://github.com/notAI-tech/fastDeploy/blob/master/cli/fastDeploy-file_client.py
chmod +x fastDeploy-file_client.py

# Single input
./fastDeploy-file_client.py --file PATH_TO_YOUR_IMAGE

# Client side batching
./fastDeploy-file_client.py --dir PATH_TO_FOLDER --ext jpg
```

# As a Python module
```bash
git clone https://github.com/notAI-tech/LogoDet/
cd LogoDet
pip install -r requirements.txt
```

```python
# Weights will be auto-downloaded
from predictor import predictor

image_paths = [image_1.jpg, image_2.png, ...]

predictions = predictor(image_paths)

```

**Notes**:

1. Although we were able to generate/ gather data for more than 2000 unique company logos, the current release is limited to [these 292 logos](https://github.com/notAI-tech/LogoDet/releases/download/292_classes_v1/classes.txt) due to hardware constraints.
2. We recommend using LogoDet via fastDeploy, as it doesn't require the user to install dependencies separately.
