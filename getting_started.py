
import skyio
from skyio import GenericPath as Path
from dotenv import load_dotenv

load_dotenv(verbose=True)

# set the cache folder
skyio.set_cache_folder("cache")
skyio.clear_cache_folder()


from_path = Path("gs://gpr-studio-data/test.txt")
to_path = Path("D://test.txt")

from_path.download_to(to_path)
with open(to_path, "rb") as f:
    data = f.read()

from_path = Path("D://test.txt")
to_path = Path("gs://gpr-studio-data/test4.txt")

from_path.upload_to(to_path)
with open(to_path, "rb") as f:
    data = f.read()
    print(data)

skyio.list_cache_folder(max_levels=5)

