# LogoDet
Neural Nets for logo detection

# Using the free API
- Signup [here](https://tech.notai.tech/signup/) for free API key.
- Maximum 16 requests per hour allowed.
- Each request can have maximum of 4 images to be processed. (i.e: maximum of 64 images can be processed per hour.)

**Example usage of the free API**

```bash
wget https://github.com/notAI-tech/fastDeploy/blob/master/cli/fastDeploy-file_client.py
chmod +x fastDeploy-file_client.py

# with webhook example
./fastDeploy-file_client.py --file ../../LogoDet/example.jpg  --url "https://tech.notai.tech/logodet/async?api_key=YOUR_API_KEY" --webhook https://fastdeploy.requestcatcher.com

# without webhook example
./fastDeploy-file_client.py --file ../../LogoDet/example.jpg  --url "https://tech.notai.tech/logodet/async?api_key=YOUR_API_KEY"

```

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
