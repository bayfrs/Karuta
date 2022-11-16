
import gdown

url = "https://drive.google.com/file/d/1NdSujVIFdgx8IdxW3fOWs64IYY9yaI7Q/view?usp=drivesdk"
output = "karuta.zip"
gdown.download(url, output, quiet=False)

