# LogoDet
Neural Nets for logo detection


# As a service (recommended)
```bash
(sudo) docker run --name logodet -p 8080:8080 notaitech/fastdeploy-recipe:logodet
```

# As a Python module
```bash
git clone https://github.com/notAI-tech/LogoDet/
cd LogoDet
pip install -r requirements.txt
```

```python
from predictor import predictor

image_paths = [image_1.jpg, image_2.png, ...]

predictions = predictor(image_paths)

```

**Notes**:

1. Although we were able to generate/ gather data for more than 2000 unique company logos, the current release is limited to [these 292 logos](https://github.com/notAI-tech/LogoDet/releases/download/292_classes_v1/classes.txt) due to hardware constraints.
2. We recommend using LogoDet via fastDeploy, as it doesn't require the user to install dependencies separately.
